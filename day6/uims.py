import requests
from bs4 import BeautifulSoup
import json



BASE_URL = 'https://uims.cuchd.in'
AUTHENTICATE_URL = BASE_URL + '/uims/'

uid = ''
password = ''
attendence = "frmStudentCourseWiseAttendanceSummary.aspx"

response = requests.get(AUTHENTICATE_URL)
#print(response.headers,response.elapsed)
#print(response.headers['location'])
soup = BeautifulSoup(response.text, 'html.parser')
view_tag = soup.find("input",{"name":"__VIEWSTATE"})
#print(view_tag)
v = view_tag['value']

data = {'__VIEWSTATE':v,
        'txtUserId':uid,
        'btnNext':'NEXT'
        }
response = requests.post(AUTHENTICATE_URL,
                         data = data,
                         
                         allow_redirects = False
                         )

#print(response.headers['location'])
#print(response.text)
pass_url = BASE_URL+response.headers['location']
response = requests.get(pass_url)
login_cookies = response.cookies
soup = BeautifulSoup(response.text, 'html.parser')
view_tag = soup.find('input',{'name':'__VIEWSTATE'})

data = {'__VIEWSTATE':view_tag['value'],
        'txtLoginPassword':password,
        'btnLogin':'LOGIN'
        }

response = requests.post(pass_url,
                         data = data,
                         
                         allow_redirects = False
                         )
home_cookies = response.cookies

#print(response.status_code)
#print(response.elapsed)
#print(response.headers)
#print(login_cookies)
#print(home_cookies)
#combine_cookies = requests.cookies.merge_cookies(login_cookies, home_cookies)
#print(combine_cookies)
attendance_url =  AUTHENTICATE_URL+attendence
#response = requests.get(AUTHENTICATE_URL+attendence, cookies=home_cookies)

#print(response.text)
#response = requests.get('https://uims.cuchd.in/UIMS/assets/js/student/student_attendance_summary_1.2.js',cookies=home_cookies)
#print(response.text)

report = requests.get('https://uims.cuchd.in/UIMS/frmStudentCourseWiseAttendanceSummary.aspx',cookies=home_cookies)
#print(report.text)

js_report_block = response.text.find("GetFullReport")
initial_quotation_mark = js_report_block + response.text[js_report_block:].find("'")
ending_quotation_mark = initial_quotation_mark + response.text[initial_quotation_mark+1:].find("'")
report_id = response.text[initial_quotation_mark+1 : ending_quotation_mark+1]

report_url = attendance_url + "/GetFullReport"
headers = {'Content-Type': 'application/json'}
data = "{UID:'" + report_id + "'}"
response = requests.post(report_url, headers=headers, data=data)

attendance = json.loads(response.text)
print(attendence)
#print(response.text)
#print(json.loads(attendance))
#print(response.status_code)
#print(response.headers)
#print(response.text)
#print(response.text)
