from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

cadena_base_datos = "sqlite:///veterinaria.db"

engine = create_engine(cadena_base_datos, echo=False)

Session = sessionmaker(bind=engine)
session = Session()