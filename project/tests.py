from django.test import TestCase
from django.urls import reverse

from .models import Visit


class TestProject(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'project/index.html')

    def test_create_visit(self):
        self.client.post(reverse('home'), {
            'user_name': 'TEST_123'
        })

        self.assertEqual(Visit.objects.count(), 1)
        self.assertEqual(Visit.objects.first().name, 'TEST_123')