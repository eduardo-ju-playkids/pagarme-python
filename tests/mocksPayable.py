import json

class FakeResponse(object):
    status_code = 200
    content = '''
    {
        "object": "payable",
        "id": 1185564,
        "status": "paid",
        "amount": 100000,
        "fee": 380,
        "anticipation_fee": 0,
        "installment": null,
        "transaction_id": 1391617,
        "split_rule_id": null,
        "bulk_anticipation_id": null,
        "recipient_id": "re_citkg218g00hl8q6dh1pr5mld",
        "payment_date": "2017-03-24T03:00:00.777Z",
        "original_payment_date": null,
        "type": "credit",
        "payment_method": "boleto",
        "date_created": "2017-03-24T19:10:58.823Z"
    }
    '''

    def json(self):
        return json.loads(self.content)

def fake_request_list(*args, **kwargs):
    fakeresponse = FakeResponse()
    fakeresponse.content = '[' + fakeresponse.content + ']'
    return fakeresponse

def fake_request(*args, **kwargs):
    return FakeResponse()

def fake_request_fail_api_key(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"api_key",
        "message":"api_key inv\xc3\xa1lida"}],
        "url":"/payables/","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_id(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"id",
        "message":"payable id inv\xc3\xa1lido"}],
        "url":"/paybles/1185564","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_amount(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"amount",
        "message":"amount inv\xc3\xa1lido"}],
        "url":"/paybles/100000","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_recipient_id(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"recipient_id",
        "message":"recipient_id inv\xc3\xa1lido"}],
        "url":"/paybles/re_citkg218g00hl8q6dh1pr5mld","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_status(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"status",
        "message":"status inv\xc3\xa1lido"}],
        "url":"/paybles/paid","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_installment(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"installment",
        "message":"installment inv\xc3\xa1lida"}],
        "url":"/paybles/null","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_transaction_id(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"transaction_id",
        "message":"transaction_id inv\xc3\xa1lida"}],
        "url":"/paybles/1391617","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_split_rule_id(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"split_rule_id",
        "message":"split_rule_id inv\xc3\xa1lida"}],
        "url":"/paybles/null","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_type(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"type",
        "message":"type inv\xc3\xa1lida"}],
        "url":"/paybles/credit","method":"get"
    }
    """
    fake.status_code = 400
    return fake