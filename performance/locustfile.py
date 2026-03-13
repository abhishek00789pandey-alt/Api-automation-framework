from locust import HttpUser, task, between

class UserLoadTest(HttpUser):

    wait_time = between(1, 3)

    @task
    def get_users(self):

        response = self.client.get("/users")

        if response.status_code != 200:
            print("API Failed")