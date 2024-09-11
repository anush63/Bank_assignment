from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=20, unique=True)
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.branch_name
