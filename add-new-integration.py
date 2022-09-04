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


def add_new_integration(client: httpx.Client, org_id: str, integr_type: str,  integr_token: str, url: str) -> httpx.Response:
    """Adding a new integration to an existing org"""

    new_integration_data = {
        "type": integr_type,
        "credentials": {
            "token": integr_token,
            "url": url
        }
    }

    response = client.post(f"/org/{org_id}/integrations", data=json.dumps(new_integration_data))
    return response.json()


def main():
    """Main function. """
    SNYK_TOKEN = "..."
    ORG_ID = "..."
    INTEGR_TYPE = "gitlab"
    INTEGR_TOKEN = "..."
    URL = "https://gitlab.com"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    integration = add_new_integration(client, org_id=ORG_ID, integr_type=INTEGR_TYPE, integr_token=INTEGR_TOKEN, url=URL)
    print(integration)


if __name__ == '__main__':
    main()

