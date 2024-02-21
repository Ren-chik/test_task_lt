import json
import sys


def create_report(filled_tests):
    report = {'tests': filled_tests}
    with open('report.json', 'w') as file:
        json.dump(report, file, indent=2)


def load_json(file):
    with open(file, 'r') as file:
        data = json.load(file)
    return data


def get_data(tests, results):
    test_list = tests.get('tests')
    result_dict = {result['id']: result['value'] for result in results.get('values')}
    return fill_tests(test_list, result_dict)


def fill_tests(test_list, result_dict):
    for test in test_list:
        if 'value' in test:
            test['value'] = result_dict.get(test['id'])
        if 'values' in test:
            fill_tests(test['values'], result_dict)
    return test_list


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    tests = load_json(sys.argv[1])
    values = load_json(sys.argv[2])

    filled_tests = get_data(tests, values)

    create_report(filled_tests)
