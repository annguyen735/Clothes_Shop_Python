from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTest(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('test@gmail.com', 'password')
        self.assertEqual(super_user.email, 'test@gmail.com')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_active)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user('test@gmail.com', 'password')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_user_fail(self):
        with self.assertRaises(ValueError):    
            get_user_model().objects.create_superuser('test', 'password')