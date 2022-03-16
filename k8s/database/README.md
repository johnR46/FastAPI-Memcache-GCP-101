# check connection

> kubectl run my-db-postgresql-client --rm --tty -i --restart='Never' --image docker.io/bitnami/postgresql:14.2.0-debian-10-r25 --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql --host postgres-service -U mukulmantosh -d sampledb -p 5432