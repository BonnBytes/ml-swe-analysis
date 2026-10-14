"""Log in to OpenReview once and store an API token in .env."""

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
