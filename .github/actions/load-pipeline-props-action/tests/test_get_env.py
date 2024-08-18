import os
import pytest
#from unittest.mock import patch

# Fixture to mock the GITHUB_SERVER_URL environment variable
@pytest.fixture
def mock_git_url(monkeypatch):
    def _mock_git_url(url):
        monkeypatch.setenv('GITHUB_SERVER_URL', url)
    return _mock_git_url

def test_get_env_sandbox(mock_git_url):
    mock_git_url('https://sandbox.github.com/repo.git')
    from main import get_env
    assert get_env() == 'sandbox'

def test_get_env_local(mock_git_url):
    mock_git_url('https://localhost/repo.git')
    from main import get_env
    assert get_env() == 'local'

def test_get_env_staging(mock_git_url):
    mock_git_url('https://staging.github.com/repo.git')
    from main import get_env
    assert get_env() == 'staging'

def test_get_env_production(mock_git_url):
    mock_git_url('https://github.com/repo.git')
    from main import get_env
    assert get_env() == 'production'


# # Fixture to patch the os.getenv function
# @pytest.fixture
# def mock_getenv():
#     with patch('os.getenv') as mock:
#         yield mock

# # Parametrize the test to run with different URLs and expected results
# @pytest.mark.parametrize("url, expected", [
#     ('https://sandbox.github.com/repo.git', 'sandbox'),
#     ('https://localhost/repo.git', 'local'),
#     ('https://staging.github.com/repo.git', 'staging'),
#     ('https://github.com/repo.git', 'production'),
# ])
# def test_get_env(mock_getenv, url, expected):
#     # Set the return value for os.getenv to the parameterized URL
#     mock_getenv.return_value = url
    
#     # Import the function and run the test
#     from main import get_env
#     assert get_env() == expected
