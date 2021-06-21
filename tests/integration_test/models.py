from tests.Base_test import BaseTest
from market.models import Item, User
from market import db


class TestModels(BaseTest):
    def test_user(self):
        with self.app_context:
            user = User(username='lwando', email_address='testing@gmail.com', password_hash='12345')

            result = db.session.query(User).filter_by(username='lwando').first()
            self.assertIsNone(result)

            db.session.add(user)
            db.session.commit()

            result = db.session.query(User).filter_by(username='lwando').first()
            self.assertIsNotNone(result)
            # assert note in db.session

            db.session.delete(user)
            db.session.commit()

            result = db.session.query(User).filter_by(username='lwando').first()
            self.assertIsNone(result)

    def test_item(self):
        with self.app_context:
            item = Item(name='water', price=20, barcode='0102water', description='test')

            result = db.session.query(Item).filter_by(name='water').first()
            self.assertIsNone(result)

            db.session.add(item)
            db.session.commit()

            result = db.session.query(Item).filter_by(name='water').first()
            self.assertIsNotNone(result)
            # assert note in db.session

            db.session.delete(item)
            db.session.commit()

            result = db.session.query(Item).filter_by(name='water').first()
            self.assertIsNone(result)