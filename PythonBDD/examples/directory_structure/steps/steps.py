from behave import given, then
import Login.login


@given("I am in a directory")
def in_main_dir(context):
    print("In Main directory")

@then("I am also in a directory")
def in_add_dir(context):
    print("Also in Main dir")

@then("I am in subdirectory")
def in_sub_dir(context):
    print("I am sub directory")