from sqlalchemy import insert, select, update
from database import sync_engine
from models import metadata_obj, products_table

def insert_products_table(imya: str, opisanya: str, ochkov: int):
    with sync_engine.connect() as conn:
        querie = insert(products_table).values(
                name = imya,
                description = opisanya,
                price = ochkov
        )       
        conn.execute(querie)
        conn.commit() 

def get_products_table():
    with sync_engine.connect() as conn:
        querie =  select(products_table)
        list = set()
        for row in conn.execute(querie):
            list.add(f"Имя: {row[1]}, Описание: {row[2]}, Цена: {row[3]}")
        return list
    
def get_product_products_table(product: str):
    with sync_engine.connect() as conn:
        querie =  select(products_table).where(products_table.c.name == product)
        try:
            for row in conn.execute(querie):
                return True
        except: return False

def get_product_price_products_table(product: str):
    with sync_engine.connect() as conn:
        querie =  select(products_table).where(products_table.c.name == product)
        try:
            for row in conn.execute(querie):
                return row[3] 
        except: return 0

def get_product_name_products_table(product: str):
    with sync_engine.connect() as conn:
        querie =  select(products_table).where(products_table.c.name == product)
        try:
            for row in conn.execute(querie):
                return row[1] 
        except: return "null"