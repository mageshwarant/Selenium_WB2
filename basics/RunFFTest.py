from selenium import webdriver



class RunFFTest():

    def test(self):



        driver = webdriver.Firefox()

        driver.get("http://www.google.com")


ff = RunFFTest()
ff.test()
