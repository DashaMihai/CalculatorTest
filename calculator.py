import unittest
from selenium import webdriver

class Calculator(unittest.TestCase):

    def setUp(self):       
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()   
    def tear_down(self):
        self.driver.quit()

 
    def test_sum(self):   
        driver = self.driver    
        driver.get("http://qa-test.klika-tech.com/")
        driver.find_element_by_xpath("//*[text()='1']").click()
        button_plus = driver.find_element_by_xpath("//*[text()='+']")
        button_plus.click()        
        button_number = driver.find_element_by_xpath("//*[text()='2']")
        button_number.click()
        button_total = driver.find_element_by_xpath("//*[text()='=']")
        button_total.click()
        answer_field = driver.find_element_by_xpath("(//*[text()='3'])[1]")
        assert answer_field.text == "3"
    def test_mult(self):
        driver = self.driver    
        driver.get("http://qa-test.klika-tech.com/")
        button_reset = driver.find_element_by_xpath("//*[text()='AC']")
        button_reset.click()
        button_number = driver.find_element_by_xpath("//*[text()='3']")
        button_number.click()
        button_mult = driver.find_element_by_xpath("//*[text()='x']")
        button_mult.click()        
        button_number = driver.find_element_by_xpath("//*[text()='4']")
        button_number.click()
        button_total = driver.find_element_by_xpath("//*[text()='=']")
        button_total.click()
        answer_field = driver.find_element_by_xpath("(//*[text()='12'])[1]")
        assert answer_field.text == "12"
    def test_quotient(self):
        driver = self.driver    
        driver.get("http://qa-test.klika-tech.com/")
        button_reset = driver.find_element_by_xpath("//*[text()='AC']")
        button_reset.click()
        button_number = driver.find_element_by_xpath("//*[text()='5']")
        button_number.click()
        button_number = driver.find_element_by_xpath("//*[text()='6']")
        button_number.click()
        button_division = driver.find_element_by_xpath("//*[text()='/']")
        button_division.click()        
        button_number = driver.find_element_by_xpath("//*[text()='2']")
        button_number.click()
        button_total = driver.find_element_by_xpath("//*[text()='=']")
        button_total.click()
        answer_field = driver.find_element_by_xpath("(//*[text()='28'])[1]")
        assert answer_field.text == "28"
        
    def test_several_action(self):
        driver = self.driver    
        driver.get("http://qa-test.klika-tech.com/")
        button_reset = driver.find_element_by_xpath("//*[text()='AC']")
        button_reset.click()
        button_number = driver.find_element_by_xpath("//*[text()='9']")
        button_number.click()
        button_number = driver.find_element_by_xpath("(//*[text()='9'])[2]")
        button_number.click()
        button_division = driver.find_element_by_xpath("//*[text()='/']")
        button_division.click()        
        button_number = driver.find_element_by_xpath("//*[text()='3']")
        button_number.click()
        button_total = driver.find_element_by_xpath("//*[text()='=']")
        button_total.click()
        button_minus = driver.find_element_by_xpath("//*[text()='-']")
        button_minus.click()
        button_number = driver.find_element_by_xpath("//*[text()='8']")
        button_number.click()   
        button_total = driver.find_element_by_xpath("//*[text()='=']")
        button_total.click()
        answer_field = driver.find_element_by_xpath("//*[text()='25']")
        assert answer_field.text == "25"  
 

if __name__ == "__main__":
    unittest.main()
