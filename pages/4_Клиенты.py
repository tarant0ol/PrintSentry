import streamlit as st
import pandas as pd
from database import  get_session
from models import *

st.set_page_config(page_title="Клиенты", layout="wide")
st.title("Клиенты")

with get_session() as session:
    clients = session.query(Clients).order_by(Clients.name).all()
    rows = [{
        "имя клиента": client.name,
        "номер телефона": client.phone,
        "эл. почта": client.email,
        "дата создания аккаунта": client.create_date,
    } for client in clients]

if rows:
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
else:
    st.info("Пока нет клиентов((")