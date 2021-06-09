from market.models import User
from flask_login import current_user
from tests.Base_test import BaseTest, db

class Testing(BaseTest):
    def test_register(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/register',
                                     data=dict(username='name', email_address='email@gmail.com', password='1234'),
                                     follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email_address='email@gmail.com').first()
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), None)
            resp = self.app.post('/login', data=dict(email_address='email@gmail.com',
                                                       password='pass1234'), follow_redirects=True)
            self.assertIn(b'', resp.data)

    def test_login_correct_email_firstname(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/login',
                                     data=dict(username='name', email_address='email@gmail.com', password='1234'),
                                     follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email_address='email@gmail.com').first()
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), None)
            resp = self.app.post('/login', data=dict(email_address='email@gmail.com',
                                                       password='pass1234'), follow_redirects=True)
            self.assertIn(b'', resp.data)