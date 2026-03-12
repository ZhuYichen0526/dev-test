import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("User not found")
        return
    
    data = response.json()
    
    print("Username:", data["login"])
    print("Name:", data["name"])
    print("Public repos:", data["public_repos"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("Profile URL:", data["html_url"])


if __name__ == "__main__":
    
    username = input("Enter GitHub username: ")
    
    get_github_user(username)