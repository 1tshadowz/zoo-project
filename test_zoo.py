import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_Invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(1), 50)
        self.assertEqual(self.zoo.get_ticket_price(11), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    def test_Teen_ticket_price(self):    
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(14), 100)
        self.assertEqual(self.zoo.get_ticket_price(19), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
        
    def test_Adult_ticket_price(self):    
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(22), 150)
        self.assertEqual(self.zoo.get_ticket_price(59), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
        
    def test_Elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)


if __name__ == '__main__':
    unittest.main()
