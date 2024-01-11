from pymongo import MongoClient
import streamlit as st

def connect_to_db(database):
    try:
        mongodb_uri = st.secrets["MONGODB_URI"]
        client = MongoClient(mongodb_uri)
        db = client[database]
        return db
    except Exception as e:
        print(f"An error occurred while connecting to the database: {str(e)}")
        return None
