touch shame.csv
rm shame.csv
wget https://chezbetty.eecs.umich.edu/shame.csv
dos2unix shame.csv
echo "Adding @umich extensions..."
python util.py
echo "Mail merge database setup!"
