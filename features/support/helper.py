import logging
import allure
import requests
from jsonpath_ng import parse


class Helper:

    @staticmethod
    def assert_equals(expected_param, actual_param):
        logging.info(f"Expected: {expected_param}, Actual value: {actual_param}")
        assert expected_param == actual_param, 'Expected: {}, Actual value: {}'.format(expected_param, actual_param)

    def create_request(self, method_name, url, **kwargs):
        logging.info(f"Sending request: {method_name} to url: {url} with data {kwargs}")
        allure.attach(f"{kwargs}", name=f"Sending request: {method_name} to url: {url}",
                      attachment_type=allure.attachment_type.TEXT)
        self.response = requests.request(method_name, url, **kwargs)
        logging.info(self.response)
        allure.attach(f"{self.response}", name='Response', attachment_type=allure.attachment_type.TEXT)

    def assert_exists(self, key, value=''):
        jsonpath_expr = parse(f"$..{key}")
        result = jsonpath_expr.find(self.response.json())
        assert len(result) > 0, f"Body has no params like {key}"
        if value == '':
            return True
        else:
            assert result[0].value == value
