from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def hello(self):
        self.client.get("/hello")

        self.client.post("/hello", data={"name": "{name}"})

