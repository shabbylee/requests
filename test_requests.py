import requests
import xlrd
import json
import csv
import pyexcel_xlsx

f = open('data.csv')

reader = csv.DictReader(f, fieldnames=("key1", "key2", "key3"))

out = json.dumps(list(reader))

print type(out)

out_json = json.loads(out)

r_3 = requests.post('http://httpbin.org/post', json=out_json)

print r_3.content
print r_3.json()
print r_3.status_code

# r_1 = requests.get('http://httpbin.org/get')
#
# print r_1.text
# print r_1.json()
# print r_1.json()['origin']
# print r_1.status_code
#
#
# print type(r_1.content)
# print type(r_1.json())

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get",params=payload)
# print r.url

# partial_data = pyexcel_xlsx.get_data('test_data.xlsx', start_row=0)
# print json.dumps(partial_data)
# wb = xlrd.open_workbook('test_data.xlsx')



# with open('data.csv') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)
# print rows






# with open('data.json', 'w') as f:
#     data = json.dump(rows, f)


# Print the sheet names

# work_sheet =  wb.sheet_by_name('Sheet1')
#
# print json.dumps(work_sheet.row(1))

# files = {'file': open('test_data.xlsx', 'rb')}
# r_2 = requests.post("http://httpbin.org/post", files=files)
#
# print r_2.text