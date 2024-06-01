# Python Object Relational Mapping

## Learning Objectives
- Why python programming is awesome
- How to connet to a MySQL database from a Python script
- How to SELECT rows in MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

without ORM:
```python3
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf-8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in rows:
	print(row)
cur.close()
conn.close()
```

with an ORM:
```python3
engine = create.engine("mysql+mysqldb://{}:{}@localhost/{}".format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
	print("{}: {}".format(state.id, state.name))
session.close()
```
