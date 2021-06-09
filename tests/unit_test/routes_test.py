from tests.Base_test import BaseTest

class TestRoutes(BaseTest):
    def test_loading_page(self):
        with self.app:
            response = self.app.get('/home', content_type='html/text')
            self.assertEqual(response.status_code, 200)

    def test_market_page(self):
        with self.app:
            response = self.app.get('/market', content_type='html/text')
            self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        with self.app:
            data = self.app.get('/register')
            self.assertEqual(data.status_code, 200)

    def test_login_page(self):
        with self.app:
            data = self.app.get('/login', content_type='html/text')
            self.assertEqual(data.status_code, 200)