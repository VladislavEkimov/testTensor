import time
import unittest
from selenium import webdriver


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
        textCategoryImage = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/div/div[1]/a/div[2]').text

        categoryImage.click()
        textInputImage = browser.find_element_by_css_selector("[name='text']").get_attribute('value')

        self.assertEqual(textCategoryImage, textInputImage, 'The text of the input field and the category is different')


    def testOpenImage(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.implicitly_wait(5)
        browser.get(link)

        linkImage = browser.find_element_by_css_selector("[data-id='images']")
        linkImage.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        categoryImage = browser.find_element_by_css_selector('.PopularRequestList-Item_pos_0')
        categoryImage.click()

        text = "'{\"row\":0,\"col\":0}'"
        image = browser.find_element_by_css_selector(f"[data-grid-position={text}]")
        imageUrl1 = browser.find_element_by_css_selector(f"[data-grid-position={text}] .serp-item__thumb").get_attribute('src')
        image.click()

        imageUrl2 = browser.find_element_by_css_selector('.MMImage-Preview').get_attribute('src')

        self.assertEqual(imageUrl1, imageUrl2, "The picture didn't open")


if __name__ == "__main__":
    unittest.main()