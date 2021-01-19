from collections import namedtuple
from typing import List

ClassifierModel = namedtuple('ClassifierModel', ['code', 'name'])


def format_result(data: dict):
    if data.get('children') == {}:
        data['children'] = []
        return
    children = data.get('children', {}).values()
    for child in children:
        format_result(child)
    data['children'] = list(children)


def classifier_processor(input_data: List[ClassifierModel]):
    result = {}
    sorted_data = sorted(input_data, key=lambda x: x.code)
    for item in sorted_data:
        item_code_sequence = item.code.split('.')
        pointer = result
        for level, number in enumerate(item_code_sequence):
            if number not in pointer:
                if len(item_code_sequence) - level == 1:
                    pointer[number] = {
                        'code': item.code,
                        'name': item.name,
                        'children': {}
                    }
                else:
                    print(f'No parent for {item.code}!')
                    break
            else:
                pointer = pointer[number]['children']

    _ = [format_result(item) for item in result.values()]
    return list(result.values())


