# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:28:55 2019

@author: Thosani
"""

import nexmo
import smtplib
from datetime import date

import sqlite3

date1 = date.today()


def sent_notification(name,ph_number,mail,att_val):

    def send_sms(message):
        client = nexmo.Client(key='8bf9edeb', secret='V5rRhFAP0rCRQ7zR')

        client.send_message({
            'from': 'Nexmo',
            'to': '919769129969',
            'text': message,
        })
    def send_email(mail,message):
        print(mail)
        print(message)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("hulk64604@gmail.com","avengers@123" )
        s.sendmail("hulk64604@gmail.com", mail, message)
        s.quit()
    print(att_val)
    message="Your ward "+name+" was "
    if(att_val==True):
        message =message+" present"
    else:
        message =message+" absent"

    message = message + " on " + str(date1)
    send_email(mail,message)
    send_sms(message)

def sendNotificationdef(teacher_id):
    conn = sqlite3.connect('db.sqlite3')
    teacher_id = str(teacher_id)
    cursor=conn.execute('select * from IICapp_attendance a inner join IICapp_student s on a.student_id = s.id where teacher_id='+teacher_id)
    for row in cursor:
        print(row[7],row[10],row[11],row[1])
        sent_notification(row[7],row[10],row[11],row[1])
