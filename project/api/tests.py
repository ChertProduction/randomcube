from django.test import TestCase

from .models import Results
 
class ModelsTestCase(TestCase):
 
    def setUp(self):
          a1 = Results.objects.create(number=10, name='000')

    def test_first_name_max_length(self):
        name=Results.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEquals(max_length,100)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/randomizer')
        self.assertEqual(resp.status_code, 200)