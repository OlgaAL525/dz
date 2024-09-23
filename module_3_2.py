def send_email(recipient, *, sender = 'university.help@gmail.com'):
    L_s = len(sender)
    L_r = len(recipient)
    k = 0
    for i in range(L_r):
        if recipient[i] != '@':
            continue
        else:
            k += 1

    n = 0
    for i in range(L_s):
        if sender[i] != '@':
            continue
        else:
            n += 1

    s_4 = (sender[L_s - 4] + sender[L_s - 3] + sender[L_s - 2] + sender[L_s - 1]).lower()
    s_3 = (sender[L_s - 3] + sender[L_s - 2] + sender[L_s - 1]).lower()
    r_4 = (recipient[L_r - 4] + recipient[L_r - 3] + recipient[L_r - 2] + recipient[L_r - 1]).lower()
    r_3 = (recipient[L_r - 3] + recipient[L_r - 2] + recipient[L_r - 1]).lower()

    if (k == 0 or k > 1) or (n == 0 or n > 1) or (s_4 != '.com' and s_4 != '.net' and s_3 != '.ru') or (
            r_4 != '.com' and r_4 != '.net' and r_3 != '.ru'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес{recipient}')
        return


    if sender.lower() == recipient.lower():
        print('Нельзя отправить письмо самому себе')
        return


    if sender.lower() == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return

    if sender.lower() != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('lushnik@rambler.ru',sender = 'pos@mail.ru')