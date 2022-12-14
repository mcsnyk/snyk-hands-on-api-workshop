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


def list_all_ignores(client: httpx.Client, org_id: str, project_id: str) -> httpx.Response:
    """List all ignores."""

    response = client.get(f"/org/{org_id}/project/{project_id}/ignores")
    return response.json()


def main():
    """Main function."""

    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"
    PROJECT_ID = "<desired projectID>"

    client = create_client(base_url="https://app.snyk.io/api/v1/", token=SNYK_TOKEN)

    ignores = list_all_ignores(client, org_id=ORG_ID, project_id=PROJECT_ID)
    logging.debug(json.dumps(ignores, indent=2))


if __name__ == '__main__':
    main()
