import requests

from .exceptions import PagarmeApiError, NotBoundException
from .resource import AbstractResource
from .settings import BASE_URL


class Recipient(AbstractResource):
    BASE_URL = BASE_URL + 'recipients'

    def __init__(
        self,
        api_key=None,
        transfer_interval=['daily','weekly','monthly'],
        transfer_day=None,
        transfer_enabled=['true','false'],
        automatic_anticipation_enabled=['true','false'],
        anticipatable_volume_percentage=None,
        bank_account=None,
        bank_account_id=None,
        **kwargs):

        self.api_key = api_key
        self.transfer_interval = transfer_interval
        self.transfer_day = transfer_day
        self.transfer_enabled = transfer_enabled
        self.automatic_anticipation_enabled = automatic_anticipation_enabled
        self.anticipatable_volume_percentage = anticipatable_volume_percentage
        self.bank_account = bank_account
        self.bank_account_id = bank_account_id
        self.id = None
        self.data = {}

        for key, value in kwargs.items():
            self.data[key] = value

    def handle_response(self, data):
        self.id = data['id']
        self.transfer_interval = data['transfer_interval']
        self.transfer_day = data['transfer_day']
        self.transfer_enabled = data['transfer_enabled']
        self.automatic_anticipation_enabled = data['automatic_anticipation_enabled']
        self.anticipatable_volume_percentage = data['anticipatable_volume_percentage']
        self.bank_account = data['bank_account']
    
    def __dict__(self):
        d = self.data
        d['api_key'] = self.api_key
        d['transfer_interval'] = self.transfer_interval
        d['transfer_day'] = self.transfer_day
        d['transfer_enabled'] = self.transfer_enabled
        d['automatic_anticipation_enabled'] = self.automatic_anticipation_enabled
        d['anticipatable_volume_percentage'] = self.anticipatable_volume_percentage
        d['bank_account'] = self.bank_account

        return d

    def get_data(self):
        return self.__dict__()

    def charge(self):
        self.create()

    def find_by_id(self, id=None):
        url = self.BASE_URL + '/' + str(id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_bank_account_id(self, bank_account_id=None):
        url = self.BASE_URL + '/' + str(bank_account_id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_transfer_enabled(self, transfer_enabled=None):
        url = self.BASE_URL + '/' + str(transfer_enabled)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_transfer_day(self, transfer_day=None):
        url = self.BASE_URL + '/' + str(transfer_day)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())