from __future__ import annotations

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"


def _load_env_file(path: Path = ENV_PATH) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_env_file()

DB_HOST = os.getenv("DELIVERY_DB_HOST", "192.168.1.158")
DB_PORT = int(os.getenv("DELIVERY_DB_PORT", "3306"))
DB_USER = os.getenv("DELIVERY_DB_USER", "final")
DB_PASSWORD = os.getenv("DELIVERY_DB_PASSWORD", "tiger1234")
DB_NAME = os.getenv("DELIVERY_DB_NAME", "finalproject")
DB_CHARSET = os.getenv("DELIVERY_DB_CHARSET", "utf8")


def validate_settings() -> None:
    missing = []
    if not DB_HOST:
        missing.append("DELIVERY_DB_HOST")
    if not DB_USER:
        missing.append("DELIVERY_DB_USER")
    if not DB_PASSWORD:
        missing.append("DELIVERY_DB_PASSWORD")
    if not DB_NAME:
        missing.append("DELIVERY_DB_NAME")
    if missing:
        raise ValueError(f"Missing settings: {', '.join(missing)}")
