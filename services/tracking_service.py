from __future__ import annotations

import logging
import time
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from repositories.delivery_repository import DeliveryRepository

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeliveryResult:
    tracking_num: str
    order_idx: int
    state: int


class DeliveryTrackingService:
    def __init__(self, repository: DeliveryRepository | None = None) -> None:
        self.repository = repository or DeliveryRepository()

    def run(self) -> list[DeliveryResult]:
        op = Options()
        op.add_argument("--headless")
        op.add_argument("--disable-gpu")

        driver = webdriver.Chrome(options=op)
        results: list[DeliveryResult] = []
        try:
            for tracking_num, order_idx in self.repository.fetch_targets():
                state = self._inspect_status(driver, tracking_num)
                if state is not None:
                    self.repository.update_state(order_idx, state)
                    results.append(DeliveryResult(tracking_num, order_idx, state))
            logger.info("Updated %s delivery rows", len(results))
            return results
        finally:
            driver.quit()

    def _inspect_status(self, driver, tracking_num: str) -> int | None:
        url = f"https://trace.cjlogistics.com/next/tracking.html?wblNo={tracking_num}"
        driver.get(url)
        time.sleep(3)

        tracking_status = [row.text for row in driver.find_elements(By.XPATH, '//*[@id="statusDetail"]/tr')]
        if not tracking_status:
            return None
        if "배송완료" in tracking_status[-1]:
            return 5
        return 4
