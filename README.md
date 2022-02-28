# data-engg-zoomcamp
Work done as part of the data engineering zoomcamp conducted by datatalks.club


### Table creation queries
```sql
CREATE OR REPLACE TABLE trips_data_all.green_tripdata PARTITION BY DATE(lpep_pickup_datetime) AS 
    SELECT * EXCEPT (ehail_fee), cast(0 as NUMERIC) ehail_fee FROM trips_data_all.green_tripdata_external_table;

CREATE OR REPLACE TABLE trips_data_all.yellow_tripdata PARTITION BY DATE(tpep_pickup_datetime) AS 
    SELECT * FROM trips_data_all.yellow_tripdata_external_table;

CREATE OR REPLACE TABLE trips_data_all.fhv_tripdata PARTITION BY DATE(pickup_datetime) AS 
    SELECT * FROM trips_data_all.fhv_tripdata_external_table;

```
