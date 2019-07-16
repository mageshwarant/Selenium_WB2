from selenium import webdriver



class RunFFTest():

    def test(self):

        # driverLocation = "C:\\Users\\hp\\Documents\\GitHub\\Coding\\Python\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation

        driver = webdriver.Chrome()

        driver.get("http://www.google.com")


ff = RunFFTest()
ff.test()
