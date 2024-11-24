account_card = input("Введите тип и номер карты")
masked_account_card = ""
'''Функция,которая принимает тип и номер карты и выдает пользователю "зашифрованную информацию"'''
def mask_account_card(account_card):
    if len(account_card) == 24:
        masked_account_card = account_card.replace(account_card[14:20], "******")
        return masked_account_card
    elif len(account_card) == 27:
        masked_account_card = account_card.replace(account_card[17:23], "******")
        return masked_account_card
    elif len(account_card) == 29:
        masked_account_card = account_card.replace(account_card[19:25], "******")
        return masked_account_card
    elif len(account_card) == 26:
        masked_account_card = account_card.replace(account_card[16:22], "******")
        return masked_account_card
    elif len(account_card) == 30:
        masked_account_card = account_card.replace(account_card[20:26], "******")
        return masked_account_card
    elif len(account_card) == 25:
        return f"{account_card[0:5]} **{account_card[-4:]}"
    else:
        return "Введенные данные неверны"
'''Функция,которая принимает дату и выдает пользователю дату в формате "ДД.ММ.ГГГГ"'''
date = input("Введите дату")


def get_date(date):
    return f"{date[8:10]}.{date[5:7]}.{date[0:5]}"