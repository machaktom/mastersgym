# Here is command to re-initialize database for the first time (creating user and database). This script will drop user and database if they exist
# Before running the script make sure that postgresql is running.
psql -U postgres -f doc/sql-scripts/re-init-database.sql

# To initialize the databases for Django appplication run
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
