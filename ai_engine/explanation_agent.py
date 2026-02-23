from google import genai
from credit_risk import settings

import os

print("ENV KEY:", os.getenv("GEMINI_API_KEY"))
print("SETTINGS KEY:", settings.GEMINI_API_KEY)
client = genai.Client(api_key=settings.GEMINI_API_KEY)

# model = genai.GenerativeModel("gemini-2.5-flash")


class ExplanationAgent:

    @staticmethod
    def explain(status, risk_level, violations, application):

        prompt = f"""
        You are a senior bank credit underwriter.

        Loan Status: {status}
        Risk Level: {risk_level}
        Credit Score: {application.credit_score}
        Income: {application.income}
        Loan Amount: {application.loan_amount}
        Existing Debt: {application.existing_debt}
        Policy Violations: {violations}

        Explain clearly in 3-4 professional sentences
        why this loan was approved or rejected.
        Use banking language.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
