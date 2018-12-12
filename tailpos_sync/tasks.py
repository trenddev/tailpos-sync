import frappe
from datetime import datetime, timedelta
import requests
import urllib

def send_message(message, number):
    params = (
        ('apikey', '64229633532ecd99ddada36b000ac85f'),
        ('sendername', 'TAILPOS'),
        ('message', message),
        ('number', number)
    )
    path = 'https://semaphore.co/api/v4/messages?' + urllib.urlencode(params)
    requests.post(path)
    print 'Message Sent!'


# date format
def get_sales(str_date):
    sql = frappe.db.sql("SELECT sum(total_amount), count(*) FROM tabReceipts WHERE date ='{0}'".format(str_date))
    total_sales = '{:20,.2f}'.format(sql[0][0]).strip()
    total_count = sql[0][1]

    message = 'Sales Summary \nDate: {0} \nTotal Sales: P{1} \nTransactions: {2}'.format(str_date, total_sales, total_count)
    send_message(message, '+639177777981')
    send_message(message, '+639177779508')
    send_message(message, '+639977491965')


def send_sales():
    get_sales((datetime.now().date() - timedelta(days=1)).strftime('%Y-%m-%d'))
