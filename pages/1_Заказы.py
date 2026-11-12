import streamlit as st
import pandas as pd
from database import get_session
from models import *

st.set_page_config(page_title="Заказы", layout="wide")
st.title("Заказы")

with get_session() as session:
    orders = session.query(ProductionTasks).order_by(
        ProductionTasks.start_time.desc()
    ).all()
    rows = []
    for order in orders:
        rows.append({
            "Номер": order.task_id,
            # "Заказчик": order.customer_name,
            # "Изделие": order.product_name,
            "Статус": order.status,
            # "Количество стадий": len(order.stages),
        })

if rows:
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    selected = st.selectbox("Выберите заказ", [r["Номер"] for r in rows])
    with get_session() as session:
        order = session.query(ProductionOrder).filter_by(
            order_number=selected
        ).first()
        st.subheader(f"Стадии заказа {selected}")
        # stage_rows = [{
        #     "Стадия": stage.name,
        #     "Статус": stage.status,
        #     "Оборудование": stage.equipment.name if stage.equipment else "—",
        #     "Материал": stage.material.name if stage.material else "—",
        # } for stage in order.stages]
        # st.dataframe(pd.DataFrame(stage_rows), use_container_width=True, hide_index=True)
else:
    st.info("Заказов пока нет. Запустите seed.py для добавления демонстрационных данных.")
