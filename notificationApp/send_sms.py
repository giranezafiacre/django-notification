import requests
def send_sms( phone_number):
    data = {
        'recipients': f'{phone_number}',
        'message': f'this is notification message',
        'sender': '+250785405716',
    }

    r = requests.post('https://www.intouchsms.co.rw/api/sendsms/.json', data,
                      auth=('fiacregiraneza', 'pass123'))
    print(r.json(), r.status_code)
    return r.json()