import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category

class TestCart(unittest.TestCase):
    def test_add_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Star Wars", "Sci-Fi", "George Lucas", 19.95)
        self.assertTrue(cart.add_dvd(dvd))
        self.assertEqual(len(cart.items), 1)
    def test_discount(self):
            cart = Cart()
            cart.add_dvd(DigitalVideoDisc("Movie", "Action", "Director", cost=100.0))
            # Giảm 20% của 100 phải còn 80
            self.assertEqual(cart.apply_discount(20), 80.0)
            # Giảm quá 100% phải ném lỗi ValueError
            with self.assertRaises(ValueError):
                cart.apply_discount(150)
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa đầu tiên -> kết quả phải thành công (True)
        for i in range(20):
            dvd = DigitalVideoDisc(f"Title {i}", "Category", "Director", 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        
        # Thêm đĩa thứ 21 -> phải từ chối (False)
        dvd_21 = DigitalVideoDisc("Title 21", "Category", "Director", 10.0)
        self.assertFalse(cart.add_dvd(dvd_21))
    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("D1", "Cat", "Dir", cost=10.0))
        cart.add_dvd(DigitalVideoDisc("D2", "Cat", "Dir", cost=20.5))
        self.assertAlmostEqual(cart.total_cost(), 30.5)

    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("D1", "Cat", "Dir", 10.0))
        cart.add_dvd(DigitalVideoDisc("d4", "Cat", "Dir", 10.0))
        cart.add_dvd(DigitalVideoDisc("D3", "Cat", "Dir", 10.0))
        cart.add_dvd(DigitalVideoDisc("D2", "Cat", "Dir", 10.0))

        cart.sort_by_title()
        titles = [dvd.title for dvd in cart.items]
        self.assertEqual(titles, ["D1", "D2", "D3", "d4"])

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("D1", "Cat", "Dir", cost=25.0))
        cart.add_dvd(DigitalVideoDisc("D2", "Cat", "Dir", cost=10.5))
        cart.add_dvd(DigitalVideoDisc("D3", "Cat", "Dir", cost=50.0))
        cart.add_dvd(DigitalVideoDisc("D4", "Cat", "Dir", cost=15.0))

        cart.sort_by_cost()
        costs = [dvd.cost for dvd in cart.items]
        self.assertEqual(costs, [10.5, 15.0, 25.0, 50.0])

    def test_search_by_category(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("D1", "Cat", "Dir"))
        cart.add_dvd(DigitalVideoDisc("D2", "Dog", "Dir"))
        cart.add_dvd(DigitalVideoDisc("D3", "Cat", "Dir"))
        cart.add_dvd(DigitalVideoDisc("D4", "Dog", "Dir"))
        cart.add_dvd(DigitalVideoDisc("D5", "Cat", "Dir"))
        cart.add_dvd(DigitalVideoDisc("D6", "Cat", "Dir"))
        cart.add_dvd(DigitalVideoDisc("D7", "Cat", "Dir"))
        cart.add_dvd(DigitalVideoDisc("D8", "Chicken", "Dir"))
        matched = search_by_category(cart, "Cat")
        self.assertEqual(matched, [dvd for dvd in cart.items if dvd.category == 'Cat'])


if __name__ == "__main__":
    unittest.main()