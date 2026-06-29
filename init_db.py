from config import DB_CHARSET, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
import pymysql
from pathlib import Path


def main() -> None:
    schema_path = Path(__file__).with_name("schema.sql")
    schema_sql = schema_path.read_text(encoding="utf-8")
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset=DB_CHARSET,
    )
    try:
        with conn.cursor() as cur:
            for statement in [s.strip() for s in schema_sql.split(";") if s.strip()]:
                cur.execute(statement)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    main()

