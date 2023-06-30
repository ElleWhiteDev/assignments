from unittest import TestCase
from app import app



class ForexValidationTests(TestCase):
    def test_convert_invalid_amount(self):
        with app.test_client() as client:
            resp = client.post(
                '/convert',
                data={
                    'convert-from': 'USD',
                    'convert-to': 'USD',
                    'amount': '-100'
                },
                follow_redirects=True
            )
            self.assertEqual(resp.status_code, 200)
            self.assertIn(b'Invalid amount', resp.data)
            

    def test_round_decimal(self):
        with app.test_client() as client:
            resp = client.post(
                '/convert',
                data={
                    'convert-from': 'USD',
                    'convert-to': 'USD',
                    'amount': '100.23341'
                },
                follow_redirects=True
            )
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('100.23', html)


    def test_convert_invalid_currency_from(self):
        with app.test_client() as client:
            try:
                client.post(
                    '/convert',
                    data={'convert-from': 'ABC', 'convert-to': 'USD', 'amount': '100'},
                    follow_redirects=True)
            except ValueError as e:
                self.assertEqual(str(e), "Invalid currency code")
                

    def test_convert_invalid_currency_to(self):
        with app.test_client() as client:
            try:
                client.post(
                    '/convert', 
                    data={'convert-from': 'USD', 'convert-to': 'ABC', 'amount': '100'}, 
                    follow_redirects=True)
            except ValueError as e:
                self.assertEqual(str(e), "Invalid currency code")
