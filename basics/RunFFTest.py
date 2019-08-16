from selenium import webdriver



class RunFFTest():

    def test(self):

        #driver = webdriver.Firefox("C:\\Users\\hp\\Documents\\GitHub\\geckodriver-v0.24.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox()


        driver.get("http://www.google.com")
        print('opened Brower')


ff = RunFFTest()
ff.test()
