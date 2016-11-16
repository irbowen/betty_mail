#!/bin/bash


echo "Copy the starting db header over to the database"
cp mailmerge_starting_database.csv mailmerge_database.csv

echo "Avoiding errors..."
touch shame.csv
rm shame.csv

echo "Getting the shame list..."
wget https://chezbetty.eecs.umich.edu/shame.csv
dos2unix shame.csv

echo "Adding @umich extensions..."
./util.py >> mailmerge_database.csv

echo "Mail merge database setup! About to email..."
mailmerge --dry-run --no-limit
