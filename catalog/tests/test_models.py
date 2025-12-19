
from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):




    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='John', last_name='Doe')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name(self):
        author = Author.objects.get(id=1)
        expected_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_name)



        
