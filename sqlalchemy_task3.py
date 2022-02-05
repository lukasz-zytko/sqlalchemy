from sqlalchemy_task1 import students, engine

"""
ins = students.insert().values(name="Łukasz", lastname="Żytko")
conn = engine.connect()
result = conn.execute(ins, {'name': 'John', 'lastname': 'Cleese'},
   {'name': 'Graham', 'lastname': 'Chapman'}
)
"""

sel = students.select().where(students.c.id>3)
conn = engine.connect()
result = conn.execute(sel)

for row in result:
    print(row)