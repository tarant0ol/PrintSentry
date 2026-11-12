from dataclasses import dataclass


@dataclass
class Finding:
    parameter_code: str
    actual_value: float | None
    expected_range: str
    severity: str
    explanation: str
    recommendation: str


@dataclass
class Evaluation:
    status: str
    summary: str
    findings: list[Finding]


# DEMO ONLY: replace these example ranges with values from validated
# technological regulations for the exact resin, printer and process.
RULES_VERSION = "demo-1.0"
LIMITS = {
    "exposure_time": {
        "min": 2.0, "max": 4.0, "unit": "с",
        "recommendation": "Проверить профиль экспозиции и соответствие материала."
    },
    "wash_time": {
        "min": 3.0, "max": 8.0, "unit": "мин",
        "recommendation": "Проверить регламент промывки, состояние и чистоту растворителя."
    },
}


def evaluate_parameters(parameters: list[dict]) -> Evaluation:
    if not parameters:
        return Evaluation(
            status="Недостаточно данных",
            summary="Для оценки не переданы производственные параметры.",
            findings=[]
        )

    findings = []
    seen = set()

    for parameter in parameters:
        code = parameter["code"]
        seen.add(code)
        rule = LIMITS.get(code)
        if rule is None:
            continue

        value = float(parameter["value"])
        if not rule["min"] <= value <= rule["max"]:
            findings.append(Finding(
                parameter_code=code,
                actual_value=value,
                expected_range=f'{rule["min"]}–{rule["max"]} {rule["unit"]}',
                severity="Предупреждение",
                explanation=(
                    f'Значение {value} {rule["unit"]} выходит за демонстрационный '
                    f'диапазон {rule["min"]}–{rule["max"]} {rule["unit"]}.'
                ),
                recommendation=rule["recommendation"]
            ))

    missing = set(LIMITS) - seen
    if missing:
        return Evaluation(
            status="Недостаточно данных",
            summary="Отсутствуют параметры: " + ", ".join(sorted(missing)),
            findings=findings
        )

    if findings:
        return Evaluation(
            status="Обнаружены отклонения",
            summary=f"Выявлено отклонений: {len(findings)}.",
            findings=findings
        )

    return Evaluation(
        status="Соответствует",
        summary="По проверенным демонстрационным правилам отклонений не выявлено.",
        findings=[]
    )
