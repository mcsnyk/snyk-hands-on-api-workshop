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


def moving_orgs(client: httpx.Client, org_id: str, proj_id: str, target_org_id: str) -> httpx.Response:
    """Moving a project to a different org."""

    moving_org_data = {

        "targetOrgId": target_org_id
    }

    response = client.put(f"/org/{org_id}/project/{proj_id}/move", data=json.dumps(moving_org_data))
    return response.json()


def main():
    """Main function"""
    
    SNYK_TOKEN = "..."
    PROJECT_ID = "..."
    ORIGIN_ORG_ID = "..."
    TARGET_ORG_ID = "..."
    
    # create a client:
    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)
    
    # moving project from one org into another
    moving_org = moving_orgs(client, org_id=ORIGIN_ORG_ID, proj_id=PROJECT_ID, target_org_id=TARGET_ORG_ID)
    logging.debug(json.dumps(moving_org, indent=2))


if __name__ == '__main__':
    main()
   
