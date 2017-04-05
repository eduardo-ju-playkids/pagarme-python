import mock

from .mocksRecipient import fake_request,fake_request_fail_id,fake_request_fail_bankAccount_id,fake_request_fail_transfer_enabled,fake_request_fail_transfer_day
from pagarme.recipient import Recipient,PagarmeApiError
from pagarme.bankAccount import BankAccount
from .pagarme_test import PagarmeTestCase

class RecipientTestCase(PagarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_create_recipient_object_bankAccount(self):
        bankAccount = BankAccount(api_key='apikey', bank_code='341', agencia='3209', agencia_dv='4', conta='58054', conta_dv='1',
            type='conta_corrente',document_number='26268738888',legal_name='BANK ACCOUNT PYTHON')
        recipient = Recipient(api_key='api_key',transfer_interval='weekly', transfer_day=5,transfer_enabled='true', 
        	automatic_anticipation_enabled='true', anticipatable_volume_percentage=85, bank_account=bankAccount)
        recipient.charge()
        self.assertEqual('re_cj01ath3700xqs56dmv00epj6',recipient.id)

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_create_recipient_bankAccount_id(self):
        recipient = Recipient(api_key='api_key',transfer_interval='weekly', transfer_day=5,transfer_enabled='true', 
            automatic_anticipation_enabled='true', anticipatable_volume_percentage=85, bank_account_id='17422412')
        recipient.charge()
        self.assertEqual('re_cj01ath3700xqs56dmv00epj6',recipient.id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_recipient_by_id(self):
        recipient = Recipient(api_key='apikey')
        recipient.find_by_id('re_cj01ath3700xqs56dmv00epj6')
        self.assertEqual('re_cj01ath3700xqs56dmv00epj6', recipient.id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_id))
    def test_get_recipient_by_id_fail(self):
        recipient = Recipient(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            recipient.find_by_id('re_cj01ath3700xqs56dmv55wpj6')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request)) 
    def test_get_recipient_by_bankAccount_id(self):
        recipient = Recipient(api_key='apikey')
        params={"bank_account_id":17422412}
        recipient.find_by(params)
        self.assertEqual(params['bank_account_id'], recipient.bank_account['id'])

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_bankAccount_id))
    def test_get_recipient_by_bankAccount_id_fail(self):
        recipient = Recipient(api_key='apikey')
        params={"bank_account_id":17422413}
        with self.assertRaises(PagarmeApiError):
            recipient.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_recipient_by_transfer_enabled(self):
        recipient = Recipient(api_key='apikey')
        params={"transfer_enabled":True}
        recipient.find_by(params)
        self.assertEqual(params['transfer_enabled'],recipient.transfer_enabled)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_transfer_enabled))
    def test_get_recipient_by_transfer_enabled_fail(self):
        recipient = Recipient(api_key='apikey')
        params={"transfer_enabled":False}
        with self.assertRaises(PagarmeApiError):
            recipient.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_recipient_by_transfer_day(self):
        recipient = Recipient(api_key='apikey')
        params={"transfer_day":5}
        recipient.find_by(params)
        self.assertEqual(params['transfer_day'], recipient.transfer_day)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_transfer_day))
    def test_get_recipient_by_transfer_day_fail(self):
        recipient = Recipient(api_key='apikey')
        params={"transfer_day":8}
        with self.assertRaises(PagarmeApiError):
            recipient.find_by(params)