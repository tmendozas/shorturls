from django.test import TestCase
import random
from shorturls.app.helpers.encoder import encode,decode
# Create your tests here

class Encode(TestCase):
    
    def test_encoding(self):
        original = random.randint(0,1000000)
        encoded = encode(original)
        decoded = decode(encoded)
        self.assertEqual(original, decoded)