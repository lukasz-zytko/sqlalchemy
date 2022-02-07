from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('sqlite:///database.db')
conn = engine.connect()
metadata = MetaData()
table = Table("tasks", metadata, autoload=True, autoload_with=engine)

result = conn.execute(table.select())

for re in result:
    print(re)