import httpx
import json
import logging

"""
run: pip3 install -r requirements.txt
"""

# Here you can change the logging level:
logging.basicConfig(level=logging.DEBUG)


def create_client(base_url: str, token: str) -> httpx.Client:
    """Create a client."""

    client = httpx.Client(
        base_url=base_url,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"token {token}",
        },
    )
    return client


def get_latest_issues(client: httpx.Client, org_ids: list[str]) -> httpx.Response:
    """Get latest issues."""

    # This filter allows you to narrow the results.

    filters = {
        "filters": {
            "orgs": org_ids,
            "severity": [
                "critical",
            ],
            "types": [
                "vuln"
            ],
            "ignored": False,
            "projects": ["..."],
        }
    }
    response = client.post(f"/reporting/counts/issues?from=2020-08-01&to=2020-08-03&groupBy=severity", data=json.dumps(filters))
    return response.json()


def main():
    """Main function."""

    SNYK_TOKEN = "..."
    ORG_IDS = ["..."]

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    latest_issues = get_latest_issues(client, org_ids=ORG_IDS)
    logging.debug(json.dumps(latest_issues, indent=2))


if __name__ == '__main__':
    main()
