from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    PRODUCT_ITEM = (By.CLASS_NAME, "product-item")
    PRODUTC_TITLE = (By.CLASS_NAME, "product-title")

    def are_all_the_products_displayed(self):  # verifica daca avem produse afisate
        self.wait_for_element_to_be_present(self.PRODUCT_ITEM, 2)
        product_item_list = self.find_all(self.PRODUCT_ITEM)
        # daca gaseste vreun produs ce nu este afisat, returneaza fals si iese imediat din functie
        for item in product_item_list:
            if not item.is_displayed():
                return False

        return True

    def are_all_titles_containing_text(self, text: str):  # verifica daca toate titlurile de produs un text dat
        title_list = self.find_all(self.PRODUTC_TITLE)
        # daca gaseste vreun titlu ce nu contine un text cautat, returneaza fals si iese imediat din functie
        for title in title_list:
            if text.lower() not in title.text.lower():
                return False

        return True

