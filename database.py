from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker,declarative_base

# DATABASE_URL="postgresql://postgres:Sanket123@localhost:5432/hms"
DATABASE_URL="postgresql://hms_3xku_user:rGl1fJBNiBcPKiP3UmCI2bOVGaxhIwuP@dpg-d67aubggjchc73ai9m0g-a.oregon-postgres.render.com/hms_3xku"

engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()
