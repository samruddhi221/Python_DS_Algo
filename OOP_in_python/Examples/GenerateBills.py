"""
You work in a company where you have to generate bills to the customer. Each customer has following:
* Each customer owns a List of Accounts.
* Every account has a list of Clusters.
* Every Cluster has a list of Resources (router, Hosts, Load balancers)

#### Cost for customer:
* The cost for a customer is the sum of cost for all accounts owned by customer.
* The cost of an account is total cost of all clusters under that account.
* The cost of an Cluster is total cost of all resource under that account.
"""
import functools
from abc import ABC, abstractmethod
from typing import List


class Resource(ABC):
    def __init__(self):
        self.price = 0


class Router(Resource):
    def __init__(self):
        super().__init__()
        self.__setattr__("price", 10)


class Host(Resource):
    def __init__(self):
        super().__init__()
        self.__setattr__("price", 20)


class LoadBalancer(Resource):
    def __init__(self):
        super().__init__()
        self.__setattr__("price", 30)


class Cluster:
    def __init__(self, resources: List[Resource]):
        self.resources = resources

    @property
    def price(self):
        # cost_sum = 0
        # for resource_ in self.resources:
        #     cost_sum += resource_.price
        # return cost_sum
        return functools.reduce(lambda x, y: x+y, [i.price for i in self.resources])


class Account:
    def __init__(self, clusters: List[Cluster]):
        self.clusters = clusters

    @property
    def price(self):
        # cost_sum = 0
        # for cluster_ in self.clusters:
        #     cost_sum += cluster_.price
        # return cost_sum
        return functools.reduce(lambda x, y: x+y, [i.price for i in self.clusters])


class Customer:
    def __init__(self, name: str, accounts: List[Account]):
        self.name = name
        self.accounts = accounts

    @property
    def price(self):
        # cost_sum = 0
        # for account_ in self.accounts:
        #     cost_sum += account_.price
        # return cost_sum
        return functools.reduce(lambda x, y: x+y, [i.price for i in self.accounts])


class AccountManager:
    def __init__(self, customers: List[Customer]):
        self.customer_map = {}              # customer_name: customer_object
        for customer in customers:
            self.customer_map[customer.name] = customer

    def generate_bill(self, customer_name):
        return self.customer_map[customer_name].price


cluster1 = Cluster([Router(), LoadBalancer(), Host()])
cluster2 = Cluster([LoadBalancer(), Host()])
cluster3 = Cluster([Router(), LoadBalancer()])

account1 = Account([cluster1, cluster2])
account2 = Account([cluster1, cluster3])
account3 = Account([cluster2, cluster3])

customer1 = Customer("A", [account1, account2])
customer2 = Customer("B", [account3, account2])
customer3 = Customer("C", [account1, account3])

account_manager = AccountManager([customer1, customer2, customer3])
print(account_manager.generate_bill("A"))
print(account_manager.generate_bill("B"))
print(account_manager.generate_bill("C"))

