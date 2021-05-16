from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app,db
from application.models import Team, Players

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() 

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestHomepage(TestBase):
    def test_homepage(self):
        self.driver.get(f"http://localhost:{self.TEST_PORT}")
        fantasy_teams_title = self.driver.find_element_by_xpath('/html/body/h2').text
        self.assertIn('Fantasy Teams', fantasy_teams_title)

class TestAddTeam(TestBase):
    TEST_CASES = [("Manchester United","Premier League"), ("Real Madrid","La Liga"), ("Liverpool","Premier League")]
   
    def submit_input(self, name, league):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="league"]').send_keys(league)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

class TestAddPlayer(TestBase):
    TEST_CASES = [("Wayne Rooney", "English", "ST"), ("Joe Hart", "English", "GK"), ("Lionel Messi", "Argentinian", "RW")]

    def submit_input(self, name, nationality, position):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="league"]').send_keys(nationality)
        self.driver.find_element_by_xpath('//*[@id="league"]').send_keys(position)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()