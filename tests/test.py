import unittest
from customer import Customer
from restaurant import Restaurant
from review import Review


class TestRestaurantReviews(unittest.TestCase):

    def setUp(self):
        
        self.customer1 = Customer("John", "Doe")
        self.customer2 = Customer("Jane", "Smith")
        self.restaurant1 = Restaurant("Sample Restaurant")
        self.restaurant2 = Restaurant("Another Restaurant")
        self.review1 = Review(self.customer1, self.restaurant1, 4)
        self.review2 = Review(self.customer2, self.restaurant1, 5)
        self.review3 = Review(self.customer1, self.restaurant2, 3)

    def test_customer_methods(self):
        self.assertEqual(self.customer1.full_name(), "John Doe")
        self.assertEqual(self.customer2.given_name, "Jane")
        self.assertEqual(self.customer1.family_name, "Doe")

    def test_restaurant_methods(self):
        self.assertEqual(self.restaurant1.name, "Sample Restaurant")
        self.assertEqual(self.restaurant2.reviews, [])  # Assuming reviews is a list

    def test_review_methods(self):
        self.assertEqual(self.review1.rating, 4)
        self.assertEqual(self.review2.customer, self.customer2)
        self.assertEqual(self.review3.restaurant, self.restaurant2)

    def test_object_relationship_methods(self):
        self.assertEqual(self.review1.customer(), self.customer1)
        self.assertEqual(self.review2.restaurant(), self.restaurant1)
        self.assertEqual(self.restaurant1.customers(), [self.customer1, self.customer2])
        self.assertEqual(self.customer1.restaurants(), [self.restaurant1, self.restaurant2])

    def test_aggregate_association_methods(self):
        self.assertEqual(self.customer1.num_reviews(), 2)
        self.assertEqual(Customer.find_by_name("Jane Smith"), self.customer2)
        self.assertEqual(Customer.find_all_by_given_name("John"), [self.customer1])


if __name__ == '__main__':
    unittest.main()
