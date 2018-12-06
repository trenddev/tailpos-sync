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
    from_date = str_date + ' 00:00:00'
    end_date = (datetime.strptime(str_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d') + ' 00:00:00'
    sql = frappe.db.sql("SELECT sum(total_amount), count(*) FROM tabReceipts "
                        "WHERE date >='{0}' AND date <'{1}'".format(from_date, end_date))
    total_sales = '{:20,.2f}'.format(sql[0][0]).strip()
    total_count = sql[0][1]

    message = 'Sales Summary \nDate: {0} \nTotal Sales: P{1} \nTransactions: {2}'.format(str_date, total_sales, total_count)
    send_message(message, '+639177777981')
    send_message(message, '+639177779508')


def test_text():
    get_sales('2018-12-02')
