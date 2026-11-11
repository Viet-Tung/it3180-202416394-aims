import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa đầu tiên -> kết quả phải thành công (True)
        for i in range(20):
            dvd = DigitalVideoDisc(f"Title {i}", "Category", "Director", 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        
        # Thêm đĩa thứ 21 -> phải từ chối (False)
        dvd_21 = DigitalVideoDisc("Title 21", "Category", "Director", 10.0)
        self.assertFalse(cart.add_dvd(dvd_21))

if __name__ == "__main__":
    unittest.main()