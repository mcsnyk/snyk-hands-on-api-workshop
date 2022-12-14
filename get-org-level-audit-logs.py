import httpx
import json
import logging

logging.basicConfig(level=logging.DEBUG)


def create_client(base_url: str, token: str) -> httpx.Client:
    """Create a client."""
    limits = httpx.Limits(max_keepalive_connections=10, max_connections=20)

    client = httpx.Client(
        base_url=base_url,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"token {token}",
        },
        timeout=500,
        limits=limits,
    )
    return client


def get_audit(client: httpx.Client, org_id: str) -> httpx.Response:
    """Get audit logs of your organization."""

    audit_data_filter = {
        "filters": {
            "event": "org.project.monitor"
        }
    }

    response = client.post(f"/org/{org_id}/audit?from=2022-12-10&to=2022-12-14&page=1&sortOrder=ASC", data=json.dumps(audit_data_filter))
    return response.json()


def main():
    """Main function. """
    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    it = get_audit(client, org_id=ORG_ID)
    logging.debug(json.dumps(it, indent=2))


if __name__ == '__main__':
    main()
