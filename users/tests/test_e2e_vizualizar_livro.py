from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from library.models import Book
from django.utils.text import slugify
import time

class BookDetailE2ETest(LiveServerTestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Harry Potter e a Pedra Filosofal",
            details="Primeiro livro da série Harry Potter.",
            slug=slugify("Harry Potter e a Pedra Filosofal")
        )

        edge_options = Options()
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        self.browser = webdriver.Edge(options=edge_options)

    def tearDown(self):
        self.browser.quit()

    def test_book_detail_page(self):
        self.browser.get(f"{self.live_server_url}/")
        time.sleep(1)

        biblioteca_link = self.browser.find_element(By.LINK_TEXT, "Biblioteca")
        ActionChains(self.browser).move_to_element(biblioteca_link).click().perform()
        time.sleep(1)

        livro = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Harry Potter e a Pedra Filosofal")
        livro.click()
        time.sleep(1)

        titulo = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Harry Potter e a Pedra Filosofal", titulo)