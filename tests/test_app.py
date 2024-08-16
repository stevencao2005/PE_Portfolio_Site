import unittest
import json
import os
os.environ['TESTING'] = 'true'

from app import app

#test the application routes.
class AppTestCase(unittest.TestCase):
    def setUp(self):

        # creates a test client to mimic a web browser's behavior (simulate, test, analyze responses to HTTP requests)
        self.client = app.test_client()
 
    def test_home(self):
        # verifies that the home page loads correctly and contains specific HTML elements.
        response = self.client.get('/')
        assert response.status_code == 200
        html     = response.get_data(as_text=True)

        assert '<title>Steven Cao</title>' in html
        assert '<h1>Steven Cao</h1>' in html
        assert '<img src="./static/img/profile_pic.jpg">' in html

    def test_timeline(self):
        # tests the timeline post API, ensure that posts can be created and retrieved as expected
        
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # creates a new timeline post
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == "John Doe"
        assert json["email"] == "john@example.com"
        assert json["content"] == "Hello world, I'm John!"
        assert json["id"] == 1

        # check if the post was successfully created and can be retrieved
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == "John Doe"
        assert json["timeline_posts"][0]["email"] == "john@example.com"
        assert json["timeline_posts"][0]["content"] == "Hello world, I'm John!"
        assert json["timeline_posts"][0]["id"] == 1

    def test_malformed_timeline_post(self):
        # Tests the timeline post API with invalid data to ensure proper error handling and validation.
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        d = response.get_json()
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
        
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

