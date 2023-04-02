from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def hello(self):
        self.client.get("/hello")

        # example of a POST request to "/hello" endpoint
        # replace "{name}" with an actual name
        self.client.post("/hello", data={"name": "{name}"})

