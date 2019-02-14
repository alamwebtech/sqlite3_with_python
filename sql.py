import sqlite3
conn = sqlite3.connect("my_friends.db")
#Create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = ''' INSERT INTO friends
#                      VALUES ('Merriwether', 'Lewis', 7)'''

# Bad practise, do not insert data bellow shown way
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES('{form_first}')"

# Better way 

# form_first = "Marry-Todd"
# query = f"INSERT INTO friends(first_name) VALUES(?)"

# Anther way to insert data

# data = ("Steve", "Irwin", 9)
# query = "INSERT INTO friends VALUES(?,?,?)"


'''
BULK INSERT
'''


people = [("Roald", "Amundsen", 5),
("Rosa", "Park", 8),
("Henry", "Hudson", 7),
("Neil", "Armstrong", 7),
("Daniel", "Boone", 3)]



average = 0
for person in people:
	c.execute("INSERT INTO friends VALUES(?,?,?)", person)
	print("INSERTING NOW")



# c.execute(query,data)
#commit changes
conn.commit()
conn.close()