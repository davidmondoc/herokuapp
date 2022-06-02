from behave import *

@given('')
def step_impl(context):
    context.login_page( )

@when('')
def step_impl(context,user):
    context.login_page.login_action( user )

@when('')
def step_impl(context,password):
    context.login_page.password_action( password )

@when ('')
def step_impl(context):
    context.login_page.LOGIN_BTN( )

@then
def step_implem(context):
    context.check_current_url()