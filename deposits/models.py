from django.db import models


class Deposit(models.Model):

    deposit = models.CharField(max_length=50)
    term = models.CharField(max_length=1)
    rate = models.CharField(max_length=10)

    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate

    def interest(self):
        interest = self.deposit*self.term*self.rate

        return interest