from behave import given, when, then

@given("I am in a directory")
def in_main_dir(context):
    print("In Main directory")

@then("I am also in a directory")
def in_add_dir(context):
    print("Also in Main dir")