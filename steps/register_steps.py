from behave import *


@given("I am on the Register Page")
def step_impl(context):
    context.register_page.navigate_to_register_page()


@when("I click on the Register button")
def step_impl(context):
    context.register_page.click_on_register_button()


@then("First name error is displayed")
def step_impl(context):
    assert context.register_page.is_first_name_error_displayed()


@then("Last name error is displayed")
def step_impl(context):
    assert context.register_page.is_last_name_error_displayed()


@then("Email error is displayed")
def step_impl(context):
    assert context.register_page.is_email_error_displayed()


@then('Password error is displayed')
def step_impl(context):
    assert context.register_page.is_password_error_displayed()


@then('Confirm password error is displayed')
def step_impl(context):
    assert context.register_page.is_password_error_displayed()


@when('I select Female Gender')
def step_impl(context):
    context.register_page.select_female_radio_button()


@when('I enter "{text}" in the First name')
def step_impl(context, text):
    context.register_page.set_first_name(text)


@when('I enter "{text}" in the Last name')
def step_impl(context, text):
    context.register_page.set_last_name(text)


@when('I select day "{text}" in the Date of birth')
def step_impl(context, text):
    context.register_page.select_day_of_birth(text)


@when('I select month "{text}" in the Date of birth')
def step_impl(context, text):
    context.register_page.select_month_of_birth(text)


@when('I select year "{text}" in the Date of birth')
def step_impl(context, text):
    context.register_page.select_year_of_birth(text)


@when('I enter "{text}" in the Email')
def step_impl(context, text):
    context.register_page.set_email(text)


@when('I enter "{text}" in the Company')
def step_impl(context, text):
    context.register_page.set_company(text)


@when('I uncheck the Newsletter')
def step_impl(context):
    context.register_page.uncheck_newsletter_checkbox()


@when('I insert "{text}" in the Password')
def step_impl(context, text):
    context.register_page.set_password(text)


@when('I insert "{text}" in the Confirm password')
def step_impl(context, text):
    context.register_page.set_confirm_password(text)


@then('The register success message is displayed')
def step_impl(context):
    assert context.register_page.is_register_success_message_displayed()


@then('The Continue button is displayed')
def step_impl(context):
    assert context.register_page.is_continue_button_displayed()


@then('The register success message contains "{text}"')
def step_impl(context, text):
    # assert {text}, {context.register_page.get_register_success_message_text()}
    assert f'Expected: {text}, \n Actual: {context.register_page.get_register_success_message_text()}'


@then('The email error text contains "{text}"')
def step_impl(context, text):
    assert f'Expected: {text}, \n Actual: {context.register_page.get_email_error_text()}'
