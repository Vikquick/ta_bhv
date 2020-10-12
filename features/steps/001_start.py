import logging
import json as j
from behave import step
from features.support.helper import Helper


@step('check response code is "{code:n}"')
def step_impl(context, code):
    Helper.assert_equals(code, context.response.status_code)


@step('send "{method_name}" to url "{url}" with json "{json}"')
def step_impl(context, method_name, url, json):
    logging.info(method_name.upper())
    Helper.create_request(context, method_name.upper(), url, json=j.loads(json))


@step('check response body has param "{key}" with value "{value}"')
def step_impl(context, key, value):
    Helper.assert_exists(context, key=key, value=value)


@step('check response body has param "{key}"')
def step_impl(context, key):
    Helper.assert_exists(context, key=key)
