import requests

username = input("Enter GitHub username: ")

user_url = f"https://api.github.com/users/{username}"
repo_url = f"https://api.github.com/users/{username}/repos"

user = requests.get(user_url).json()
repos = requests.get(repo_url).json()

repo_list = ""

for repo in repos:
    repo_list += f"<li>{repo['name']}</li>"

html = f"""
<html>
<head>
<title>GitHub Dashboard</title>
</head>

<body>

<h1>GitHub Profile Dashboard</h1>

<h2>{user['login']}</h2>

<p>Public repos: {user['public_repos']}</p>
<p>Followers: {user['followers']}</p>

<h3>Repositories</h3>

<ul>
{repo_list}
</ul>

</body>
</html>
"""

with open("dashboard.html","w",encoding="utf-8") as f:
    f.write(html)

print("Dashboard created: dashboard.html")