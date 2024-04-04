import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
<<<<<<< HEAD
        self.assertEqual(b'{ "imie": "Yua", "msg": "Hello World!"}', rv.data)
=======
        self.assertEqual(b'{ "imie":"Via", "msg":"Hello World!"}', rv.data)
>>>>>>> bd593701c4aa38065ef4f995dd01ead146842707
