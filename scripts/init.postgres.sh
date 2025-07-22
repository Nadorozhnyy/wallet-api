#!/bin/bash

set -e
set -u

function create_user_and_database() {
	local database=$1
	echo "  Creating database $database with user $POSTGRES__USER"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES__USER" --dbname "postgres" <<-EOSQL
	    CREATE DATABASE $database;
	    GRANT ALL PRIVILEGES ON DATABASE $database TO $POSTGRES__USER;
EOSQL
}

if [ -n "$POSTGRES__DATABASE_NAME" ]; then
	echo "Multiple database creation requested: $POSTGRES__DATABASE_NAME"
	for db in $(echo "$POSTGRES__DATABASE_NAME" | tr ',' ' '); do
		create_user_and_database "$db"
	done
	echo "----Multiple databases created----"
fi
