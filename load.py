import pandas as pd
import logging
from sqlalchemy import text
from config import engine
from decorators.timer import timer_decorator
from decorators.logger import logger_decorator
from decorators.retry import retry

logger = logging.getLogger(__name__)


@timer_decorator
@logger_decorator
@retry(retries=3)
def loading_data(df: pd.DataFrame) -> None:
    try:
        with engine.begin() as connection:
            data_list = df.to_dict(orient='records')

            query = text("""
                INSERT INTO github_repositories(
                    repo_id,
                    repo_name,
                    owner_login,
                    language,
                    stargazers_count,
                    forks_count,
                    created_at,
                    updated_at,
                    pushed_at,
                    organization_login
                )
                VALUES (:repo_id, :repo_name, :owner_login, :language, :stargazers_count, :forks_count, :created_at, :updated_at, :pushed_at, :organization_login)
                ON CONFLICT(repo_id)
                DO NOTHING
            """)

            connection.execute(query, data_list)


        logger.info(f"All data loaded successfully — rows inserted: {len(data_list)}")

    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

    return {
        "status": "SUCCES",
        "loaded_rows": len(data_list)
    }