from typing import Iterable, Any


def filter_by_state(dictionaries: Iterable [dict[Any, Any]], state: Any='EXECUTED') -> list[dict[Any, Any]]:
    executed_list = []
    for i in dictionaries:
        if i['state'] == state:
            executed_list.append(i)
    return executed_list


def sort_by_date(dictionaries: Iterable[dict[Any, Any]], reverse: bool=True) -> list[dict[Any, Any]]:
    list_for_date = sorted(dictionaries, key=lambda x: x['date'], reverse=reverse)
    return list_for_date