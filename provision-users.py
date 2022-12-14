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


def provision_users(client: httpx.Client, org_id: str) -> httpx.Response:
    """Creating a new org"""

    data = {
        "email": "<employee email >",
        "rolePublicId": "<role public ID>",

    }

    response = client.post(f"/org/{org_id}/provision", data=json.dumps(data))
    return response.json()


def main():
    """Main function"""
    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    prov_user = provision_users(client, org_id=ORG_ID)
    logging.debug(json.dumps(prov_user, indent=2))


if __name__ == '__main__':
    main()
