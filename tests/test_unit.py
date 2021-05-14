import unittest
import pytest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Team, Players

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED= False 
            )
        return app
    
    def setUp(self):
        db.create_all()
        test_team = Team(name = "Manchester United", league = "Premier League")
        db.session.add(test_team)
        db.session.commit()
        test_players = Players(name = "Wayne Rooney", nationality = "English", position = "CM")
        db.session.add(test_players)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
   
    def test_add_team_get(self):
        response = self.client.get(url_for('add_team'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_player_get(self):
        response = self.client.get(url_for('add_player', id=1))
        self.assertEqual(response.status_code, 200)
   
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects= True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_team(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Manchester United", response.data)
        self.assertIn(b"Premier League", response.data)

class TestAdd_Team(TestBase):
    def test_add_team_team(self):
        response = self.client.post(
            url_for("add_team"),
            data=dict(name = 'Bayern Munich', league = 'Bundesliga'), follow_redirects= True)
        self.assertIn(b"Bayern Munich", response.data)
        self.assertIn(b"Bundesliga", response.data)

class TestAdd_Player(TestBase):
    def test_add_player_team(self):
        response = self.client.post(
            url_for("add_player", id=1),
            data=dict(name = 'Wayne Rooney', position = 'ST'), follow_redirects= True)
        self.assertIn(b"Wayne Rooney", response.data)
        self.assertIn(b"ST", response.data)

class TestUpdate(TestBase):
    def test_update_team(self):
        response = self.client.post(
            url_for("update", id=1),
            data=dict(name = 'Real Madrid', league = 'La Liga'), follow_redirects= True)
        self.assertIn(b"Real Madrid", response.data)
        self.assertIn(b"La Liga", response.data)

class TestDelete(TestBase):
    def test_update_team(self):
        response = self.client.get(url_for("delete", id=1),follow_redirects= True)
        self.assertNotIn(b"Manchester United", response.data)
        self.assertNotIn(b"Premier League", response.data)






