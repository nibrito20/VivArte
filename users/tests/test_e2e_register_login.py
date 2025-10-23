from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.urls import reverse

class UserFlowE2ETest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        
        service = Service(r"C:\Users\jotaa\Downloads\edgedriver_win64 (1)\msedgedriver.exe")
        self.browser = webdriver.Edge(service=service, options=options)
        
        self.user = User.objects.create_user(username='joaopfdias', password='SAOaloGGO123', email='joaopfdias@example.com')

    def tearDown(self):
        self.browser.quit()

    def test_usuario_pode_registrar_e_fazer_login(self):
        self.browser.get(self.live_server_url + reverse('users:register'))

        username_input = self.browser.find_element(By.NAME, 'username')
        email_input = self.browser.find_element(By.NAME, 'email')
        password_input = self.browser.find_element(By.NAME, 'password1')
        confirm_password_input = self.browser.find_element(By.NAME, 'password2')

        username_input.send_keys('joaopfdias')
        email_input.send_keys('joaopfdias@example.com')
        password_input.send_keys('SAOaloGGO123')
        confirm_password_input.send_keys('SAOaloGGO123')

        confirm_password_input.send_keys(Keys.RETURN)

        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'Entrar')))

        self.browser.get(self.live_server_url + reverse('users:login'))

        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')

        username_input.send_keys('joaopfdias')
        password_input.send_keys('SAOaloGGO123')

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        print("Current URL após login:", self.browser.current_url)

        page_source = self.browser.page_source
        print(page_source)

        try:
            sair_button = WebDriverWait(self.browser, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.nav-button'))
            )

            self.assertTrue(sair_button.is_displayed())
            self.assertTrue(sair_button.is_enabled())

            self.assertIn('Sair', page_source)
            self.assertNotIn('Entrar', page_source)

        except Exception as e:
            print("Erro ao tentar acessar o botão Sair após o login.")
            raise e