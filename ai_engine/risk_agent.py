from .ml_model import predict_risk


class RiskAgent:

    @staticmethod
    def evaluate(application):
        data = [
            application.credit_score,
            application.income,
            application.loan_amount,
            application.employment_years,
            application.existing_debt,
        ]

        risk_probability = predict_risk(data)

        if risk_probability > 0.6:
            risk_level = "HIGH"
        elif risk_probability > 0.4:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        return risk_probability, risk_level
