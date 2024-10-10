def send_email(message, recipient, sender = "university.help@gmail.com"):
    if ("@" and (".com" or ".ru" or ".net") ) not in (recipient or sender) or ("@" or (".com" or ".ru" or ".net"))\
        not in (recipient or sender):
        print(f"'Невозможно отправить письмо с адреса' {sender} 'на адрес' {recipient}")
    elif sender == recipient:
        print("'Нельзя отправить письмо самому себе!'")
    elif sender == "university.help@gmail.com":
        print(f"'Письмо успешно отправлено с адреса' {sender} 'на адрес' {recipient}")
    elif sender != "university.help@gmail.com":
        print(f"'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса' {sender} 'на адрес' {recipient}")

send_email('messagie', "university.help@gmail.com", '@mail.com' )
send_email('messagie', "university.help@gmail.com" )
send_email('messagie', '@mail.com' )
send_email('messagie', '@mail.om')
send_email('messagie', 'mail.om')

