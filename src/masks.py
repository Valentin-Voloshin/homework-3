card_number = (input("Введите номер карты"))
lenght_of_card_number = len(str(card_number))
#Длина номера карты, для проверки со стандартной длиной


def get_mask_card_number(card_number):
    if lenght_of_card_number == 16:
        mask_card_number = card_number.replace(card_number[6:12], "******")
        list_mask_card_number = []
        for elements in range(lenght_of_card_number // 4):
            list_mask_card_number.append(f"{mask_card_number[elements * 4:(elements + 1) * 4]}")
        splited_mask_card_number = " ".join(list_mask_card_number)
        return splited_mask_card_number
    else:
        return "Неверно введены данные(стандартный номер карты - 16 цифр)"


'''Функция, которая принимает у пользователя номер карты и форматирует его в "скрытый" формат'''
account_number = str(input("Введите номер вашего счета"))
#Номер счета, который мы получаем от пользователя


def get_mask_account(account_number):
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Номер счета введен неверно(стандартный номер счета содержит - 20 цифр)"

'''Функция, которая принимает у пользователя номер счета и форматирует его в "скрытый" формат'''
