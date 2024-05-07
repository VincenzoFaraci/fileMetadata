# Importa la funzione create_engine da SQLAlchemy, che verrà utilizzata per creare un'istanza di motore per il database.
from sqlalchemy import create_engine

# Importa la funzione declarative_base da SQLAlchemy, che verrà utilizzata per definire la classe base per le classi di modello.
from sqlalchemy.ext.declarative import declarative_base

# Importa la funzione sessionmaker da SQLAlchemy, che verrà utilizzata per creare una classe Session per interagire con il database.
from sqlalchemy.orm import sessionmaker

# Definisce l'URL del database che verrà utilizzato da SQLAlchemy per connettersi al database.
SQLALCHEMY_DATABASE_URL = "sqlite:///./files.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()