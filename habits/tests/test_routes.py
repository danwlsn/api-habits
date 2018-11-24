import unittest

from flask import Flask

from habits import db, app
from habits.routes import index, list_habits
from habits.models import Habit


class RoutesTest(unittest.TestCase):
    def populate_db(self):
        habits = [
            'Do this',
            'Do that',
            'Clean up todo comments'
        ]
        for habit in habits:
            h = Habit(title=habit)
            db.session.add(h)
            db.session.commit()
        pass

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_index_route(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b'Hello, World!')

