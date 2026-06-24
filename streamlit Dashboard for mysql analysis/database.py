from sqlalchemy import create_engine
import pandas as pd
from config import *

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

def load_data(query):
    return pd.read_sql(query, engine)