## Week 1
### Google Details
2. Project Name: taxi-rides-ny
4. export GOOGLE_APPLICATION_CREDENTIALS="<file-name>"
5. Used `export PYTHONHTTPSVERIFY=0` to get through the SSL issue 

### Docker Commands for Postgres
```shell
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data:rw" \
  -p 5432:5432 \
  -d \
  postgres:13
  
```