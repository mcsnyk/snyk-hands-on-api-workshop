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
    
    SNYK_TOKEN = "..."
    GROUP_ID = "..."
    NEW_PROJECT_NAME = "..."
    
    # creating a client:
    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)
    
    # creating our new org:
    new_org = create_new_org(client, group_id=GROUP_ID, new_project_name=NEW_PROJECT_NAME)
    
    # print out the logs:
    print("--"*16, "\n Logging information:", "\n", "--"*16)
    logging.debug(json.dumps(new_org, indent=2))
    
    # check the ID of the newly created org:
    new_org_id = new_org.get('id')
    print("New org ID: ", new_org_id)


if __name__ == '__main__':
    main()
