from unittest import TestCase
from market.models import User, Item
from market import db
from tests.Base_test import BaseTest

class TestAllModels(BaseTest):
    def test_user_is_created(self):
        new_user = User(id =0,
                        username='Name',
                        email_address='mail@gmail.com',
                        password_hash='54321',
                        budget=1000,
        )
        self.assertEqual(new_user.id,0)
        self.assertAlmostEqual(new_user.password_hash,'54321')
        self.assertEqual(new_user.username, 'Name')
        self.assertEqual(new_user.email_address, 'mail@gmail.com')
        self.assertEqual(new_user.budget,1000)