"""Tests for the login endpoint."""

import pytest

def test_login_returns_ok(client):
    """The login endpoint returns a successful JSON response."""
    response = client.post(
        "/api/login/", json={"email": "morpheus@matrix.com", "pwd": "1234"}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert set(response.json()) == {"ok"}
    assert isinstance(response.json()["ok"], bool)
    assert response.json()["ok"]


@pytest.mark.parametrize(
    ("credentials", "missing_fields"),
    [
        ({"email": "user@example.com"}, {"pwd"}),
        ({"pwd": "test-password"}, {"email"}),
        ({}, {"email", "pwd"}),
    ],
)
def test_login_requires_credentials(client, credentials, missing_fields):
    """The login endpoint requires both credentials in the JSON body."""
    response = client.post("/api/login/", json=credentials)

    assert response.status_code == 422
    assert {tuple(error["loc"]) for error in response.json()["detail"]} == {
        ("body", field) for field in missing_fields
    }


def test_login_rejects_invalid_credentials(client):
    response = client.post(
        "/api/login/", json={"email": "user@example.com", "pwd": "wrong"}
    )
    assert response.status_code == 401


def test_login_rejects_query_only_credentials(client):
    response = client.post(
        "/api/login/", params={"email": "morpheus@matrix.com", "pwd": "1234"}
    )
    assert response.status_code == 422


def test_login_rejects_get(client):
    response = client.get("/api/login/")
    assert response.status_code == 405
