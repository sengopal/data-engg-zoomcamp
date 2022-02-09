### Homework 3

-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `fluent-tea-338517.camp_ny_taxi.external_yellow_taxi`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://dtc_data_lake_fluent-tea-338517/raw/yellow_taxi_2019_*.parquet', 'gs://dtc_data_lake_fluent-tea-338517/raw/yellow_taxi_2020_*.parquet']
);

-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `fluent-tea-338517.camp_ny_taxi.external_fhv_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://dtc_data_lake_fluent-tea-338517/raw/fhv_tripdata_2019_*.parquet', 'gs://dtc_data_lake_fluent-tea-338517/raw/fhv_tripdata_2020_*.parquet']
);

-- filter by dropoff_datetime and order by dispatching_base_num *


-- Creating a partition and cluster table
CREATE OR REPLACE TABLE fluent-tea-338517.camp_ny_taxi.fhv_tripdata
PARTITION BY DATE(dropoff_datetime)
CLUSTER BY dispatching_base_num AS
SELECT * FROM fluent-tea-338517.camp_ny_taxi.external_fhv_tripdata;

-- count for fhv vehicles data for year 2019
select count(*) from fluent-tea-338517.camp_ny_taxi.fhv_tripdata where EXTRACT(YEAR from pickup_datetime)=2019;

-- distinct dispatching_base_num we have in fhv for 2019
select count(distinct dispatching_base_num) from fluent-tea-338517.camp_ny_taxi.fhv_tripdata where EXTRACT(YEAR from pickup_datetime)=2019;

-- count, estimated and actual data processed for query which counts trip between 2019/01/01 and 2019/03/31 for dispatching_base_num B00987, B02060, B02279 *
select count(*) from fluent-tea-338517.camp_ny_taxi.fhv_tripdata where DATE(dropoff_datetime) between date(timestamp('2019-01-01 00:00:00 UTC')) and date(timestamp('2019-03-30 23:59:59 UTC')) and dispatching_base_num in ('B00987', 'B02060', 'B02279')

