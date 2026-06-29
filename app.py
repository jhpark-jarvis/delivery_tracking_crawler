from __future__ import annotations

import logging
import schedule
import time

from config import validate_settings
from services.tracking_service import DeliveryTrackingService

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    validate_settings()
    service = DeliveryTrackingService()
    schedule.every(10).seconds.do(service.run)
    logger.info("Delivery tracking scheduled every 10 seconds")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
