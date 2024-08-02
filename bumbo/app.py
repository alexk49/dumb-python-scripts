from api import API


app = API()


@app.route("/home")
def home(request, response):
    response.text = "hello from the home page"


@app.route("/about")
def about(request, response):
    response.text = "hello from the about page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"hello {name}"


@app.route("/tell/{age}")
def tell(request, response, age):
    response.text = f"you are this years old: {age}"


@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "books page"
