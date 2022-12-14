import httpx
import json
import logging

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


def get_org_dependencies(client: httpx.Client, org_id: str) -> httpx.Response:
    """Get the dependencies of an org."""

    # this filter allows you to narrow the results to the results
    # within one project. Makes it easier for you to identify what
    # you are looking for from reporting.
    filters = {
        "filters": {
            "languages": ["golang"],
            "projects": ["2a4e0cae-70f5-4f66-8624-c99d4f79c2cd"],
            "severity": ["medium", "high"]
        }
    }
    response = client.post(f"/org/{org_id}/dependencies", data=json.dumps(filters))
    return response.json()


def main():
    """Main function. """
    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    org_dependencies = get_org_dependencies(client, org_id=ORG_ID)
    print(json.dumps(org_dependencies, indent=2))


if __name__ == '__main__':
    main()
