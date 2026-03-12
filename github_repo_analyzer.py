import requests
from collections import Counter


def analyze_repos(username):

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    if response.status_code != 200:
        print("User not found")
        return

    repos = response.json()

    repo_count = len(repos)

    stars = sum(repo["stargazers_count"] for repo in repos)

    languages = [repo["language"] for repo in repos if repo["language"]]

    language_counter = Counter(languages)

    most_used_language = None

    if language_counter:
        most_used_language = language_counter.most_common(1)[0][0]

    print("\nGitHub Repo Analysis")
    print("--------------------")

    print("Username:", username)
    print("Total repos:", repo_count)
    print("Total stars:", stars)

    if most_used_language:
        print("Most used language:", most_used_language)

    print("\nRepo list:")

    for repo in repos:
        print("-", repo["name"])


if __name__ == "__main__":

    username = input("Enter GitHub username: ")

    analyze_repos(username)