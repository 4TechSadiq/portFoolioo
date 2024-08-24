import smtplib

USER = "sadiqcp2023@gmail.com"
PASSWORD = "uajknfahhmfhisri"

def send_mail(name:str, mail:str, msg: str, nmbr: str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs="sadikcp2014@gmail.com", msg=f"Subject:portfoliio!!\n\n Name:{name}\n Mail:{mail}\n number{nmbr} \n Message:{msg}")
        
        return True