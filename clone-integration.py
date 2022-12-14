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


def clone_integration(client: httpx.Client, org_id: str, integration_id: str) -> httpx.Response:
    """Clone an existing integration."""
    filters = {
        "destinationOrgPublicId": "f37316c4-a21b-4dfc-989f-677f35f0bf88"
    }

    response = client.post(f"/org/{org_id}/integrations/{integration_id}/clone", data=json.dumps(filters))
    return response.json()


def main():
    """Main function. """
    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"
    integration_id = "<integration ID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    org_dependencies = clone_integration(client, org_id=ORG_ID, integration_id=integration_id)
    print(json.dumps(org_dependencies, indent=2))


if __name__ == '__main__':
    main()
