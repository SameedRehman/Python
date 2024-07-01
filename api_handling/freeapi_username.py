import requests

def fetch_random_user_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    reponse = requests.get(url)
    data = reponse.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data ["login"]["username"]
        country = user_data ["location"]["country"]
        return username , country
    else:
        raise Exception ("Failed to fetch data")

def main():
    try:
        username,country =fetch_random_user_api()
        print(f"Username:{username} \ncountry:{country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()