import requests
import pytest, os
from dotenv import load_dotenv

load_dotenv()

HOST="https://release-gs.qa-playground.com/api/v1"

@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response=requests.post(
        url=f"{HOST}/setup",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}",
"X-Task-Id": "API-1"}
    )
    assert response.status_code==205
