import unittest

from app import process_input

 

class TestApp(unittest.TestCase):

   def setUp(self):
       self.a = 10
       self.b = 5

   def test_0010_add(self):

       result = process_input(self.a, self.b, "add")
       self.assertEqual(result, 15)

def suite():

   suite = unittest.TestSuite()
   suite.addTests(
       unittest.TestLoader().loadTestsFromTestCase(TestApp)
   )
   return suite


if __name__ == '__main__':
    print("HelloW!")
    unittest.TextTestRunner(verbosity=2).run(suite())