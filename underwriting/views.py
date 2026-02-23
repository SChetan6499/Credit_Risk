from django.shortcuts import render, redirect
from .models import LoanApplication
from ai_engine.risk_agent import RiskAgent
from ai_engine.policy_agent import PolicyAgent
from ai_engine.explanation_agent import ExplanationAgent


def apply_loan(request):

    if request.method == "POST":
        application = LoanApplication.objects.create(
            name=request.POST["name"],
            age=int(request.POST["age"]),
            income=float(request.POST["income"]),
            loan_amount=float(request.POST["loan_amount"]),
            credit_score=int(request.POST["credit_score"]),
            employment_years=int(request.POST["employment_years"]),
            existing_debt=float(request.POST["existing_debt"]),
        )

        risk_probability, risk_level = RiskAgent.evaluate(application)
        violations = PolicyAgent.validate(application)

        # Decision Logic
        if risk_probability > 0.6 or violations:
            status = "REJECTED"
        else:
            status = "APPROVED"

        explanation = ExplanationAgent.explain(
            status, risk_level, violations, application
        )

        application.risk_probability = risk_probability
        application.loan_status = status
        application.decision_reason = explanation
        application.save()

        return render(request, "decision.html", {"app": application})

    return render(request, "apply_loan.html")
