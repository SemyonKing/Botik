from sqlalchemy import insert, select, update
from database import sync_engine
from models import metadata_obj, list_products

def insert_list_products_table(product: str, user: str):
    with sync_engine.connect() as conn:
        querie = insert(list_products).values(
                username = user,
                productname = product
        )       
        conn.execute(querie)
        conn.commit()  

def get_list_products_table(user: str):
    with sync_engine.connect() as conn:
        list = set()
        querie = select(list_products).where(list_products.c.username == user)      
        for row in conn.execute(querie):
            list.add(f"{row[2]}")
        return list
 
def get_boolean_list_products_table(user: str, product: str):
    with sync_engine.connect() as conn:
        list = set()
        querie = select(list_products).where(list_products.c.username == user, list_products.c.productname == product)      
        try:
            for row in conn.execute(querie):
                return True
        except: return False
        