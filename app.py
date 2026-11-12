import streamlit as st
from sqlalchemy import func
from database import get_session
from models import *

st.set_page_config(page_title="Контроль качества", page_icon="🧪", layout="wide")


st.title("Информационная система контроля качества")
st.caption("Прототип подсистемы контроля качества аддитивного производства")

with get_session() as session:
    orders_count = session.query(func.count(ProductionTasks.task_id)).scalar() or 0
    active_count = session.query(ProductionTasks).filter(
        ProductionTasks.status == "В работе"
    ).count()
    stages_count = session.query(func.count(ProductionStages.stage_id)).scalar() or 0
    checks_count = session.query(func.count(QualityChecks.check_id)).scalar() or 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Всего заказов", orders_count)
c2.metric("Заказов в работе", active_count)
c3.metric("Производственных стадий", stages_count)
c4.metric("Проверок качества", checks_count)

st.subheader("Рабочее пространство оператора")
# st.info(
#     "Используйте меню слева для просмотра заказов, запуска демонстрационной "
#     "проверки качества и просмотра оборудования."
# )
# st.warning(
#     "Правила контроля в этом прототипе демонстрационные. "
#     "Не используйте их для реального выпуска продукции без валидации."
# )
