from sqlalchemy import Table, Identity, Column, Integer, String, MetaData, Boolean

metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj, 
    Column("id", Integer, Identity(start=1,increment=1), primary_key=True),
    Column("username", String),
    Column("points", Integer, default=0)
)
questions_table = Table(
    "questions",
    metadata_obj, 
    Column("id", Integer, Identity(start=1,increment=1), primary_key=True),
    Column("message_id", Integer),
    Column("question", String),
    Column("answer", String),
    Column("points", Integer),
    Column("resolved", Boolean),
    Column("user", String, nullable=True)
)
products_table = Table(
    "products",
    metadata_obj, 
    Column("id", Integer, Identity(start=1,increment=1), primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("price", Integer)
)
list_products = Table(
    "list_products",
    metadata_obj, 
    Column("id", Integer, Identity(start=1,increment=1), primary_key=True),
    Column("username", String),
    Column("productname", String),
)
