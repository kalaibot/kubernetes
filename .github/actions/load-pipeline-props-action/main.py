git_url = os.getenv('GITHUB_SERVER_URL')
def get_env():
    """
    Get the environment based on the git URL.

    Returns:
        str: The environment name.
    """
    if 'sandbox' in git_url:
        return 'sandbox'
    elif 'localhost' in git_url:
        return 'local'
    elif 'staging' in git_url:
        return 'staging'
    else:
        return 'production'
