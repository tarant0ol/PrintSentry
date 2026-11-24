import streamlit as st
import pandas as pd
from database import get_session
from models import *
from sqlalchemy import select
# from quality_repository import get_stage_parameter_dicts, save_quality_check 
# from quality_engine import evaluate_parameters





st.set_page_config(page_title="Контроль качества", layout="wide")
st.title("Контроль качества")


stmt = (
    select (
        QualityChecks.stage_id,
        ProductionStages.stage_name,
        QualityChecks.comment,
        QualityChecks.check_date,
        Employees.full_name,
    )
    .select_from(QualityChecks)
    .join(ProductionStages, ProductionStages.stage_id == QualityChecks.stage_id)
    .join(Employees, Employees.employee_id == QualityChecks.employee_id)
)

with get_session() as session:
    checks = session.execute(stmt).all()
    check_options = [f"{check.stage_id} — {check.stage_name}" for check in checks]

    rows = [{
        "Номер стадии задания": stage.stage_id,
        "Наим. стадии": stage.stage_name,
        "Дата проверки": stage.check_date,
        "Комментарий": stage.comment,
        "Ответственный": stage.full_name,
    }
    for stage in checks
    ]


selected_label = st.selectbox("Производственное задание", check_options)


# with get_session() as session:
#     params = get_stage_parameter_dicts(session, stage_id)

st.subheader("Данные о проверках")
if rows:
    st.dataframe(pd.DataFrame(rows), width='stretch', hide_index=True)


# if st.button("Выполнить проверку качества", type="primary"):
#     evaluation = evaluate_parameters(params)
#     with get_session() as session:
#         check = save_quality_check(session, stage_id, evaluation)
#         st.session_state["last_check_id"] = check.id
#     st.session_state["last_evaluation"] = evaluation

# evaluation = st.session_state.get("last_evaluation")
# if evaluation:
#     st.divider()
#     st.subheader("Результат оценки")
#     if evaluation.status == "Соответствует":
#         st.success(evaluation.status)
#     elif evaluation.status == "Недостаточно данных":
#         st.warning(evaluation.status)
#     else:
#         st.error(evaluation.status)
#     st.write(evaluation.summary)

#     for finding in evaluation.findings:
#         with st.expander(f"{finding.parameter_code}: {finding.severity}", expanded=True):
#             st.write(f"**Фактическое значение:** {finding.actual_value}")
#             st.write(f"**Допустимый диапазон:** {finding.expected_range}")
#             st.write(f"**Обоснование:** {finding.explanation}")
#             st.write(f"**Рекомендация:** {finding.recommendation}")

# st.divider()
# st.subheader("История проверок")
# with get_session() as session:
#     checks = session.query(QualityCheck).order_by(
#         QualityCheck.checked_at.desc()
#     ).limit(50).all()
#     history = [{
#         "ID": check.id,
#         "Стадия": check.stage.name,
#         "Заказ": check.stage.order.order_number,
#         "Результат": check.status,
#         "Дата": check.checked_at,
#         "Версия правил": check.rules_version,
#     } for check in checks]
# if history:
#     st.dataframe(pd.DataFrame(history), use_container_width=True, hide_index=True)
# else:
#     st.caption("Проверок пока нет.")
