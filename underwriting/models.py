from django.db import models


class LoanApplication(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    income = models.FloatField()
    loan_amount = models.FloatField()
    credit_score = models.IntegerField()
    employment_years = models.IntegerField()
    existing_debt = models.FloatField()

    risk_probability = models.FloatField(null=True, blank=True)
    loan_status = models.CharField(max_length=20, null=True, blank=True)
    decision_reason = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
