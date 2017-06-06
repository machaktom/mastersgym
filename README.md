# Install PostgreSQL on ubuntu and Django connector
sudo apt-get install postgresql
sudo su - postgres
createdb mgbudget
createuser -P -d mgadmin
psql
GRANT ALL PRIVILEGES ON DATABASE mgbudget TO mgadmin;
(ctrl+D)
cdproject && pip install psycopg2

# Here is command to re-initialize database for the first time (creating user and database). This script will drop user and database if they exist
# Before running the script make sure that postgresql is running.
psql -U postgres -f doc/sql-scripts/re-init-database.sql
p:ython manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
