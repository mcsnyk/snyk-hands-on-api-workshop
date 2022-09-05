import httpx
import json
import logging

"""
run: pip3 install -r requirements.txt
"""

# Here you can change the logging level:
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


def create_new_org(client: httpx.Client, group_id: str, new_project_name: str, source_org_settings: str = "") -> httpx.Response:
    """Creating a new organisation."""

    create_new_org_data = {
        "name": new_project_name,
        "groupId": group_id#,
        #"sourceOrgId": source_org_settings
    }

    response = client.post(f"/org", data=json.dumps(create_new_org_data))
    return response.json()


def get_all_orgs_in_a_group(client: httpx.Client, group_id: str) -> httpx.Response:
    """Listing all orgs in a Group."""

    response = client.get(f"/group/{group_id}/orgs")
    return response.json()


def list_existing_integrations(client: httpx.Client, org_id: str) -> httpx.Response:
    """List all existing integrations for an org."""

    response = client.get(f"/org/{org_id}/integrations")
    return response.json()


def add_new_integration(client: httpx.Client, org_id: str, integr_type: str,  integr_token: str, url: str) -> httpx.Response:
    """Adding a new integration to an existing org."""

    new_integration_data = {
        "type": integr_type,
        "credentials": {
            "token": integr_token,
            "url": url
        }
    }

    response = client.post(f"/org/{org_id}/integrations", data=json.dumps(new_integration_data))
    return response.json()


def get_org_dependencies(client: httpx.Client, org_id: str) -> httpx.Response:
    """Get the dependencies of an org."""

    # this filter allows you to narrow the results to the results
    # within one project. Makes it easier for you to identify what
    # you are looking for from reporting.
    filters = {
        "filters": {
            "languages": ["javascript", "terraform"],
            "projects": ["f5b58850-b885-4690-838c-5b1165f0b21e"],
            "severity": ["critical", "high"]
        }
    }
    response = client.post(f"/org/{org_id}/dependencies", data=json.dumps(filters))
    return response.json()


def get_licenses(client: httpx.Client, org_id: str) -> httpx.Response:
    """Get licenses."""

    # this filter allows you to narrow the results to the licenses
    # within one project. Makes it easier for you to identify what
    # you are looking for from reporting.

    filters = {
        "filters": {
            "projects": ["116ac265-a00c-43d1-8a9e-9f46964660e5"],
        }
    }
    response = client.post(f"/org/{org_id}/licenses", data=json.dumps(filters))
    return response.json()


def main():
    """Main function."""

    SNYK_TOKEN = "bf9b9173-fdf6-4d2a-b603-ebc6e6b0f341"
    GROUP_ID = "40efc063-b5d7-4f2c-932b-13f6f13f4bd9"
    NEW_PROJECT_NAME = "new-organisation-name"

    splinter_to_get_groups = "-08-"

    INTEGR_TYPE = "gitlab"
    INTEGR_TOKEN = "glpat-9YciuBMPA3sqSdfuzNRv"
    URL = "https://gitlab.com"

    ###creating a client:
    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    #####  Task 1  #####
    ### creating our new org:
    #new_org = create_new_org(client, group_id=GROUP_ID, new_project_name=NEW_PROJECT_NAME)

    ### print out the logs:
    #print("--" * 16, "\n Logging information:", "\n", "--" * 16)
    #logging.debug(json.dumps(new_org, indent=2))

    ### check the ID of the newly created org:
    #new_org_id = new_org.get('id')
    #print("New org ID: ", new_org_id)


    ##### Task 2 #####
    ###getting all details from all orgs in a Group
    #group_orgs_detailed = get_all_orgs_in_a_group(client, group_id=GROUP_ID)

    ### print out the logs:
    #print("--"*16, "\n Logging information about all the orgs in the Group:", "\n", "--"*16)
    #print(json.dumps(group_orgs_detailed, indent=2))

    ###Focus only on org-data, Group metadata is not interesting at this point:
    #group_orgs = group_orgs_detailed.get("orgs")

    ###Narrowing down the results:
    #print("--" * 16, "\n ID of the newly created org in the Group:", "\n", "--"*16)
    #for org in group_orgs:
    #    if splinter_to_get_groups in org["created"]:
    #        print(org["id"])

    ##### Task 3 #####
    ###List the existing integrations for an org:
    #list_integrations = list_existing_integrations(client, org_id=ORG_ID)
    #print(json.dumps(list_integrations, indent=2))

    ###Add a new integration to your newly created org:
    #new_integration = add_new_integration(client, org_id=new_org_id, integr_type=INTEGR_TYPE, integr_token=INTEGR_TOKEN, url=URL)
    #print(json.dumps(new_integration, indent=2))


    ##### Task 4 #####
    ###Dependencies of an organization
    ###Try to adjust the filter in the function get_org_dependencies
    #org_dependencies = get_org_dependencies(client, org_id=new_org_id)
    #print(json.dumps(org_dependencies, indent=2))


    ##### Task 5 #####
    ###List the used Open Source licences in a project of an organization
    #licenses = get_licenses(client, org_id=ORG_ID)

    ###List all used Open Source licences:
    #print("--" * 16, "\n All used Open Source licences:", "\n", "--"*16)
    #for license in licenses["results"]:
    #    print(json.dumps(license.get("id"), indent=2))


    ###Multiple licences:
    #chosen_double_license = "BSD-3-Clause OR MIT"

    #print("--" * 16, "\n Problems with multiple licences Open Source licences:", "\n", "--" * 16)
    #for license in licenses["results"]:
    #    if license["id"] == chosen_double_license:
    #        logging.debug(json.dumps(license, indent=2))


if __name__ == '__main__':
    main()
