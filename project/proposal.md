# Zoomcamp Project Proposal

## Project requirements
1. pipeline for processing dataset and putting it to a datalake 
2. pipeline for moving the data from the lake to a data warehouse 
3. Transform the data in the data warehouse: prepare it for the dashboard
4. Create a dashboard

## Dataset
[Spotify Dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-600k-tracks?select=tracks.csv)

## References
1. [Rubric](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_7_project)

## Technology choices
1. Cloud: GCP
2. Infrastructure as code (IaC): Terraform 
3. Workflow orchestration: Airflow 
4. Data Warehouse: BigQuery 
5. Batch processing: Spark 
6. Stream processing: None

## Project specific choices

1. Datalake: GCP Bucket
2. Transformations: dbt

## Problem description - Spotify Monitoring
Spotify data analytics monitor the popular tracks and the associated artists in a periodical manner. This project helps 
1. pull the raw data into GCP cloud
2. Transforms the raw data into standard tables
3. Joins the artists and tracks table to provide popularity metrics via dbt and write them back into BigQuery
4. Produce dashboard tiles in Google Data studio.
5. This allows the analytics to view the combined tracks and artists popularity information for quick review.

## Proposal to address the requirements
1. **Data ingestion** - Using Airflow to download the dataset and place it in GCP Bucket
2. **Data warehouse** - BigQuery will be used to host the tables
3. **Transformations** - Use dbt to convert transform the data from GCP bucket and add to BigQuery (partitioned and clustered)
4. **Dashboard** - Use Google Data studio to build the dashboards 

## Dashboard Tiles
1. Total number of tracks
2. Total number of artists
3. Most popular song - by popularity
4. Most popular artist - by followers
5. Most Tracks - Sort by Artist