# encoding utf-8

import mock

from .mocksPayable import fake_request,fake_request_fail_id,fake_request_fail_amount,fake_request_fail_recipient_id,fake_request_fail_status,fake_request_fail_installment
from .mocksPayable import fake_request_fail_transaction_id,fake_request_fail_split_rule_id,fake_request_fail_type
from .pagarme_test import PagarmeTestCase
from pagarme.payable import Payable,PagarmeApiError

class PayableTestCase(PagarmeTestCase):

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_id(self):
        payable = Payable(api_key='api_key')
        payable.find_by_id(1185564)
        self.assertEqual(1185564, payable.id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_id))
    def test_get_payable_by_id_fails(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_id(1185564)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_amount(self):
        payable = Payable(api_key='api_key')
        payable.find_by_amount(100000)
        self.assertEqual(100000, payable.amount)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_amount))
    def test_get_payable_by_amount_fails(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_amount(100000)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_recipient_id(self):
        payable = Payable(api_key='api_key')
        payable.find_by_recipient_id('re_citkg218g00hl8q6dh1pr5mld')
        self.assertEqual('re_citkg218g00hl8q6dh1pr5mld', payable.recipient_id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_recipient_id))
    def test_get_payable_by_recipient_id_fails(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_recipient_id('re_citkg218g00hl8q6dh1pr5mld')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_status(self):
        payable = Payable(api_key='api_key')
        payable.find_by_status('')
        self.assertEqual('paid', payable.status)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_status))
    def test_get_payable_by_status_fails(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_status('paid')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_installment(self):
        payable = Payable(api_key='api_key')
        payable.find_by_installment('null')
        self.assertEqual(None, payable.installment)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_installment))
    def test_get_payable_by_installment_fails(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_installment('null')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_transaction_id(self):
        payable = Payable(api_key='api_key')
        payable.find_by_transaction_id('1391617')
        self.assertEqual(None, payable.installment)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_transaction_id))
    def test_get_payable_by_transaction_id_fail(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_transaction_id('null')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_split_rule_id(self):
        payable = Payable(api_key='api_key')
        payable.find_by_split_rule_id('')
        self.assertEqual(None, payable.split_rule_id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_split_rule_id))
    def test_get_payable_by_split_rule_id_fail(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_split_rule_id('null')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_type(self):
        payable = Payable(api_key='api_key')
        payable.find_by_type('')
        self.assertEqual('credit', payable.type)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_type))
    def test_get_payable_by_type_fail(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_type('credit')