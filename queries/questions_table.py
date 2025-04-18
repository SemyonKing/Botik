from sqlalchemy import insert, select, update
from database import sync_engine
from models import metadata_obj, questions_table

def insert_questions_table(message: int, vopros: str, otvet: str, ochkov: int):
    with sync_engine.connect() as conn:
        querie = insert(questions_table).values(
                message_id = message,
                question = vopros,
                answer = otvet,
                points = ochkov,
                resolved = False,
                user = None
        )       
        conn.execute(querie)
        conn.commit()   

def update_user_question_table(otvet: str, user: str):
    with sync_engine.connect() as conn:
        querie =  update(questions_table).where(questions_table.c.answer == otvet).values(resolved = True, user = user)
        conn.execute(querie)
        conn.commit() 

def get_msg_id_questions_table(otvet: str):
    with sync_engine.connect() as conn:
        querie =  select(questions_table).where(questions_table.c.answer == otvet)
        try:
            for row in conn.execute(querie):
                return row[1]      
        except: return None

def get_question_questions_table(vopros: str):
    with sync_engine.connect() as conn:
        querie =  select(questions_table).where(questions_table.c.question == vopros)
        try:
            for row in conn.execute(querie):
                return row[2]
        except: return "null"

def get_question_answer_questions_table(otvet: str):
    with sync_engine.connect() as conn:
        querie =  select(questions_table).where(questions_table.c.answer == otvet)
        try:
            for row in conn.execute(querie):
                return row[2]
        except: return "null"

def get_answer_questions_table(otvet: str):
    with sync_engine.connect() as conn:
        querie =  select(questions_table).where(questions_table.c.answer == otvet)
        try:
            for row in conn.execute(querie):
                return row[3]
        except: return "null"

def get_poins_questions_table(otvet: str):
    with sync_engine.connect() as conn:
        querie =  select(questions_table).where(questions_table.c.answer == otvet)
        try:
            for row in conn.execute(querie):
                return row[4]
        except: return 0

def get_bool_questions_table(otvet: str):
    with sync_engine.connect() as conn:
        querie =  select(questions_table).where(questions_table.c.answer == otvet)
        try:    
            for row in conn.execute(querie):
                return row[5]
        except: return True