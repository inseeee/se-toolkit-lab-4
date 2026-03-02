import os
import requests

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:42002")
API_TOKEN = os.getenv("API_TOKEN", "my-secret-api-key")

def test_get_interactions_returns_200():
    url = f"{API_BASE_URL}/interactions/"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_get_interactions_response_is_a_list():
    url = f"{API_BASE_URL}/interactions/"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    assert isinstance(data, list)
