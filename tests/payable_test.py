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
            payable.find_by_id(1185566)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_amount(self):
        payable = Payable(api_key='api_key')
        params={"amount":100000}
        payable.find_by(100000)
        self.assertEqual(params['amount'], payable.amount)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_amount))
    def test_get_payable_by_amount_fails(self):
        payable = Payable(api_key='apikey')
        params={"amount":200000}
        with self.assertRaises(PagarmeApiError):
            payable.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_recipient_id(self):
        payable = Payable(api_key='api_key')
        params={"recipient_id":'re_citkg218g00hl8q6dh1pr5mld'}
        payable.find_by(params)
        self.assertEqual(params['recipient_id'], payable.recipient_id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_recipient_id))
    def test_get_payable_by_recipient_id_fails(self):
        payable = Payable(api_key='apikey')
        params={"recipient_id":'re_citkg218g00hl8q6dh1pr5dfg'}
        with self.assertRaises(PagarmeApiError):
            payable.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_status(self):
        payable = Payable(api_key='api_key')
        params={"status":'paid'}
        payable.find_by(params)
        self.assertEqual(params['status'], payable.status)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_status))
    def test_get_payable_by_status_fails(self):
        payable = Payable(api_key='apikey')
        params={"status":'waiting_funds'}
        with self.assertRaises(PagarmeApiError):
            payable.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_installment(self):
        payable = Payable(api_key='api_key')
        params={"installment":None}
        payable.find_by(params)
        self.assertEqual(params['installment'], payable.installment)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_installment))
    def test_get_payable_by_installment_fails(self):
        payable = Payable(api_key='apikey')
        params={"installment":1}
        with self.assertRaises(PagarmeApiError):
            payable.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_transaction_id(self):
        payable = Payable(api_key='api_key')
        params={"transaction_id":1391617}
        payable.find_by(params)
        self.assertEqual(params['transaction_id'], payable.transaction_id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_transaction_id))
    def test_get_payable_by_transaction_id_fail(self):
        payable = Payable(api_key='apikey')
        params={"transaction_id":None}
        with self.assertRaises(PagarmeApiError):
            payable.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_split_rule_id(self):
        payable = Payable(api_key='api_key')
        params={"split_rule_id":None}
        payable.find_by(params)
        self.assertEqual(params['split_rule_id'], payable.split_rule_id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_split_rule_id))
    def test_get_payable_by_split_rule_id_fail(self):
        payable = Payable(api_key='apikey')
        params={"split_rule_id":'sr_ci7xsejbp000awq16wr5rkweh'}
        with self.assertRaises(PagarmeApiError):
            payable.find_by(params)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_payable_by_type(self):
        payable = Payable(api_key='api_key')
        params={"type":'credit'}
        payable.find_by(params)
        self.assertEqual(params['type'], payable.type)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_type))
    def test_get_payable_by_type_fail(self):
        payable = Payable(api_key='apikey')
        params={"type":None}
        with self.assertRaises(PagarmeApiError):
            payable.find_by(params)