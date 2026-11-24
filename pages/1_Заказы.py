import streamlit as st
import pandas as pd
from database import get_session
from models import *
from sqlalchemy import select

st.set_page_config(page_title="Заказы", layout="wide")
st.title("Заказы")

with get_session() as session:
    orders = (
        session.query(
            ProductionTasks.task_id,
            ProductionTasks.start_time,
            ProductionTasks.end_time,
            ProductionTasks.status,
            Materials.name.label("material_name"),
        )
        .select_from(ProductionTasks)
        .join(MaterialBatches, ProductionTasks.material_batch_id == MaterialBatches.batch_id)
        .join(Materials, MaterialBatches.material_id == Materials.material_id)
        .order_by(ProductionTasks.start_time.desc())
        .all()
    )


    rows = [
        {
            "Номер": order.task_id,
            "Время начала": order.start_time,
            "Время завершения": order.end_time,
            "Используемый материал": order.material_name,
            "Статус": order.status,
        }
        for order in orders
    ]


if rows:
    st.dataframe(pd.DataFrame(rows), width='stretch', hide_index=True)
    selected = st.selectbox("Выберите заказ", [r["Номер"] for r in rows])
    stmt = (
        select(
            Products.name,
            OrderProducts.quantity,
            OrderProducts.unit_price,
            ProductionTasks.task_id,
            ProductionTasks.status
        )
        .join(Orders, OrderProducts.order_id == Orders.order_id)
        .join(Products, OrderProducts.product_id == Products.product_id)
        .outerjoin(ProductionTasks, OrderProducts.order_product_id == ProductionTasks.order_product_id)
        .where(Orders.order_id == selected)
    )
    st.subheader(f"Заказ {selected}")
    with get_session() as session:
        products = session.execute(stmt).all()

        product_rows = [{
            "Наим. продукта": product.name,
            "Кол-во": product.quantity,
            "цена за шт.": product.unit_price,
            "Номер задания": product.task_id,
            "Статус задания": product.status,
        } for product in products]

if product_rows:
    st.dataframe(pd.DataFrame(product_rows), width='stretch', hide_index=True)
    selected = st.selectbox("Выберите номер задания", [r["Номер задания"] for r in product_rows])
    stmt = (
        select(
            ProductionStages.stage_name,
            ProductionStages.start_time,
            ProductionStages.end_time,
            ProductionStages.status,
            Materials.name,
            # StageEquipment.equipment_id
        )
        .select_from(ProductionTasks)
        .outerjoin(ProductionStages,  ProductionTasks.task_id == ProductionStages.task_id)
        .join(MaterialBatches, ProductionTasks.material_batch_id == MaterialBatches.batch_id)
        .join(Materials, MaterialBatches.material_id == Materials.material_id)
        # .join(StageEquipment, ProductionStages.stage_id == StageEquipment.stage_id)
        .where(ProductionTasks.task_id == selected)
    )
    st.subheader(f"Задание {selected}")
    with get_session() as session:
        stages = session.execute(stmt).all()

        stage_rows = [{
            "Наим. стадии": stage.stage_name,
            "Время старта": stage.start_time,
            "Время завершения": stage.end_time,
            "Статус стадии": stage.status,
            "Наим. материала": stage.name,
            # "Используемое оборудование": stage.equipment_id
        } for stage in stages]

    if stage_rows:
        st.dataframe(pd.DataFrame(stage_rows), width='stretch', hide_index=True)

