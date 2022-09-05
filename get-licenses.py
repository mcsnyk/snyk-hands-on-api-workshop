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

    SNYK_TOKEN = "..."
    ORG_ID = "..."

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    licenses = get_licenses(client, org_id=ORG_ID)

    # List all used Open Source licences:
    print("--" * 16, "\n All used Open Source licences:", "\n", "--"*16)
    for license in licenses["results"]:
        print(json.dumps(license.get("id"), indent=2))


    # Multiple licences:
    chosen_double_license = "BSD-3-Clause OR MIT"

    print("--" * 16, "\n Problems with multiple licences Open Source licences:", "\n", "--" * 16)
    for license in licenses["results"]:
        if license["id"] == chosen_double_license:
            logging.debug(json.dumps(license, indent=2))


if __name__ == '__main__':
    main()
