import httpx
import json
import logging

"""
run: pip3 install -r requirements.txt
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


def create_client_v3(base_url: str, token: str) -> httpx.Client:
    """Create a client v3."""
    client_v3 = httpx.Client(
        base_url=base_url,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/vnd.api+json",
            "Authorization": f"Token {token}",
        },
    )
    return client_v3


def get_all_projects(client: httpx.Client, org_id: str) -> httpx.Response:
    """Get all projects of an org."""

    filter_no = {
    }

    response = client.post(f"/org/{org_id}/projects", data=json.dumps(filter_no))
    return response.json()


def get_code_issues_v3(client: httpx.Client, org_id: str, proj_id: str) -> httpx.Response:
    """Get code issues for Code."""

    response = client.get(f"/orgs/{org_id}/issues?project_id={proj_id}&type=code&version=2022-04-06%7Eexperimental")
    return response.json()


def main():
    """Main function"""
    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    all_projects = get_all_projects(client, org_id=ORG_ID)
    #logging.debug(json.dumps(all_projects, indent=2))

    list_of_ids = []
    it3 = []

    for pr in all_projects["projects"]:
        list_of_ids.append(json.dumps(pr.get("id")).strip())
        #print(json.dumps(pr.get("id"), indent=2))

    client3 = create_client_v3(base_url="https://api.snyk.io/rest/", token=SNYK_TOKEN)

    # list all code issues:
    for i in range(len(list_of_ids)):
        it3.append(get_code_issues_v3(client3, org_id=ORG_ID, proj_id=f"{list_of_ids[i][1:37]}"))
        #logging.debug(json.dumps(it3, indent=2))

    # All projects that we find in an org:
    #print(len(it3))
    #logging.debug(json.dumps(it3, indent=2))

    for iii in range(len(it3)):
        #Let's consider only the code issues:
        a = it3[iii]["data"]
        print(a)
        if len(a) != 0:
            for j in range(len(a)):
                #print(a[j]["attributes"]["cwe"])
                if "1330" in str(a[j]["attributes"]["cwe"]) or "532" in str(a[j]["attributes"]["cwe"]):
                    logging.debug(json.dumps(a[j], indent=2))


if __name__ == '__main__':
    main()
