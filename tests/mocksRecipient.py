import json

class FakeResponse(object):
    status_code = 200
    content = '''
    {
        "object": "recipient",
        "id": "re_cj01ath3700xqs56dmv00epj6",
        "transfer_enabled": true,
        "last_transfer": null,
        "transfer_interval": "weekly",
        "transfer_day": 5,
        "automatic_anticipation_enabled": true,
        "anticipatable_volume_percentage": 85,
        "date_created": "2017-03-08T18:29:15.340Z",
        "date_updated": "2017-03-08T18:29:15.340Z",
        "bank_account": {
            "object": "bank_account",
            "id": 17422412,
            "bank_code": "341",
            "agencia": "3209",
            "agencia_dv": "5",
            "conta": "58054",
            "conta_dv": "1",
            "type": "conta_corrente",
            "document_type": "cpf",
            "document_number": "26268738888",
            "legal_name": "BANK ACCOUNT PYTHON",
            "charge_transfer_fees": true,
            "date_created": "2017-03-08T18:29:09.644Z"
        }
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
        "url":"/recipients/","method":"get"
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
        "message":"recipient id inv\xc3\xa1lido"}],
        "url":"/recipients/re_cj01ath3700xqs56dmv00epj6","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_bankAccount_id(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"bankAccount_id",
        "message":"bankAccount id inv\xc3\xa1lido"}],
        "url":"/recipients/17422412","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_transfer_enabled(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"transfer_enabled",
        "message":"transfer_enabled inv\xc3\xa1lido"}],
        "url":"/recipients/true","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_transfer_day(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"transfer_day",
        "message":"transfer_day inv\xc3\xa1lido"}],
        "url":"/recipients/5","method":"get"
    }
    """
    fake.status_code = 400
    return fake