from locust import task, between, TaskSet, User, HttpUser
from extract_logs import markov_chain
from client import SocialMediaClient
import random

ENDPOINTS = {
    "/feed": "view_feed",
    "/like/:id": "like_post",
    "/profile/:id": "view_profile",
    "/follow/:id": "follow_user",
    "/post": "create_post"
}

# permet de déterminer quel endpoint arrive generalement après un endpoint
class MarkovUser(TaskSet):
    def on_start(self):
        self.social_media_client = SocialMediaClient(self.client)
        self.social_media_client.login()
        self.current_state = "/feed"
    @task
    def perform_api(self):
        if self.current_state in markov_chain:
            transitions = markov_chain[self.current_state]
            next_endpoint = random.choices(
                list(transitions.keys()),
                weights=list(transitions.values())
            )[0]

        if next_endpoint in ENDPOINTS:
            method_name = ENDPOINTS[next_endpoint]
            getattr(self.social_media_client, method_name)()

        self.current_state = next_endpoint


class MarkovSocialMediaUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [MarkovUser]