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


def list_existing_integrations(client: httpx.Client, org_id: str) -> httpx.Response:
    """List all existing integrations for an org"""

    response = client.get(f"/org/{org_id}/integrations")
    return response.json()


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
    INTEGR_TYPE = "gitlab" #example
    INTEGR_TOKEN = "..." #if you don't want to bother (valid until 7th Sep., Gitlab:): glpat-Q6W69UPuVFhs4qzvJiiF
    URL = "https://gitlab.com" #example
    
    # creating a client:
    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)
    
    # list all the existing integrations for an org:
    list_integrations = list_existing_integrations(client, org_id=ORG_ID)
    print(json.dumps(list_integrations, indent=2))

    #new_integration = add_new_integration(client, org_id=ORG_ID, integr_type=INTEGR_TYPE, integr_token=INTEGR_TOKEN, url=URL)
    #print(json.dumps(new_integration, indent=2))


if __name__ == '__main__':
    main()

