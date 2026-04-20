from locust import task, between, TaskSet, User, HttpUser
from extract_logs import endpoint_counts
from client import SocialMediaClient
import random

ENDPOINTS = {
"/feed" : "view_feed",
"/like/:id" : "like_post",
"/profile/:id" : "view_profile",
"/follow/:id" : "follow_user",
"/post" : "create_post"
}

class GlobalUser(TaskSet):
    def on_start(self):
        self.social_media_client = SocialMediaClient(self.client)
        self.social_media_client.login()

        total = 0
        self.dict = {}
        for endpoint in ENDPOINTS:
            if endpoint in endpoint_counts:
                total += endpoint_counts[endpoint]

        for endpoint in ENDPOINTS:
            if endpoint in endpoint_counts:
                self.dict[endpoint] = endpoint_counts[endpoint]/total

    @task
    def perform_api(self):
        endpoint = random.choices( list(self.dict.keys()), weights=list(self.dict.values()))[0]
        method_name = ENDPOINTS[endpoint]
        getattr(self.social_media_client, method_name)()


class GlobalSocialMediaUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [GlobalUser]