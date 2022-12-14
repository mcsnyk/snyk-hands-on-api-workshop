import httpx
import json
import logging

logging.basicConfig(level=logging.INFO)


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


def moving_orgs(client: httpx.Client, org_id: str, proj_id: str) -> httpx.Response:
    """Moving orgs"""

    #example:
    moving_data = {
        "originOrg": "b7a341bb-e4f8-4dbd-940c-e4ad79e5f015",
        "movedProject": "db29d53e-a130-475c-9353-6268a226354e",
        "targetOrgId": "b6553a7e-9051-43aa-8bf7-3437e1918e04"
    }

    response = client.put(f"/org/{org_id}/project/{proj_id}/move", data=json.dumps(moving_data))
    return response.json()


def updating_projects(client: httpx.Client, org_id: str, proj_id: str) -> httpx.Response:
    """Updating projects"""

    update_data = {
        "testFrequency": "daily"
    }

    update_data2 = {'id': '2a4e0cae-70f5-4f66-8624-c99d4f79c2cd', 'name': 'fiber5/fiber:go.mod', 'created': '2022-08-18T15:49:27.167Z',
     'origin': 'gitlab', 'type': 'gomodules', 'readOnly': False, 'testFrequency': 'weekly', 'totalDependencies': 18,
     'issueCountsBySeverity': {'low': 0, 'high': 1, 'medium': 3, 'critical': 0}, 'imageTag': '0.0.0',
     'lastTestedDate': '2022-08-18T15:49:27.524Z',
     'browseUrl': 'https://app.snyk.io/org/fiber5/project/2a4e0cae-70f5-4f66-8624-c99d4f79c2cd',
     'importingUser': {'id': '400e8955-44f8-4db5-8d6c-09819cd67722', 'name': 'gitlab', 'username': 'gitlab',
                       'email': None}, 'owner': None, 'tags': [], 'isMonitored': True,
     'attributes': {'criticality': [], 'lifecycle': [], 'environment': []}, 'branch': 'master'}

    response = client.put(f"/org/{org_id}/project/{proj_id}", data=json.dumps(update_data))
    return response.json()


def list_projects(client: httpx.Client, org_id: str) -> httpx.Response:
    """Listing projects"""

    filters = {
        "filters": {
            "type": "helmconfig",
            "type": "k8sconfig",
        }
    }

    response = client.post(f"/org/{org_id}/projects", data=json.dumps(filters))
    return response.json()


def main():
    """Main function"""
    #SNYK_TOKEN = "76473652-3695-4d8e-a0d3-86364949e890"
    #PROJECT_ID = "db29d53e-a130-475c-9353-6268a226354e"   # terraform from mcsnyk
    #ORIGIN_ORG = "b7a341bb-e4f8-4dbd-940c-e4ad79e5f015"

    #fiber
    #SNYK_TOKEN = "d0f16833-6f60-49b9-bf94-8aa5615591ea"
    SNYK_TOKEN = "fea30ee7-0dc5-4836-9dd7-4f951035ad52"
    ORIGIN_ORG1 = "7ea19655-a1de-437a-8f92-54dd2d2d55ff"
    PROJECT_ID1 = "2a4e0cae-70f5-4f66-8624-c99d4f79c2cd"
    fiber_orgid = "7ea19655-a1de-437a-8f92-54dd2d2d55ff"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    #moving_org = moving_orgs(client, org_id=ORIGIN_ORG, proj_id=PROJECT_ID)
    #print(moving_org)

    #up = updating_projects(client, org_id=ORIGIN_ORG1, proj_id=PROJECT_ID1)
    #print(up)

    lp = list_projects(client, org_id=fiber_orgid)
    print(lp)


if __name__ == '__main__':
    main()
