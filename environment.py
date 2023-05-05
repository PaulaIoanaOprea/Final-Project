from browser import Browser
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage


# before_all este o metoda care este recunoscuta de libraria behave.ini si care se va executa inainte de toate testele
def before_all(context):  # context ne ajuta sa accesam toate paginilie care vor putea fi folosite in alte fisiere
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()


# after_all este o metoda care este recunoscuta de libraria behave.ini si care se va executa dupa toate testele
def after_all(context):
    context.browser.close()
