import time
import unittest
from selenium import webdriver
import Selenium2Library

class TestYandexImages(unittest.TestCase):
    def testLinkImages(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)

        if browser.find_elements_by_css_selector("[data-id='images']"):
            result = 1
        else:
            result = 0
        self.assertEqual(result, True, 'Link Pictures missing on the page')


    def testUrl(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)
        linkImage = browser.find_element_by_css_selector("[data-id='images']")
        linkImage.click()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        url = browser.current_url
        self.assertIn('https://yandex.ru/images/', url, "Couldn't navigate to the URL https://yandex.ru/images/")

    def testCategory(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)

        linkImage = browser.find_element_by_css_selector("[data-id='images']")
        linkImage.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        categoryImage = browser.find_element_by_css_selector('.PopularRequestList-Item_pos_0')
        categoryImage.click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()