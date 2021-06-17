from market.models import User, Item
from market import db
from tests.Base_test import BaseTest

class TestAllModels(BaseTest):
    def testing_user_is_created(self):
        new_user = User(id =0,
                        username='Name',
                        email_address='mail@gmail.com',
                        password_hash='54321',
                        budget=1000,
        )
        self.assertEqual(new_user.id, 0)
        self.assertAlmostEqual(new_user.password_hash,'54321')
        self.assertEqual(new_user.username, 'Name')
        self.assertEqual(new_user.email_address, 'mail@gmail.com')
        self.assertEqual(new_user.budget, 1000)


    def testing_Items(self):
     new_user = Item(id=0,
                        name='Name',
                        price=100,
                        barcode='908070',
                        description='Good',
                        owner =1000
                        )
     self.assertEqual(new_user.id, 0)
     self.assertEqual(new_user.name, 'Name')
     self.assertAlmostEqual(new_user.price, 100)
     self.assertEqual(new_user.barcode,'908070')
     self.assertEqual(new_user.description,'Good')
     self.assertEqual(new_user.owner, 1000)

    def testing_item_repr_method(self):
        item = Item(name='Phone', price=300, barcode='2020abc', description='New')

        new_item = item.__repr__()

        self.assertEqual(new_item, 'Phone')


    def testing_item_sell_method(self):
        user = User(id=1, username='lwando', email_address='mr.meje@gmail.com', password_hash='123456', budget=3000)
        item = Item(name='Phone', price=1500, barcode='1010xuz', description='oldPhone', owner=1)
        can_sell = item.sell(user)
        db.session.commit()
        self.assertIsNone(can_sell)

    def testing_item_buy_method(self):
        user = User(id=2, username='lwando', email_address='mr.meje@gmail.com', password_hash='123456', budget=3000)
        item = Item(name='Phone', price=5000, barcode='2020xyz', description='new', owner=1)
        buy = item.buy(user)
        db.session.commit()
        self.assertIsNone(buy)