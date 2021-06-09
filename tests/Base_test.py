from unittest import TestCase
from market import app
from market.models import db


class BaseTest(TestCase):
    def setUp(self):
        # test database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context()

