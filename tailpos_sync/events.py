import frappe
import requests
import urllib


def send_message(message, number):
    params = (
        ('apikey', 'xxxxxxxxxxx'),
        ('sendername', 'TAILPOS'),
        ('message', message),
        ('number', number)
    )
    path = 'https://semaphore.co/api/v4/messages?' + urllib.urlencode(params)
    requests.post(path)
    print 'Message Sent!'


def add_role(doc, method):
    doc.add_roles('Subscriber')
    doc.save()
