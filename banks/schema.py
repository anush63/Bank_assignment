import graphene
from graphene_django.types import DjangoObjectType
from .models import Bank, Branch

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch

class BankType(DjangoObjectType):
    class Meta:
        model = Bank

class Query(graphene.ObjectType):
    branches = graphene.List(BranchType)
    banks = graphene.List(BankType)

    def resolve_branches(self, info, **kwargs):
        return Branch.objects.select_related('bank').all()

    def resolve_banks(self, info, **kwargs):
        return Bank.objects.all()

schema = graphene.Schema(query=Query)
