import httpx
import json
import logging

"""
pip3 freeze > requirements.txt
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


def delete_a_project(client: httpx.Client, org_id: str, proj_id: str) -> httpx.Response:
    """Delete a project from an org."""

    response = client.delete(f"/org/{org_id}/project/{proj_id}")
    return response.json()


def main():
    """Main function"""
    SNYK_TOKEN = "<your token>"
    PROJECT_ID = "<project ID>"
    ORIGIN_ORG_ID = "<origin org ID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    moving_org = delete_a_project(client, org_id=ORIGIN_ORG_ID, proj_id=PROJECT_ID)
    logging.debug(json.dumps(moving_org, indent=2))


if __name__ == '__main__':
    main()
