from sqlalchemy import create_engine
from sqlalchemy.sql import text
connect = "postgresql://postgresql:Qsdr64@localhost:5432/SQL"

def test_con():
    create_engine(connect)

def test_insert():
    create_engine(connect)
    text("insert into subject (subject_titlevalues ('new_title')") 
def test_update():
    create_engine(connect)
    text("UPDATE subject set subject_title = 'title' where subject_id = null")
def test_delete():
    create_engine(connect)
    text("delete from subject where subject_title = 'new_title'")

