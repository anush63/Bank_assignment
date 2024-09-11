from django.test import TestCase
from graphene.test import Client
from .schema import schema

class BankBranchTests(TestCase):
    def setUp(self):
        # Set up initial data
        pass

    def test_branch_query(self):
        client = Client(schema)
        query = '''
        query {
            branches {
                edges {
                    node {
                        branchName
                        bank {
                            name
                        }
                        ifsc
                    }
                }
            }
        }
        '''
        executed = client.execute(query)
        self.assertIn('branches', executed)
