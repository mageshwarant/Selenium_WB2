from behave import given, when, then

@given("I am in login Page")
def in_logon_page(context):
    print("In Logon Page")