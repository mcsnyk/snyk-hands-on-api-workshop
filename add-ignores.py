import httpx
import json
import logging

"""
run: pip3 install -r requirements.txt
"""

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


def add_ignores(client: httpx.Client, org_id: str, project_id: str, issue_id: str) -> httpx.Response:
    """Add new ignores."""

    ignores_data = {
        "reason": "Testing creating ignores via API v1",
        "reasonType": "temporary-ignore",
        "expires": "2022-12-28T22:45:00.260Z",
        "disregardIfFixable": False
    }

    response = client.post(f"/org/{org_id}/project/{project_id}/ignore/{issue_id}", data=json.dumps(ignores_data))
    return response.json()


def main():
    """Main function."""

    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"
    PROJECT_ID = "<desired projectID>"
    ISSUE_ID = "SNYK-PYTHON-JINJA2-1012994"

    client = create_client(base_url="https://app.snyk.io/api/v1/", token=SNYK_TOKEN)

    added_ignores = add_ignores(client, org_id=ORG_ID, project_id=PROJECT_ID, issue_id=ISSUE_ID)
    logging.debug(json.dumps(added_ignores, indent=2))


if __name__ == '__main__':
    main()
