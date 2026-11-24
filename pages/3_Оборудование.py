import streamlit as st
import pandas as pd
from database import  get_session
from models import *
from sqlalchemy import select

st.set_page_config(page_title="Оборудование", layout="wide")
st.title("Оборудование")

stmt = ( 
    select(
        EquipmentType.name,
        Equipment.serial_number,
        Equipment.status,
        Equipment.installation_date
    )
    .select_from(Equipment)
    .outerjoin(EquipmentModels, EquipmentModels.equipment_model_id == Equipment.equipment_model_id)
    .join(EquipmentType, EquipmentType.equipment_type_id == EquipmentModels.equipment_type_id)
)
with get_session() as session:
    equipment = session.execute(stmt).all()
    rows = [{
        "Тип об-я": item.name,
        "Серийный номер": item.serial_number,
        "Статус": item.status,
        "Дата установки": item.installation_date,
    } for item in equipment]

if rows:
    st.dataframe(pd.DataFrame(rows), width='stretch', hide_index=True)
    selected = st.selectbox("Выберите оборудование", [r["Серийный номер"] for r in rows])
    stmt = (
        select(
            ProductionTasks.task_id,
            ProductionStages.stage_name,
            StageEquipment.start_time,
            StageEquipment.end_time,
        )
        .select_from(StageEquipment)
        .outerjoin(Equipment, Equipment.equipment_id == StageEquipment.equipment_id)
        .outerjoin(ProductionStages, ProductionStages.stage_id == StageEquipment.stage_id)
        .outerjoin(ProductionTasks, ProductionStages.task_id == ProductionTasks.task_id)
        .where(Equipment.serial_number == selected)
    )

    with get_session() as session:
        equipment_stages = session.execute(stmt).all()

        equipment_stage_rows = [{
            "Номер задания": item.task_id,
            "Стадия": item.stage_name,
            "Время старта": item.start_time,
            "Время завершения": item.end_time,
        } for item in equipment_stages]

    if equipment_stage_rows:
        st.dataframe(pd.DataFrame(equipment_stage_rows), width='stretch', hide_index=True)

