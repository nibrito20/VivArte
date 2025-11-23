from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library.models import Book, Wishlist

class WishlistE2ETest(LiveServerTestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="nciuw78432rjidscn923r"
        )
        self.book = Book.objects.create(
            title="Harry Potter e a Pedra Filosofal",
            details="Detalhes do livro",
            slug="harry-potter-e-a-pedra-filosofal"
        )

        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 15)

    def tearDown(self):
        self.browser.quit()

    def test_e2e_add_and_remove_wishlist(self):
        self.browser.get(f"{self.live_server_url}/users/login/")
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.user.username)
        self.browser.find_element(By.NAME, "password").send_keys("nciuw78432rjidscn923r")
        self.browser.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]").click()

        self.wait.until(EC.url_contains("/library/"))

        book_card_xpath = f"//div[contains(., '{self.book.title}')]"
        book_card = self.wait.until(EC.presence_of_element_located((By.XPATH, book_card_xpath)))

        add_link = book_card.find_element(By.XPATH, ".//a[contains(text(),'Adicionar')]")
        add_link.click()

        self.assertTrue(Wishlist.objects.filter(user=self.user, book=self.book).exists())

        self.browser.get(f"{self.live_server_url}/library/lista-de-desejos/")

        wishlist_card = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(., '{self.book.title}')]"))
        )

        remove_link = wishlist_card.find_element(By.XPATH, ".//*[contains(text(),'Remover')]")
        remove_link.click()

        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, f"//div[contains(., '{self.book.title}')]"))
        )

        self.assertFalse(Wishlist.objects.filter(user=self.user, book=self.book).exists())
