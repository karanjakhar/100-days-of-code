from uims_api import SessionUIMS


bot_token = ''
bot_chatID = ''
bot_message = 'hello'
print('here')
# replace these with your credentials
my_account = SessionUIMS("", "")
print('here...')
# `my_acc.attendance` returns attendance info for available subjects in JSON format
subjects = my_account.attendance

# display attendance for each subject
for subject in subjects:
    #subject_attendance = "{} - {}%".format(subject["Title"], subject["TotalPercentage"])
    print(subject)
    #print(subject['Total_Delv'],subject['Total_Attd'])
    #subject_attendace = '{} - {}%'.format(subject[])
    #send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    #requests.get(send_text)
    #print(subject_attendance)





