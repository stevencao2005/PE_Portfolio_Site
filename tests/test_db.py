import unittest
from peewee import *

from app import TimelinePost

MODELS=[TimelinePost]

test_db=SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first=TimelinePost.create(name='Doe', email='doe@example.com', content='Hello')
        assert first.id==1
        second=TimelinePost.create(name='Jane', email='jane@example.com', content='Heya')
        assert second.id==2