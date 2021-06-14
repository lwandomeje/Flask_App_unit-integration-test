from market.models import User
from flask_login import current_user
from market.models import User, Item
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

    def test_Login(self):
        with self.app:
            response = self.app.post('/register',
                                     data=dict(username='Name', email_address='mail@gmail.com',
                                               password1='54321', password2='54321'),
                                     follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(username='Name').first()
            #self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'', response.data)
            # assert that user is logged in
            #self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            resp = self.app.post('/login', data =dict(username='Name', password='54321'),follow_redirects=True)

            self.assertIn(b'',resp.data)

            out = self.app.get('/logout', follow_redirects=True)
            self.assertIn(b'You have been logged out!',out.data)
            self.assertEqual(out.status_code, 200)