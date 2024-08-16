import unittest
from peewee import *

from app import TimelinePost

MODELS=[TimelinePost]

test_db=SqliteDatabase(':memory:')

#test the TimelinePost model.
class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind models to the test database and connect
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()

        # Create tables
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Drop tables and close the database connection
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        # Create posts
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content="Hello world, I'm John!")
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content="Hello world, I'm Jane!")

        # Assertions for first post
        assert first_post.id == 1
        assert first_post.name == 'John Doe'
        assert first_post.email == 'john@example.com'
        assert first_post.content == "Hello world, I'm John!"
        assert first_post.created_at is not None
 
        # Assertions for second post
        assert second_post.id == 2
        assert second_post.name == 'Jane Doe'
        assert second_post.email == 'jane@example.com'
        assert second_post.content == "Hello world, I'm Jane!"
        assert second_post.created_at is not None