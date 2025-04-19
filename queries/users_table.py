from sqlalchemy import insert, select, update
from database import sync_engine
from models import metadata_obj, users_table

def insert_users_table(imya: str, user_id: int, ochkov: int):
    with sync_engine.connect() as conn:
        querie = insert(users_table).values(
                user_id = user_id,
                username = imya,
                points = ochkov
        )       
        conn.execute(querie)
        conn.commit()  

def get_user_points(user_id: int):
    with sync_engine.connect() as conn:
        querie =  select(users_table).where(users_table.c.user_id == user_id)
        try:
            for row in conn.execute(querie):
                return row[2]
        except: return 0

def get_bool_user_table(user_id: int):
    with sync_engine.connect() as conn:
        querie =  select(users_table).where(users_table.c.user_id == user_id)
        try:
            for row in conn.execute(querie):
                return True
        except: return False

def update_user_table(user_id: int, ochkov: int):
    with sync_engine.connect() as conn:
        querie =  update(users_table).where(users_table.c.user_id == user_id).values(points = users_table.c.points + ochkov)
        conn.execute(querie)
        conn.commit()  