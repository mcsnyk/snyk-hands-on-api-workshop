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


def pr_enable_disable(client: httpx.Client, org_id: str, project_id: str) -> httpx.Response:
    """Enable and disable PRs for projects."""

    data_disable = {
        "pullRequestInheritance": "custom",
        "pullRequestTestEnabled": False
    }

    # data_enable = {
    #     "pullRequestInheritance": "integration"
    # }

    response = client.put(f"/org/{org_id}/project/{project_id}/settings", data=json.dumps(data_disable))
    return response.json()


def main():
    """Main function."""

    SNYK_TOKEN = "...."

    # orgID where the project is:
    ORGANISATION_ID = "...."
    PROJECT_ID = "...."

    # create a client:
    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    # Enable or disable PR-s for a given project:
    pr_en = pr_enable_disable(client, org_id=ORGANISATION_ID, project_id=PROJECT_ID)
    logging.debug(json.dumps(pr_en, indent=2))


if __name__ == '__main__':
    main()
