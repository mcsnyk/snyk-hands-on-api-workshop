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


def get_all_orgs_in_a_group(client: httpx.Client, group_id: str) -> httpx.Response:
    """Listing all orgs in a Group"""

    response = client.get(f"/group/{group_id}/orgs")
    return response.json()


def main():
    """Main function"""
    SNYK_TOKEN = "bf9b9173-fdf6-4d2a-b603-ebc6e6b0f341"
    GROUP_ID = "40efc063-b5d7-4f2c-932b-13f6f13f4bd9"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    group_orgs_detailed = get_all_orgs_in_a_group(client, group_id=GROUP_ID)

    print("--"*16, "\n Logging information about all the orgs in the Group:", "\n", "--"*16)
    print(json.dumps(group_orgs_detailed, indent=2))

    group_orgs = group_orgs_detailed.get("orgs")

    # Narrowing down the results:
    print("--" * 16, "\n ID of the newly created org in the Group:", "\n", "--"*16)
    for org in group_orgs:
        if "........" in org["name"]:
            print(org["id"])


if __name__ == '__main__':
    main()
