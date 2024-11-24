from src.masks import card_number, get_mask_card_number

"""Импорт функций, которые маскируют номер карты"""
from src.masks import account_number, get_mask_account

"""Импорт функций, которые маскируют номер счета"""

from src.widget import account_card, mask_account_card

print(get_mask_card_number(card_number))
"""Вывод функций, которые маскируют номер карты"""
print(get_mask_account(account_number))
"""Вывод функций, которые маскируют номер счета"""
print(mask_account_card(account_card))
