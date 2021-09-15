import time
import unittest
from selenium import webdriver
from selenium.webdriver.common import keys


class TestYandex(unittest.TestCase):

    def testInput(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)
        if browser.find_elements_by_xpath('//*[@id="text"]'):
            input = True
        else:
            input = False
        self.assertEqual(input, True, 'No input field')

    def testSearch(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)
        input = browser.find_element_by_xpath('//*[@id="text"]')
        input.send_keys('тензор')

        if browser.find_element_by_css_selector("[role='listbox']"):
            suggest = True
        else:
            suggest = False
        self.assertEqual(suggest, True, 'No suggest field')

    def testLink(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)
        input = browser.find_element_by_xpath('//*[@id="text"]')
        input.send_keys('тензор')
        input.send_keys(keys.Keys.ENTER)
        temp = 0



        link1 = browser.find_element_by_css_selector("[data-cid='1']").text
        link2 = browser.find_element_by_css_selector("[data-cid='2']").text
        link3 = browser.find_element_by_css_selector("[data-cid='3']").text
        link4 = browser.find_element_by_css_selector("[data-cid='4']").text
        browser.execute_script("window.scrollTo(0, 200);")
        link5 = browser.find_element_by_css_selector("[data-cid='5']").text


        if ('tensor.ru' in link1) or ('tensor.ru' in link2) or ('tensor.ru' in link3) or ('tensor.ru' in link4) or ('tensor.ru' in link5):
            temp += 1

        self.assertNotEqual(temp, 0, 'There is no link tensor.ru in the first five results')



if __name__ == "__main__":
    unittest.main()
