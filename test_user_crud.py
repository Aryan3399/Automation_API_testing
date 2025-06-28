import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
TEST_USER_ID = 999

create_payload = {
    "id": TEST_USER_ID,
    "title": "Test CREATE user",
    "dueDate": "2025-06-28T06:01:34.423Z",
    "completed": True
}

update_payload = {
    "id": TEST_USER_ID,
    "title": "Test UPDATE user",
    "dueDate": "2025-06-28T06:01:34.423Z",
    "completed": False
}

def test_create_user():
    response = requests.post(BASE_URL, json=create_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == TEST_USER_ID
    assert data["title"] == create_payload["title"]
    assert data["completed"] is True
    print("CREATED:", data)

def test_get_user():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    print("Total records fetched:", len(data))

def test_update_user():
    response = requests.put(f"{BASE_URL}/{TEST_USER_ID}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_payload["title"]
    assert data["completed"] is False
    print("UPDATED:", data)

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/{TEST_USER_ID}")
    assert response.status_code == 200
    print(f"Deleted user with ID {TEST_USER_ID}")
