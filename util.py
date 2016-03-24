
out = open('mailmerge_database.csv', 'wb')
out.write('email,name,debt\n')

with open('shame.csv') as f:
  for line in f:
    words = line.split(',')
    unique_name = words[0]
    email = unique_name + "@umich.edu"
    out.write(email + ',' + words[1] + ',' + words[2])
