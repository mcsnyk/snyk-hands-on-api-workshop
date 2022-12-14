import httpx
import json
import logging

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


def view_org_dependencies(client: httpx.Client, org_id: str) -> httpx.Response:
    """Get the dependencies of an org."""

    response = client.get(f"/org/{org_id}/settings")
    return response.json()


def main():
    """Main function. """
    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    org_dependencies = view_org_dependencies(client, org_id=ORG_ID)
    print(json.dumps(org_dependencies, indent=2))


if __name__ == '__main__':
    main()
