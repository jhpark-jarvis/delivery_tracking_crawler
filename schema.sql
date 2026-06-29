CREATE TABLE IF NOT EXISTS T_order (
    idx INT PRIMARY KEY,
    trackingNum VARCHAR(64) NOT NULL,
    cancelDT DATETIME NULL
);

CREATE TABLE IF NOT EXISTS T_orderList (
    idx INT AUTO_INCREMENT PRIMARY KEY,
    order_idx INT NOT NULL,
    orderState INT NOT NULL,
    cancelCount INT NULL
);

