import sys
path = str(sys.argv[0]).split('/')[-1]
url = "https://test-api.intbee.com/"
url_f = "https://test-www.intbee.com/"
url_c = "https://test-item.intbee.com/"
url_u = 'http://test-api.intbee.com/'
url_wxappF = 'http://test-api.intbee.com/api/admin'

# url_dev = 'http://demo-api.intbee.com/'

if path == 'run_produce.py':
    url = "https://api.intbee.com/"
    url_f = "https://merchant.intbee.com/"
    url_c = "https://item.intbee.com/"
    url_u = 'http://api.intbee.com/'


if path == 'run_demo.py':
    url = "https://demo-api.intbee.com/"
    url_f = "https://demo-www.intbee.com/"
    url_c = "https://demo-item.intbee.com/"
    url_u = 'http://demo-api.intbee.com/'

