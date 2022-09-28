import httpx
import json
import logging

logging.basicConfig(level=logging.DEBUG)


def create_client(base_url: str, token: str) -> httpx.Client:
    """Create a client"""

    client = httpx.Client(
        base_url=base_url,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"token {token}",
        },
    )
    return client


def remove_org(client: httpx.Client, org_id: str = "") -> httpx.Response:
    """Removing an existing org"""

    response = client.delete(f"/org/{org_id}")
    return response.json()


def main():
    """Main function"""
    SNYK_TOKEN = "..."
    ORG_ID = "..."

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    removed_org = remove_org(client, org_id=ORG_ID)
    logging.debug(json.dumps(removed_org, indent=2))


if __name__ == '__main__':
    main()
