import pytest


@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
   assert True


@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
   assert False


@pytest.mark.api
@pytest.mark.event
def test_event_api():
   assert True


@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
   assert True
