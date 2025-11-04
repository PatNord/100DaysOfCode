import smtplib
import pandas as pd
import datetime as dt

today = dt.datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv("birthdays.csv")

birthday_dict = {}
for item in df.iterrows():
    row = item[1]
    key = (row['month'], row['day'])
    birthday_dict[key] = {
        'name':row['name'],
        'email':row['email'],
        'year':row['year']
    }

if today_tuple in birthday_dict:

    person = birthday_dict[today_tuple]['name']
    person_email = birthday_dict[today_tuple]['email']
    with open("letter.txt", "r") as f:
        data = f.read()
        letter = data.replace("[NAME]", person)
   
    my_email = "nordlund.patrik94@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls() #<- secures the connection
    connection.login(user=my_email, password="DELETED")
    connection.sendmail(from_addr=my_email, to_addrs=person_email, msg=letter)
    connection.quit()

