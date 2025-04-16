CREATE DATABASE IF NOT EXISTS single_test;
CREATE TABLE IF NOT EXISTS single_test.test_table
(
    `my_date` DateTime DEFAULT NOW(),
    `timestamp` DateTime,
    `applicationId` Int64,
    `date` Date,
    `my_interval` Int64,
    `count` Int64
)
ENGINE = MergeTree()
ORDER BY timestamp
PARTITION BY toYYYYMMDD(timestamp)
TTL my_date + INTERVAL 12 HOUR;
