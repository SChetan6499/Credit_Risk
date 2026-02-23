class PolicyAgent:

    @staticmethod
    def validate(application):
        violations = []

        if application.credit_score < 600:
            violations.append("Credit score below 600")

        dti = application.existing_debt / application.income

        if dti > 0.5:
            violations.append("Debt-to-Income ratio above 50%")

        return violations
