# data-engg-zoomcamp
Work done as part of the data engineering zoomcamp conducted by datatalks.club

## Leaderboard
[Certificate](https://certificate.datatalks.club/dezoomcamp/2022/bed393da5e7da394409bca0aaee25f02bc886179.pdf)

![DE-zoomcamp-leaderboard-Apr2022](https://user-images.githubusercontent.com/787381/170883195-1570a58b-9740-4e50-9689-2884c34f7d0b.png)

![Screen Shot 2022-05-29 at 10 21 22 AM](https://user-images.githubusercontent.com/787381/170883243-aab85457-6bcb-497b-94ed-e9f051a66b35.png)



### Table creation queries
```sql
CREATE OR REPLACE TABLE trips_data_all.green_tripdata PARTITION BY DATE(lpep_pickup_datetime) AS 
    SELECT * EXCEPT (ehail_fee), cast(0 as NUMERIC) ehail_fee FROM trips_data_all.green_tripdata_external_table;

CREATE OR REPLACE TABLE trips_data_all.yellow_tripdata PARTITION BY DATE(tpep_pickup_datetime) AS 
    SELECT * FROM trips_data_all.yellow_tripdata_external_table;

CREATE OR REPLACE TABLE trips_data_all.fhv_tripdata PARTITION BY DATE(pickup_datetime) AS 
    SELECT * FROM trips_data_all.fhv_tripdata_external_table;

```
