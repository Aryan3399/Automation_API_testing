# Automation_API_testing

# 🧪 API Testing with Python & Pytest

This is a simple project to test **CRUD operations** (Create, Read, Update, Delete) on a fake REST API using `requests` and `pytest`.

---

## 🔗 API Used

- [FakeRestAPI](https://fakerestapi.azurewebsites.net/api/v1/Activities)

---

## 📂 File

- `test_user_crud.py` – contains all test functions:
  - `test_create_user()`
  - `test_get_user()`
  - `test_update_user()`
  - `test_delete_user()`

---

## ✅ Features Tested

| Method | Action   | Function             | Description                          |
|--------|----------|----------------------|--------------------------------------|
| POST   | Create   | `test_create_user()` | Creates a new fake user              |
| GET    | Read     | `test_get_user()`    | Fetches list of all users            |
| PUT    | Update   | `test_update_user()` | Updates the created fake user        |
| DELETE | Delete   | `test_delete_user()` | Deletes the user by ID               |


## 🚀 How to Run

```bash
pip install requests pytest
pytest -v test_all.py

# Optional (prettier output):
pip install pytest-sugar

✅ Sample Output
test_all.py::test_create_user ✓
test_all.py::test_get_user ✓
test_all.py::test_update_user ✓
test_all.py::test_delete_user ✓

📌 Author
--ARYAN  -learning API automation with Python.
