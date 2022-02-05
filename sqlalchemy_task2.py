from sqlalchemy_task1 import students

ins = students.insert().values(name="Eric", lastname="Kowalski")

print(ins.compile().params)

sel = students.select().where(students.c.name=="Eric")
print(sel.compile())
print(sel.compile().params)

upd = students.update().where(students.c.name=="Eric").values(name="Jon")
print(upd.compile())
print(upd.compile().params)

rem = students.delete().where(students.c.lastname=="Kowalski")
print(rem.compile())
print(rem.compile().params)