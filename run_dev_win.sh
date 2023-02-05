POSTGRES_NAME=test_postgres
CHECK_POSTGRES_CREATED="$(docker images|grep $POSTGRES_NAME)"

echo "Running/Creating postgresDB for developing"
docker run --rm --name $POSTGRES_NAME -v "$PWD/postgresdb_volume" -e POSTGRES_PASSWORD=django -e POSTGRES_USER=testuser -e POSTGRES_DB=testdb -p 5432:5432 postgres
