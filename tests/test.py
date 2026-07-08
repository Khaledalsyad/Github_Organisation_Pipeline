import pandas as pd
data = {
    "id": [1],
    "name": ["repo1"],
    "description": ["description1"],
    "full_name": ["user/repo1"],
    "private": [False],
    "visibility": ["public"],
    "fork": [False],
    "homepage": ["http://example.com"],
    "ssh_url": ["ssh://git@github.com/user/repo1.git"],
    "clone_url": ["https://github.com/user/repo1.git"],
    "html_url": ["https://github.com/user/repo1"],
    "language": ["Python"],
    "created_at": ["2023-01-01T12:00:00Z"],
    "updated_at": ["2024-01-01T12:00:00Z"],
    "topics": [["python", "django"]],
    "size": [1024],
    "stargazers_count": [100],
    "watchers_count": [200],
    "forks_count": [300],
    "open_issues_count": [400],
    "deleted": [False]
}

df = pd.DataFrame(data)
# assert df.shape ==(1, 21)

# assert df['id'].all() == 1
assert df['name'].iloc[0] =="repo1"
