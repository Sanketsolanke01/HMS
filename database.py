from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="postgresql://hms_6tnp_user:IlTgZZD89jLvcNShsrCMzNNEv2ADPQ7L@dpg-d5gj0e6r433s73dnbfbg-a.oregon-postgres.render.com/hms_6tnp"

engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()
