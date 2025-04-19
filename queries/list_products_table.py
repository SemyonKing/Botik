from sqlalchemy import insert, select, update, join
from database import sync_engine
from models import metadata_obj, list_products, products_table

def insert_list_products_table(product_id: int, user_id: int):
    with sync_engine.connect() as conn:
        querie = insert(list_products).values(
                user_id = user_id,
                product_id = product_id
        )       
        conn.execute(querie)
        conn.commit()  

def get_list_products_table(user_id: int):
    with sync_engine.connect() as conn:
        list = set()
        table = join(list_products, products_table, list_products.c.product_id == products_table.c.id)
        querie = select(list_products.c.user_id,products_table.c.name).select_from(table).where(list_products.c.user_id == user_id)     
        for row in conn.execute(querie):
            list.add(f"{row[1]}")
        return list

def get_boolean_list_products_table(product_id: int, user_id: int):
    with sync_engine.connect() as conn:
        list = set()
        querie = select(list_products).where(list_products.c.user_id == user_id, list_products.c.product_id == product_id)      
        try:
            for row in conn.execute(querie):
                return True
        except: return False
        