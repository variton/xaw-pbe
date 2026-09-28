"""Tests for the heartbeat endpoint."""

import pytest

from conftest import client

from xawpbe import app 


def test_hbeat_returns_ok(client):
    """The heartbeat endpoint returns a successful JSON response."""
    response = client.get("/api/hbeat")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"hbeat": "ok"}
