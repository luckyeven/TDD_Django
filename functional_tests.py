from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

class NewVisitorTest(unittest.TestCase): 
    def setUp(self):  
        self.browser = webdriver.Firefox()  

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_todo_list(self):  
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")  

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)  
        header_text = self.browser.find_element(By.TAG_NAME,"h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"),"Enter a to-do item")

        # types Buy peacock teathers into a text box
        # inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys("Use peacock feathers to make a fly")

        # when hit enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID,"id_list_table")
        rows = table.find_elements(By.TAG_NAME,"tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn(
        "2: Use peacock feathers to make a fly",
        [row.text for row in rows],
    )
        # Satisfied, she goes back to sleep
        self.fail("Finish the test!")

if __name__ == "__main__":  
    unittest.main()  