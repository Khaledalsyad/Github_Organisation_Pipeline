import pandas as pd
from typing import Generator


def transform_data(raw_data: Generator) -> pd.DataFrame:
    """
    Transform raw data from GitHub API into a clean DataFrame
    """
    records = []

    for organization, repos in raw_data:
        for repo in repos:
            records.append({
                'repo_id': repo.get('id'),
                'repo_name': repo.get('name'),
                'owner_login': repo.get('owner', {}).get('login'),
                'language': repo.get('language'),
                'stargazers_count': repo.get('stargazers_count', 0),
                'forks_count': repo.get('forks_count', 0),
                'created_at': repo.get('created_at'),
                'updated_at': repo.get('updated_at'),
                'pushed_at': repo.get('pushed_at'),
                'organization_login': organization,
            })

    df = pd.DataFrame(records)

    # convert datetime columns
    for col in ['created_at', 'updated_at', 'pushed_at']:
        df[col] = pd.to_datetime(df[col], utc=True)

    return df


def incremental_filter(df: pd.DataFrame, last_run_time) -> pd.DataFrame:
    """
    Filter rows that were updated after the last pipeline run
    """
    if last_run_time is None:
        return df

    filters = df[df['updated_at'] > pd.to_datetime(last_run_time, utc=True)]
    
    print(f"Number of rows after incremental filter: {len(filters)}")
    
    return filters