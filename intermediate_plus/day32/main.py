import smtplib
import datetime as dt
import random

#This project sends motivational quote on mondays to spesific email and stores used quotes on seperate txt file.

quotes = []
used_quotes = []

with open("quotes.txt") as f:
    for line in f:
        quotes.append(line.strip())



def send_email():
    global used_quotes
    quotes_not_used = [q for q in quotes if q not in used_quotes]
    random_quote = random.choice(quotes_not_used)

    try:
        with open("used_quotes.txt") as f:
            used_quotes = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        used_quotes = []
   
   
    my_email = "nordlund.patrik94@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls() #<- secures the connection
    connection.login(user=my_email, password="DELETED")
    connection.sendmail(from_addr=my_email, to_addrs="Patrik.Nordlund@yahoo.com", msg=f"Subject:Motivation\n\n{random_quote}")
    connection.quit()

    used_quotes.append(random_quote)
    with open("used_quotes.txt", "a") as f:
        f.write(random_quote + "\n")

now = dt.datetime.now()
day = now.weekday()

if day == 0:
    send_email()

print(used_quotes)

