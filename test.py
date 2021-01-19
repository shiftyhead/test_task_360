from unittest import TestCase
from main import ClassifierModel, classifier_processor


class ClassifierTest(TestCase):
    input_data = [
        {
            'code': '1',
            'name': 'name 1',
        },
        {
            'code': '2',
            'name': 'name 2',
        },
        {
            'code': '1.1',
            'name': 'name 1.1',
        },
        {
            'code': '1.2',
            'name': 'name 1.2',
        },
        {
            'code': '1.2.1',
            'name': 'name 1.2.1',
        },
        {
            'code': '1.2.2',
            'name': 'name 1.2.2',
        },
    ]
    result = [
        {'code': '1', 'name': 'name 1', 'children': [
            {'code': '1.1', 'name': 'name 1.1', 'children': []},
            {'code': '1.2', 'name': 'name 1.2', 'children': [
                {'code': '1.2.1', 'name': 'name 1.2.1', 'children': []},
                {'code': '1.2.2', 'name': 'name 1.2.2', 'children': []},
            ]}
        ]},
        {'code': '2', 'name': 'name 2', 'children': []},
    ]

    def test_classifier_processor(self):
        test_data = [ClassifierModel(**item) for item in self.input_data]
        processed_data = classifier_processor(test_data)
        self.assertEqual(processed_data, self.result)
