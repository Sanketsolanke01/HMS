from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="postgresql://postgres:Sanket123@localhost:5432/hms"

engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()