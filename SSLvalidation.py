import OpenSSL
import ssl, socket
import datetime
import time
import win32com.client as win32

path = 'C:/Users/c5290346/Desktop/input.txt'
file = open(path, 'r')
for line in file:
    a = line.split(',')
    url = a[0]
    gtg = int(a[1])
    email = a[2]

    cert = ssl.get_server_certificate((url, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    expiration = x509.get_notAfter()

    exp_day = expiration[6:8].decode('utf-8')
    exp_month = expiration[4:6].decode('utf-8')
    exp_year = expiration[:4].decode('utf-8')
    exp_date = exp_day+'.'+exp_month+'.'+exp_year
    exp_date = datetime.datetime.strptime(exp_date, '%d.%m.%Y')
    now = datetime.date.today()

    today = datetime.datetime.strptime(now, '%d.%m.%Y')
    #today = datetime.datetime.strptime('10.08.2019', '%d.%m.%Y')

    expires = exp_date - today
    days_left = expires.days

    if days_left > gtg:
        print('Das Zertifikat von ' + url + ' ist noch ' + str(days_left) + ' Tage gültig.')
    elif days_left < 0:
        days_left = abs(days_left)
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = email
        mail.Subject = 'Zertifikat abgelaufen'
        mail.Body = 'Das Zertifikat für ihre Website ' + url + ' ist seit ' + days_left + ' Tagen abgelaufen.\n'
        mail.Send()
    else:
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = email
        mail.Subject = 'Zertifikat läuft ab'
        mail.Body = 'Das Zertifikat für ihre Website ' + url + ' ist nur noch ' + str(days_left) + ' Tage gültig.\n'
        mail.Send()


file.close()