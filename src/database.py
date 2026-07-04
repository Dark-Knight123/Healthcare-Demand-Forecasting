from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres@localhost:5432/mimic_demo"
engine = create_engine(DATABASE_URL)