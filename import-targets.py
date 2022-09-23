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


def import_target(client: httpx.Client, org_id: str, integr_id: str) -> httpx.Response:
    """Importing targets."""

    # a trending javascript project at the moment
    values = {
        "target": {
            "owner": "zadam",
            "name": "trilium",
            "branch": "main"
        },
        "files": [
            {
                "path": "package.json"
            }
        ]
    }

    response = client.post(f"/org/{org_id}/integrations/{integr_id}/import", data=json.dumps(values))
    return response.json()


def main():
    """Main function."""

    SNYK_TOKEN = "..."  # Snyk personal API Token
    ORG_ID = "..."  # Snyk Org.ID
    INTEGR_ID = "..."  # Snyk integrationID with Github

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    it = import_target(client, org_id=ORG_ID, integr_id=INTEGR_ID)
    logging.debug(json.dumps(it, indent=2))


if __name__ == '__main__':
    main()
