"""Log in to OpenReview once and store an API token in .env.

OpenReview accounts with multi-factor authentication need an interactive login.
Run this script in a terminal, enter the TOTP code, and the crawler code and
tests then use the stored token without asking again. The token expires after
one week, run this script again to refresh it.

Usage:
    uv run --no-project --with openreview-py --with python-dotenv \
        python scripts/openreview_token.py
"""

import os

import openreview
from dotenv import find_dotenv, load_dotenv, set_key

ONE_WEEK = 7 * 24 * 60 * 60

if __name__ == "__main__":
    dotenv_path = find_dotenv(usecwd=True) or ".env"
    load_dotenv(dotenv_path)
    client = openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net",
        username=os.environ["OPENREVIEW_USERNAME"],
        password=os.environ["OPENREVIEW_PASSWORD"],
        tokenExpiresIn=ONE_WEEK,
    )
    set_key(dotenv_path, "OPENREVIEW_TOKEN", client.token, quote_mode="never")
    print(f"Stored OPENREVIEW_TOKEN in {dotenv_path}, valid for one week.")
