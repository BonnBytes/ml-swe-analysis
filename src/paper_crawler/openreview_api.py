"""This module talks to the OpenReview API.

OpenReview now blocks headless browsers and plain downloads,
so we get PDF links and the PDFs themselves through the API.
"""

import functools
import os
import urllib.parse

import openreview
from dotenv import load_dotenv


def openreview_credentials() -> dict[str, str]:
    """Get the OpenReview login arguments from the environment or a .env file.

    Prefer a stored token, accounts with multi-factor authentication
    can only log in interactively. Create one with scripts/openreview_token.py.

    Returns:
        dict[str, str]: Keyword arguments for the OpenReview clients.
    """
    load_dotenv()
    if os.environ.get("OPENREVIEW_TOKEN"):
        return {"token": os.environ["OPENREVIEW_TOKEN"]}
    return {
        "username": os.environ["OPENREVIEW_USERNAME"],
        "password": os.environ["OPENREVIEW_PASSWORD"],
    }


@functools.cache
def _v1_client() -> openreview.Client:
    return openreview.Client(
        baseurl="https://api.openreview.net", **openreview_credentials()
    )


@functools.cache
def _v2_client() -> openreview.api.OpenReviewClient:
    return openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net", **openreview_credentials()
    )


def pdf_link(note_id: str) -> str:
    """Build the PDF link for an OpenReview note.

    Args:
        note_id (str): The id of the submission note.

    Returns:
        str: The PDF link, download_pdf can fetch it.
    """
    return f"https://openreview.net/pdf?id={note_id}"


def download_pdf(link: str) -> bytes:
    """Download the PDF behind an OpenReview PDF link through the API.

    Each API version only knows its own notes, try v2 first and fall back to v1.

    Args:
        link (str): A link created by pdf_link.

    Returns:
        bytes: The PDF file.
    """
    note_id = urllib.parse.parse_qs(urllib.parse.urlparse(link).query)["id"][0]
    try:
        return _v2_client().get_pdf(note_id)
    except openreview.OpenReviewException:
        return _v1_client().get_pdf(note_id)


def get_iclr_pdf_2019() -> list[str]:
    """Get the PDF links of the accepted ICLR 2019 papers.

    ICLR 2019 uses the v1 API. Each submission has a meta review with the final recommendation.

    Returns:
        list[str]: PDF links of all oral and poster papers.
    """
    client = _v1_client()
    submissions = client.get_all_notes(
        invitation="ICLR.cc/2019/Conference/-/Blind_Submission",
        details="directReplies",
    )
    accepted = [
        submission
        for submission in submissions
        if any(
            reply["invitation"].endswith("/Meta_Review")
            and reply["content"].get("recommendation", "").startswith("Accept")
            for reply in submission.details["directReplies"]
        )
    ]
    return [pdf_link(submission.id) for submission in accepted]


def get_iclr_pdf_2018() -> list[str]:
    """Get the PDF links of the accepted ICLR 2018 papers.

    ICLR 2018 uses the v1 API and has a single decision invitation for all papers.
    Workshop track invitations do not count as accepted.

    Returns:
        list[str]: PDF links of all oral and poster papers.
    """
    client = _v1_client()
    decisions = client.get_all_notes(
        invitation="ICLR.cc/2018/Conference/-/Acceptance_Decision"
    )
    return [
        pdf_link(decision.forum)
        for decision in decisions
        if decision.content.get("decision", "").startswith("Accept")
    ]
