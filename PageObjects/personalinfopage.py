from selenium.webdriver.common.by import By
from PageObjects.userhomepage import userhome


class personalinfo:

    # constructor to get driver
    def __init__(self, testdriver):
        self.localdriver = testdriver

    # locators
    Titlemr = (By.ID, "id_gender1")
    Titlemrs = (By.ID, "id_gender2")
    Fname = (By.ID, "customer_firstname")
    Lname = (By.ID, "customer_lastname")
    Pwd = (By.XPATH, "//*[@id='passwd']")
    Addrs = (By.ID, "address1")
    City = (By.CSS_SELECTOR, "[name='city']")
    State = (By.ID, "id_state")
    Post = (By.CSS_SELECTOR, "[id='postcode']")
    Otr = (By.ID, "other")
    Mobile = (By.ID, "phone_mobile")
    Submt = (By.ID, "submitAccount")

    # methods to return locators
    def titleselectmr(self):
        return self.localdriver.find_element(*personalinfo.Titlemr)

    def titleselectmrs(self):
        return self.localdriver.find_element(*personalinfo.Titlemrs)

    def setfname(self):
        return self.localdriver.find_element(*personalinfo.Fname)

    def setlname(self):
        return self.localdriver.find_element(*personalinfo.Lname)

    def setpwd(self):
        return self.localdriver.find_element(*personalinfo.Pwd)

    def setaddrs(self):
        return self.localdriver.find_element(*personalinfo.Addrs)

    def setcity(self):
        return self.localdriver.find_element(*personalinfo.City)

    def setstate(self):
        return self.localdriver.find_element(*personalinfo.State)

    def setpost(self):
        return self.localdriver.find_element(*personalinfo.Post)

    def setaddninfo(self):
        return self.localdriver.find_element(*personalinfo.Otr)

    def setmobile(self):
        return self.localdriver.find_element(*personalinfo.Mobile)

    def register(self):
        self.localdriver.find_element(*personalinfo.Submt).click()
        Usrhome = userhome(self.localdriver)
        return Usrhome
