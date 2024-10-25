def send_email (message, recipient, *, sender='university.help@gmail.com'):
    ends = ('.com', '.ru', '.net')
    if not recipient.endswith(ends) or not ('@' in recipient) or not sender.endswith(ends) or not ('@' in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('кукрыниксы', recipient='severianka1@yandex.ru')
send_email('глагол', recipient='university.help@gmail.com')
send_email('popados', recipient='banana.ru')
send_email('Best Student in the World', recipient='university.help@gmail.com', sender='university.fun@gmail.com')
