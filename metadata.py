import logging
import pandas as pd
from sqlalchemy import text
from config import engine
from decorators.timer import timer_decorator

logger = logging.getLogger(__name__)


@timer_decorator
def get_last_run_time():
    query = text("""
        SELECT last_run
        FROM metadata_pipeline
        WHERE pipeline_name = 'repo_pipeline'
    """)

    df = pd.read_sql(query, engine)

    if df.empty:
        return None

    last_run = df['last_run'].iloc[0]

    return last_run


def updated_last_run_time(max_update_run):
    query = text("""
        UPDATE metadata_pipeline
        SET last_run = NOW()
        WHERE pipeline_name = 'repo_pipeline'
    """)

    with engine.begin() as connection:
        connection.execute(query)

    logger.info("Last run time updated successfully")