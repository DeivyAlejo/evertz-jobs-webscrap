import requests
from bs4 import BeautifulSoup

url = "https://evertz.com/contact/careers/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# print(soup)

pagination = soup.find(id="job_paginate")

print(pagination)

# if class is "d-none" there is not pagination. 
# if class is empty there is pagination


# def main():
#     print("Hello from evertz-jobs-webscrap!")


# if __name__ == "__main__":
#     main()
