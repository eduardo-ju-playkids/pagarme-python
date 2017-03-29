# encoding: utf-8

import requests

from .exceptions import PagarmeApiError
from .resource import AbstractResource
from .settings import BASE_URL

class Payable(AbstractResource):
    BASE_URL = BASE_URL + 'payables'

    def __init__(self, 
        api_key=None,
        id=None, 
        status=None, 
        amount=None,
        fee=None, 
        installment=None,
        transaction_id=None, 
    	split_rule_id=None,
    	bulk_anticipation_id=None,
    	recipient_id=None, 
        payment_date=None,
        original_payment_date=None, 
        type=None,
        payment_method=None, 
        date_created=None, 
        **kwargs):
        
        self.api_key = api_key
        self.id = id
        self.status = status
        self.amount = amount
        self.fee = fee
        self.installment = installment
        self.transaction_id = transaction_id
        self.split_rule_id = split_rule_id
        self.bulk_anticipation_id = bulk_anticipation_id
        self.recipient_id = recipient_id
        self.payment_date = payment_date
        self.original_payment_date = original_payment_date
        self.type = type
        self.payment_method = payment_method
        self.date_created = date_created
        self.data = {}

        for key, value in kwargs.items():
            self.data[key] = value

    def handle_response(self,data):
        self.id = data['id']
        self.status = data['status']
        self.amount = data['amount']
        self.fee = data['fee']
        self.installment = data['installment']
        self.transaction_id = data['transaction_id']
        self.split_rule_id = data['split_rule_id']
        self.bulk_anticipation_id = data['bulk_anticipation_id']
        self.recipient_id = data['recipient_id']
        self.payment_date = data['payment_date']
        self.original_payment_date = data['original_payment_date']
        self.type = data['type']
        self.payment_method = data['payment_method']
        self.date_created = ['date_created']
        self.data = data

    def get_data(self):
        return self.__dict__()

    def __dict__(self):
        d = self.data
        d['api_key'] = self.api_key
        d['status'] = self.status
        d['amount'] = self.amount
        d['fee'] = self.fee
        d['installment'] = self.installment
        d['transaction_id'] = self.transaction_id
        d['split_rule_id'] = self.split_rule_id
        d['bulk_anticipation_id'] = self.bulk_anticipation_id
        d['recipient_id'] = self.recipient_id
        d['payment_date'] = self.payment_date
        d['original_payment_date'] = self.original_payment_date
        d['type'] = self.type
        d['payment_method'] = self.payment_method
        d['date_created'] = self.date_created

        return d

    def find_by_id(self, id=None):
        url = self.BASE_URL + '/' + str(id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_amount(self, amount=None):
        url = self.BASE_URL + '/' + str(amount)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_recipient_id(self, recipient_id=None):
        url = self.BASE_URL + '/' + str(recipient_id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_status(self, status=None):
        url = self.BASE_URL + '/' + str(status)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_installment(self, installment=None):
        url = self.BASE_URL + '/' + str(installment)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_transaction_id(self, transaction_id=None):
        url = self.BASE_URL + '/' + str(transaction_id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_split_rule_id(self, split_rule_id=None):
        url = self.BASE_URL + '/' + str(split_rule_id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_type(self, type=None):
        url = self.BASE_URL + '/' + str(type)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())