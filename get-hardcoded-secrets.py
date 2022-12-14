import httpx
import json
import logging

logging.basicConfig(level=logging.DEBUG)


def create_client(base_url: str, token: str) -> httpx.Client:
    """Create a client"""
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


def get_hardcoded(client: httpx.Client, org_id: str) -> httpx.Response:
    """Getting hardcoded secrets."""

    get_hardcoded_sec = {
        "filters": {
            "orgs": [
                org_id,
            ],
            "identifier": "CWE-798",
            "ignored": False
        }
    }

    response = client.post(f"/reporting/issues?from=2022-10-01&to=2022-10-17&page=1&perPage=100&sortBy=issueTitle&order=asc&groupBy=issue", data=json.dumps(get_hardcoded_sec))
    return response.json()


def main():
    """Main function. """
    SNYK_TOKEN = "<your token>"
    ORG_ID = "<desired orgID>"

    client = create_client(base_url="https://api.snyk.io/api/v1", token=SNYK_TOKEN)

    it = get_hardcoded(client, org_id=ORG_ID)
    logging.debug(json.dumps(it, indent=2))

if __name__ == '__main__':
    main()
