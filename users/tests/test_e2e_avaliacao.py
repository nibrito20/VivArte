from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from library.models import Book

class SubmitReviewE2ETest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.browser.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.book = Book.objects.create(title="Livro de Teste", slug="livro-de-teste")

    def test_e2e_submit_review(self):
        self.browser.get(f'{self.live_server_url}/users/login/')
        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password").send_keys("password")
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        self.browser.get(f'{self.live_server_url}/library/{self.book.slug}/submit_review/')
        self.browser.execute_script("""
            fetch('', {
                method: 'POST',
                headers: {'X-CSRFToken': document.cookie.match('csrftoken=([^;]+)')[1]},
                body: new URLSearchParams({
                    'subject': 'Incrível leitura!',
                    'review': 'Gostei muito deste livro, super recomendo!',
                    'rating': '5'
                })
            });
        """)

        self.assertTrue(Book.objects.filter(pk=self.book.pk).exists())