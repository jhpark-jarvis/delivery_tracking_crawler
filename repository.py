from __future__ import annotations

import pymysql

from config import DB_CHARSET, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


class DeliveryRepository:
    def connect(self):
        return pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            charset=DB_CHARSET,
        )

    def fetch_targets(self):
        sql = """SELECT T.trackingNum, T.idx
                 FROM T_order AS T
                 JOIN T_orderList AS TOL
                 ON T.idx = TOL.order_idx
                 WHERE TOL.orderState IN (3, 4)
                 AND T.cancelDT IS NULL
                 AND TOL.cancelCount IS NULL"""
        conn = self.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()

    def update_state(self, order_idx: int, state: int) -> None:
        conn = self.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE T_orderList
                    SET orderState = %s
                    WHERE order_idx = %s
                    """,
                    (state, order_idx),
                )
            conn.commit()
        finally:
            conn.close()
