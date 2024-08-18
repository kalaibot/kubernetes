import os
import pytest
from unittest.mock import patch

# Fixture to patch the os.getenv function
@pytest.fixture
def mock_getenv():
    with patch('os.getenv') as mock:
        yield mock

# Parametrize the test to run with different URLs and expected results
@pytest.mark.parametrize("url, expected", [
    ('https://sandbox.github.com/repo.git', 'sandbox'),
    ('https://localhost/repo.git', 'local'),
    ('https://staging.github.com/repo.git', 'staging'),
    ('https://github.com/repo.git', 'production'),
])
def test_get_env(mock_getenv, url, expected):
    # Set the return value for os.getenv to the parameterized URL
    mock_getenv.return_value = url
    
    # Import the function and run the test
    from main import get_env
    assert get_env() == expected
