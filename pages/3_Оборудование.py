# import streamlit as st
# import pandas as pd
# from database import  get_session
# from models import *

# st.set_page_config(page_title="Оборудование", layout="wide")
# st.title("Оборудование")

# with get_session() as session:
#     equipment = session.query(Equipment).order_by(Equipment.name).all()
#     rows = [{
#         "Наименование": item.name,
#         "Тип": item.equipment_type,
#         "Инвентарный номер": item.inventory_number,
#         "Статус": item.status,
#     } for item in equipment]

# if rows:
#     st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
# else:
#     st.info("Оборудование пока не зарегистрировано.")
