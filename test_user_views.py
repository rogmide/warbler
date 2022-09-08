import os
from unittest import TestCase
from models import db, connect_db, Message, User, Likes, Follows

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

from app import app

db.create_all()


class UserViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        self.user1 = User.signup("user1", "user1@test.com", "123456", None)
        self.user2 = User.signup("user2", "user2@test.com", "123456", None)
        self.user3 = User.signup("user3", "user3@test.com", "123456", None)
        
        db.session.commit()

    def tearDown(self):

        db.session.rollback()

    def test_users(self):
        with app.test_client() as client:
            resp = client.get("/users")

            self.assertIn("@user1", str(resp.data))
            self.assertIn("@user2", str(resp.data))
            self.assertIn("@user3", str(resp.data))
    
    # def test_show_user(self):
    #     with app.test_client() as client:
    #         resp = client.get(f"/users/")

    #         self.assertEqual(resp.status_code, 200)
    #         # self.assertIn("@user1", str(resp.data))
