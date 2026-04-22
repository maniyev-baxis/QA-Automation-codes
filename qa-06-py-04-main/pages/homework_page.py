
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

class neurotimepage:
    def __init__(self, page):
        self.page = page
        self.demo_name = page.locator("#root > div > header > div > div.header-nav-main > div.header-links-group > button > span")

    def random(self):
        self.page.goto("https://www.neurotime.ai/")


    def chekd(self):
        expect(self.demo_name).to_be_visible()
        expect(self.demo_name).not_to_be_enabled()


neuro = neurotimepage(page)
neuro.random()
neuro.chekd()




# class homeworkpage:
#     def __init__(self,page):
#         self.page = 

