import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 19.95)
        self.dvd2 = DigitalVideoDisc("Star Wars", "Sci-Fi", "George Lucas", 24.95)
        self.dvd3 = DigitalVideoDisc("Aladdin", "Animation", "John Musker", 18.99)
        self.cart.add_dvd(self.dvd1)
        self.cart.add_dvd(self.dvd2)
        self.cart.add_dvd(self.dvd3)

    def test_search_by_title_exact(self):
        results = search_by_title(self.cart, "Star Wars")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Star Wars")

    def test_search_by_title_case_insensitive(self):
        results_lower = search_by_title(self.cart, "lion")
        self.assertEqual(len(results_lower), 1)
        self.assertEqual(results_lower[0].title, "The Lion King")

        results_upper = search_by_title(self.cart, "ALADDIN")
        self.assertEqual(len(results_upper), 1)
        self.assertEqual(results_upper[0].title, "Aladdin")

    def test_search_by_title_not_found(self):
        results = search_by_title(self.cart, "Avengers")
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()