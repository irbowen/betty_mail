#!/bin/bash

echo "Cloning mailmerge"
git clone https://github.com/mavcook/mailmerge.git
cp filter_deter.py mailmerge/mailmerge/

echo "Copy the starting db header over to the database"
cp mailmerge_starting_database.csv mailmerge_database.csv



shame_file='./shame.csv'
if [ -f "$shame_file" ]
then
	echo "Using previous shame list..."
else
	echo "Avoiding errors..."
	touch shame.csv
	rm shame.csv

	echo "Getting the shame list..."
	wget https://chezbetty.eecs.umich.edu/shame.csv
	dos2unix shame.csv
fi

echo "Adding @umich extensions..."
./util.py >> mailmerge_database.csv

echo "Mail merge database setup! About to email..."
python ./mailmerge/mailmerge/main.py --dry-run --no-limit --template-functions filter_deter
