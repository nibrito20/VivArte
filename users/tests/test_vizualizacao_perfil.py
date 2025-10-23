from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
from django.test import Client

class VisualizarPerfilTest(StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='joaopfdias',
            first_name='joao',
            last_name='dias',
            email='jpfd@cesar.school',
            password='senha123'
        )

        self.browser = webdriver.Edge()
        self.browser.implicitly_wait(5)

        self.client = Client()
        self.client.login(username='joaopfdias', password='senha123')

        self.browser.get(self.live_server_url)
        for key, value in self.client.cookies.items():
            cookie = {
                'name': key,
                'value': value.value,
                'path': '/',
            }
            self.browser.add_cookie(cookie)

    def tearDown(self):
        self.browser.quit()

    def test_visualizar_informacoes_perfil(self):
        self.browser.get(self.live_server_url + "/users/account/")

        wait = WebDriverWait(self.browser, 10)

        nome = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{self.user.first_name}')]")
        ))

        sobrenome = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{self.user.last_name}')]")
        ))

        email = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{self.user.email}')]")
        ))

        self.assertTrue(nome.is_displayed())
        self.assertTrue(sobrenome.is_displayed())
        self.assertTrue(email.is_displayed())