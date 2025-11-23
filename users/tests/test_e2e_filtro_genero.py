from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library.models import Book, Genre

class BookFilterE2ETest(LiveServerTestCase):
    def setUp(self):
        self.acao = Genre.objects.create(name="Ação", slug="acao")
        self.romance = Genre.objects.create(name="Romance", slug="romance")

        self.book_acao = Book.objects.create(
            title="Missão Secreta",
            details="Livro de ação",
            slug="missao-secreta"
        )
        self.book_acao.generos.add(self.acao)

        self.book_romance = Book.objects.create(
            title="Amor Eterno",
            details="Livro de romance",
            slug="amor-eterno"
        )
        self.book_romance.generos.add(self.romance)

        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="nciuw78432rjidscn923r"
        )

        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 15)

    def tearDown(self):
        self.browser.quit()

    def test_filter_books_by_genre(self):
        self.browser.get(f"{self.live_server_url}/users/login/")
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.user.username)
        self.browser.find_element(By.NAME, "password").send_keys("nciuw78432rjidscn923r")
        self.browser.find_element(By.XPATH, "//button[contains(text(),'Entrar')]").click()

        self.wait.until(EC.url_contains("/library/"))

        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{self.book_acao.title}')]")))
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{self.book_romance.title}')]")))

        self.browser.find_element(By.LINK_TEXT, "Romance").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{self.book_romance.title}')]")))
        
        acao_elements = self.browser.find_elements(By.XPATH, f"//*[contains(text(), '{self.book_acao.title}')]")
        self.assertEqual(len(acao_elements), 0)

        self.browser.find_element(By.LINK_TEXT, "Ação").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{self.book_acao.title}')]")))
        
        romance_elements = self.browser.find_elements(By.XPATH, f"//*[contains(text(), '{self.book_romance.title}')]")
        self.assertEqual(len(romance_elements), 0)