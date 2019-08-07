from .index_tag import index
from django.test import TestCase

class TestViews(TestCase):
    
    def test_index_tag(self):
        sequence = [1,2,3,4,5,6,7]
        position = 1
        self.assertEqual(index(sequence, position), [1,2,3])