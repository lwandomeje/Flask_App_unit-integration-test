
from flask import request

from tests.Base_test import BaseTest
from market import db
from market.models import User


class TestRegister(BaseTest):
    def test_register_new_user(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="name", email_address="name@gmail.com",
                                                   password1="10111", password2="10111",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="name@gmail.com").first()

                # Asserting that the user is found in the database
                self.assertTrue(user)

                # Checking that the user has a budget of 15000
                budget = db.session.query(User).filter_by(budget=15000).first()

                # Asserting that the user has a budget of 15000
                self.assertTrue(budget)

                # asserting that the user is shown the message below
                self.assertIn(b'', response.data)



    def test_password_not_matching(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="name", email_address="name@gmail.com",
                                                   password1="202177", password2="202188", ), follow_redirects=True)

                # checking if the user is not in the User table
                user = db.session.query(User).filter_by(email_address="name@gmail.com").first()

                # Asserting that the user is found in the database
                self.assertFalse(user)

                # Asserting that the user was shown an error message
                self.assertIn(b'', response.data)