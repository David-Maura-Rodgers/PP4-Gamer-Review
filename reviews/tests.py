from django.test import TestCase


class TestViews(TestCase):
    """
    Test home page for review app
    """
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
