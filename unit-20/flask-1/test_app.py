from unittest import TestCase
from app import app


class ForexIndexTests(TestCase):
    def test_index(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Currency Converter', html)
            

    def test_conversion(self):
        with app.test_client() as client:
            resp = client.post('/convert', data={'convert-from': 'USD', 'convert-to': 'USD', 'amount': '100'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('100', html)
            self.assertIn('USD', html)
