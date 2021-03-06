# (Re)cria um db postgres
# uso:  recria_um_db_postgres <NOME DO BANCO>

set -e  # Exit immediately if a command exits with a non-zero status

echo "Database $1"
sudo -u postgres psql -c "drop DATABASE if exists $1"
sudo -u postgres psql -c "CREATE DATABASE $1 WITH OWNER = sapl ENCODING = 'UTF8' TABLESPACE = pg_default LC_COLLATE = 'pt_BR.UTF-8' LC_CTYPE = 'pt_BR.UTF-8' CONNECTION LIMIT = -1 TEMPLATE template0;"


echo "--- DJANGO MIGRATE ---" | tee -a $LOG
DATABASE_NAME=$1 ./manage.py migrate --settings sapl.legacy_migration_settings

