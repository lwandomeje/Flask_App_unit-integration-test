from flask import request
from tests.Base_test import BaseTest
from market import db
from market.models import User, Item


class TestMarketRoute(BaseTest):
    def test_market_route_can_buy(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="lwando", email_address="meje@gmail.com",
                                                   password1="123456", password2="123456",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="meje@gmail.com").first()

                data = self.app.post('/login', data=dict(username="lwando", password="123456"), follow_redirects=True)

                self.assertIn(b'', data.data)

                market_post_request = self.app.post('/market', follow_redirects=True)
                self.assertTrue(market_post_request.status_code, 200)

                purchased_item1 = Item(id=1, name="New Product", price=200, barcode=1234567,
                                       description="water")

                self.assertTrue(purchased_item1, user)

    def test_market_route_can_sell(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(id=1, username="meje", email_address="lwando@gmail.com",
                                                   password1="666", password2="666",), follow_redirects=True)

                purchased_item = Item(id=1, name="milk", price=200, barcode=1234567,
                                      description="milk", owner=1)
                db.session.add(purchased_item)
                db.session.commit()

                self.assertTrue(purchased_item)
