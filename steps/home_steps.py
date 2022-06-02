from behave import *

@given ('i am testing herokuapp')
def step_impl(context):
    context.herokuapp_home.navigate_to_page()

@when('checking form')
def step_impl(context):
    context.herokuapp_home.click_form()

@when('checking basic')
def step_impl(context):
    context.herokuapp_home.click_basic()

@when('checking digest')
def step_impl(context):
    context.herokuapp_home.click_digest()

@then('last check')
def step_impl(context):
    context.herokuapp_home.check_current_url()


@when('checking download')
def step_impl(context):
    context.herokuapp_home.click_download()

@when('checking upload')
def step_impl(context):
    context.herokuapp_home.click_upload()