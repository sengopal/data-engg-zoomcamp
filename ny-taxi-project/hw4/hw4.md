### Question 1
count of records in the model fact_trips in 2019,2020
`select count(*) from fluent-tea-338517.dbt_sgopal.fact_trips where EXTRACT(YEAR from pickup_datetime) in (2019,2020)`

### Question 2: 
What is the distribution between service type filtering by years 2019 and 2020
https://datastudio.google.com/reporting/1977350c-fffd-4cd3-8e36-4cf00c113b17/page/oIFmC

### Question 3: 
count of records in the model stg_fhv_tripdata
`SELECT count(*) FROM fluent-tea-338517.dbt_sgopal.stg_fhv_tripdata`

### Question 4:
count of records in the model fact_fhv_trips
`SELECT count(*) FROM fluent-tea-338517.dbt_sgopal.fact_fhv_trips where EXTRACT(YEAR from pickup_datetime) in (2019)`

### Question 5:
month with the biggest amount of rides 
FHV Data Report - https://datastudio.google.com/reporting/53a84586-2997-42e4-8351-11522509d9b2/page/AJHmC/edit