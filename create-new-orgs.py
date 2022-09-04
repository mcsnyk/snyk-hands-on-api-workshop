import httpx
import json
import logging

# Log-level can be eg. "INFO", "DEBUG", "CRITICAL", "ERROR", "FATAL"...
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


def create_new_org(client: httpx.Client, group_id: str, new_project_name: str, source_org_settings: str = "") -> httpx.Response:
    """Creating a new org"""

    create_new_org_data = {
        "name": new_project_name,
        "groupId": group_id
        #,"sourceOrgId": source_org_settings
    }

    response = client.post(f"/org", data=json.dumps(create_new_org_data))
    return response.json()


def main():
    """Main function"""
    
    SNYK_TOKEN = "your-snyk-group-level-token-in-the-webui"
    GROUP_ID = "your-snyk-groupid-in-the-webui"
    NEW_PROJECT_NAME = "your-new-organisation-name"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    new_org = create_new_org(client, group_id=GROUP_ID, new_project_name=NEW_PROJECT_NAME)
    logging.debug(json.dumps(new_org, indent=2))
    print(new_org)


if __name__ == '__main__':
    main()
   
