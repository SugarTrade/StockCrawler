import datetime
import os
import socket
import urllib
import urllib.parse
import urllib.request

output_folder = './stock_all_byday/'
select_type = 'ALLBUT0999'

socket.setdefaulttimeout(30)

now = datetime.datetime.now()
yesterday = today = now

# Kaster: day -1 if still morning(Data has not updated)
# if(now.hour<12):
#   today = datetime.today() - timedelta(1)
#   yesterday=today
# iserr=0
for daynum in range(1, 40):
    path = yesterday.strftime('%Y%m%d')
    yy = str(yesterday.year - 1911)

    if yesterday.month < 10:
        mm = '0' + str(yesterday.month)
    else:
        mm = str(yesterday.month)

    if yesterday.day < 10:
        dd = '0' + str(yesterday.day)
    else:
        dd = str(yesterday.day)

    qdatein = '{0}/{1}/{2}'.format(yy, mm, dd)
    print(qdatein)

    url = "http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php"
    values = {
        'download': 'csv',
        'qdate': qdatein,
        'selectType': select_type
    }

    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(url, data.encode('utf-8'))
    response = urllib.request.urlopen(req)
    name = 'A112{0}{1}.csv'.format(path, select_type)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file1 = open(output_folder + name, "w")
    for line in response.read().decode('CP950'):
        if len(line) > 0:
            file1.writelines(line)
    file1.close()

    yesterday = yesterday - datetime.timedelta(days=1)
