import smtplib
from vklancer import api
import time
from email.mime.text import MIMEText

MY_ID = 120733253  # VK ID
TARGET_EMAIL = 'komarnitskij.v@phystech.edu'  # 'admin@provizor.com'
TIME_FOR_CHECK = (21, 52, 0)  # (Hours, Minutes, Seconds)
PAUSE = 15  # secs
ACCESS_TOKEN = '1681a3411681a3411681a341eb16dc9dc3116811681a3414fe4550523ce4719042792e4'  # DO NOT TOUCH
MY_EMAIL = 'komarik200026@gmail.com'
MY_PASSWORD = 'C3prmt^VJ@QF'


def isTimeToSendStats():
    current_time = (time.ctime().split()[3]).split(':')
    return int(current_time[0]) == TIME_FOR_CHECK[0] and int(current_time[1]) == TIME_FOR_CHECK[1] and TIME_FOR_CHECK[
        2] <= int(current_time[2]) < \
           TIME_FOR_CHECK[2] + PAUSE


def send_email(online_time):
    online_time = time.strftime('%H:%M:%S', time.gmtime(online_time))
    date = ' '.join(time.ctime().split()[1:3])
    info = vk.users.get(access_token=ACCESS_TOKEN, user_ids=MY_ID)['response'][0]
    text = MIMEText('{date} 2018. {first_name} {last_name} has been online for {online_time}'.format(date=date,
                                                                                                     first_name=info[
                                                                                                         'first_name'],
                                                                                                     last_name=info[
                                                                                                         'last_name'],
                                                                                                     online_time=online_time))
    text['Subject'] = 'Время в сети'
    text['From'] = MY_EMAIL
    text['To'] = TARGET_EMAIL
    print(text.as_string())
    mail.sendmail(MY_EMAIL, TARGET_EMAIL, text.as_string())


# TODO: допилить емэйл


def mainloop():
    online_time_for_a_day = 0
    while 1:
        if isTimeToSendStats():
            send_email(online_time_for_a_day)
            online_time_for_a_day = 0
        info = vk.users.get(access_token=ACCESS_TOKEN, user_ids=MY_ID, fields='online')['response']
        if info[0]['online']:
            online_time_for_a_day += PAUSE
        time.sleep(PAUSE)


if __name__ == '__main__':
    vk = api.API(version='5.74')
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    mail.login(MY_EMAIL, MY_PASSWORD)
    mainloop()
