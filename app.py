from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/")
def home():

    return """
    <h1>GitHub Dashboard</h1>

    <form action="/user">

    GitHub username:
    <input name="username">

    <button type="submit">Search</button>

    </form>
    """


@app.route("/user")
def user():

    username = request.args.get("username")

    url = f"https://api.github.com/users/{username}"

    user = requests.get(url).json()

    return f"""

    <h1>{user['login']}</h1>

    <p>Public repos: {user['public_repos']}</p>
    <p>Followers: {user['followers']}</p>

    """


app.run()