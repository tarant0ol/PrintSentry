# import streamlit as st
# import pandas as pd
# from database import get_session
# from models import *
# from quality_repository import get_stage_parameter_dicts, save_quality_check 
# from quality_engine import evaluate_parameters

# st.set_page_config(page_title="Контроль качества", layout="wide")
# st.title("Контроль качества")

# with get_session() as session:
#     stages = session.query(ProductionStage).all()
#     stage_options = {
#         f"{stage.order.order_number} — {stage.name} (ID {stage.id})": stage.id
#         for stage in stages
#     }

# if not stage_options:
#     st.info("Нет производственных стадий. Сначала добавьте демо-данные.")
#     st.stop()

# selected_label = st.selectbox("Производственная стадия", list(stage_options))
# stage_id = stage_options[selected_label]

# with get_session() as session:
#     params = get_stage_parameter_dicts(session, stage_id)

# st.subheader("Производственные параметры")
# if params:
#     st.dataframe(pd.DataFrame(params), use_container_width=True, hide_index=True)
# else:
#     st.warning("Для выбранной стадии параметры не зарегистрированы.")

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
