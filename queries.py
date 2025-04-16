from sqlalchemy import text, insert, Table, select
from database import sync_engine
from models import metadata_obj, questions_table, users_table

def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def insert_questions_table(vopros: str, otvet: str, ochkov: int):
    with sync_engine.connect() as conn:
        querie = insert(questions_table).values(
                question = vopros,
                answer = otvet,
                points = ochkov
        )       
        conn.execute(querie)
        conn.commit()   

def insert_users_table(imya: str, ochkov: int):
    with sync_engine.connect() as conn:
        querie = insert(users_table).values(
                username = imya,
                points = ochkov
        )       
        conn.execute(querie)
        conn.commit()  


def get_questions_table(otvet: str):
    with sync_engine.connect() as conn:
        querie =  select(questions_table).where(questions_table.c.answer == otvet)
        for row in conn.execute(querie):
            return True