# prepare
```bash
mkdir /tmp/click_data_tmp;
docker run -d --name click --rm -v /tmp/click_data_tmp:/var/lib/clickhouse/ clickhouse/clickhouse-server:24.8.14.39;
python generate_data.py;
for i in $(ls test_data* -1); do docker cp ./$i click:/tmp/; done;
docker exec -ti click bash;
```

## 1. Difference between column vs row-oriented database
https://clickhouse.com/docs/intro#row-oriented-vs-column-oriented-storage

## 2. Types of table engine
https://clickhouse.com/docs/ru/engines/table-engines  
2.1 MergeTree  
2.2 ReplacingMergeTree  
2.3 SummingMergeTree  
2.4 AggregatingMergeTree  
2.5 CollapsingMergeTree (VersionedCollapsingMergeTree)  
2.6 Distributed  
2.7 Log  
2.8 tinyLog  
2.9 stripeLog  
2.10 Dictionaries  
2.11 Integrations (PostgreSQL,Mysql,Redis,Kafka,Rabbit, etc....)  

## 3. General *MergeTree table settings
```sh
# insert migrations.sql to click with clickhosue-client -mn, then exit
cat /tmp/test_data1.csv | clickhouse-client --query="INSERT INTO single_test.test_table format CSV"
```
```sql
\l
USE single_test (or \c single_test)
\d (OR SHOW TABLES)
SELECT * FROM test_table limit 30;
```
3.1 PARTITION BY  
```sql
SELECT partition,name,active FROM system.parts where table= 'test_table'
```
3.2 ORDER BY(PRIMARY KEY)  
```sql
EXPLAIN indexes=1 SELECT * FROM single_test.test_table WHERE  timestamp >=NOW('Europe/Moscow') and timestamp < NOW('Europe/Moscow')+toIntervalMinute(120);
```
3.3 TTL  
DELETE - delete expired rows (default action);
RECOMPRESS codec_name - recompress data part with the codec_name;
TO DISK 'aaa' - move part to the disk aaa;
TO VOLUME 'bbb' - move part to the disk bbb;

```sql
ALTER TABLE single_test.test_table MODIFY TTL my_date + INTERVAL 1 HOUR;
```
3.4 How click stored data in disk?  
```sql
SELECT partition,name,active FROM system.parts where table= 'test_table' limit 10 format Vertical;
```
3.5 Delete specific partitions  
```sql
SELECT 'ALTER TABLE single_test.test_table DETACH PARTITION '||partition||';' FROM system.parts where table= 'test_table' and  partition < '20250502' format TSVRaw;
```
## 4. How to read logs?
