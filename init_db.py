from sqlalchemy import text
from config import engine

def create_tables():
    with engine.begin() as conn:
        print("Creating table: metadata_pipeline")
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS metadata_pipeline (
                pipeline_name VARCHAR(255) PRIMARY KEY,
                last_run TIMESTAMP WITH TIME ZONE
            );
        """))
        print("Creating table: github_repositories")
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS github_repositories (
                repo_id BIGINT PRIMARY KEY,
                repo_name VARCHAR(255),
                owner_login VARCHAR(255),
                language VARCHAR(255),
                stargazers_count INT,
                forks_count INT,
                created_at TIMESTAMP WITH TIME ZONE,
                updated_at TIMESTAMP WITH TIME ZONE,
                pushed_at TIMESTAMP WITH TIME ZONE,
                organization_login VARCHAR(255)
            );
        """))
        
        print("Inserting initial record into metadata_pipeline")
        conn.execute(text("""
            INSERT INTO metadata_pipeline (pipeline_name, last_run)
            VALUES ('repo_pipeline', NULL)
            ON CONFLICT (pipeline_name) DO NOTHING;
        """))
    print("Database initialized successfully.")

if __name__ == "__main__":
    create_tables()
