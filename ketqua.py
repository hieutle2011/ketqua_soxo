#!usr/bin/env python3

# Kiểm tra giá trị đầu vào có trúng lô (trùng 2 số cuối với bất kỳ giải nào)
# trả về kết quả trúng lô. Nếu không trả về kết quả xổ số

from bs4 import BeautifulSoup as bs
import requests
import sys

url = 'http://ketqua.net/'
r = requests.get(url)
t = r.text
soup = bs(t, 'html.parser')
tags = soup('td')
lst = []
for tag in tags:
    if tag.get('id') is not None and tag.get('id').startswith('rs'):
        lst.append(tag.get('id'))
kq = [soup.find(id=i).text for i in lst]

won = []
for arg in sys.argv[1:]:
    for k in kq:
        try:
            if arg[-2:] == k[-2:] and arg[-2:] not in won:
                won.append(arg[-2:])
        except:
            print('Wrong integer format')
            quit()
if won == []:
    print('Khong co lo trung!\nKet qua xo so la:\n', kq)
else:
    print('Lo trung la:', won)
