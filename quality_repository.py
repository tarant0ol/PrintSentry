from models import QualityCheck, QualityFinding, ProductionParameter
from services.quality_engine import RULES_VERSION


def save_quality_check(session, stage_id: int, evaluation):
    check = QualityCheck(
        stage_id=stage_id,
        status=evaluation.status,
        summary=evaluation.summary,
        rules_version=RULES_VERSION,
    )
    session.add(check)
    session.flush()

    for item in evaluation.findings:
        session.add(QualityFinding(
            check_id=check.id,
            parameter_code=item.parameter_code,
            actual_value=item.actual_value,
            expected_range=item.expected_range,
            severity=item.severity,
            explanation=item.explanation,
            recommendation=item.recommendation,
        ))
    session.commit()
    return check


def get_stage_parameter_dicts(session, stage_id: int):
    rows = session.query(ProductionParameter).filter_by(stage_id=stage_id).all()
    return [
        {"code": row.code, "name": row.name, "value": row.value, "unit": row.unit}
        for row in rows
    ]
