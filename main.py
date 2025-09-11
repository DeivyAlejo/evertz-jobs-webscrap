import requests
from bs4 import BeautifulSoup
import json
import time

# Check out this other link: http://evertz.applytojob.com/apply/

url = "http://evertz.applytojob.com/apply/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
jobs = soup.find('ul', class_='list-group')
li_jobs = jobs.find_all(class_='list-group-item')

job_list = []

for li in li_jobs:
    h4 = li.find('h4')
    a_tag = h4.find('a')
    job_title = a_tag.get_text(strip=True)
    job_link = a_tag['href']
    inner_ul = li.find('ul')
    inner_li_items = inner_ul.find_all('li')
    details = [item.get_text(strip=True) for item in inner_li_items]

    if len(details) <2:
        details.append("")

    job_list.append({
            'Job name':job_title,
            'Location': details[0],
            'Department':details[1],
            'Link': job_link
        })

with open('jobs_new.json', 'w', encoding='utf-8') as f:
    json.dump(job_list, f, ensure_ascii=False, indent=4)

print("Job data saved to jobs.json")

# print(jobs)

# This code is for this url "https://evertz.com/contact/careers/"
# url = "https://evertz.com/contact/careers/"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# pagination = soup.find(id="job_paginate")

# multiple_pages = pagination.get("class")

# jobs = soup.find(id="job_results")

# li_jobs = jobs.find_all("li")


# # This is to extract all the listing when I know how to extract one. Do not delete this
# list_of_urls = []
# base_url = 'https://evertz.com/contact/careers/?page='
# if (not multiple_pages):
#     # print("Multiple pages")

#     li_items = pagination.find_all("li")

#     for li in li_items:
#         try:
#             page = int(li.get_text(strip=True))
#             list_of_urls.append(base_url+(str(page-1)))
#         except ValueError:
#             # Code that runs if an exception occurs
#             print("Something went wrong!")

#         # print(type(li.get_text))

# job_list = []

# for url in list_of_urls:
#     time.sleep(1)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     jobs = soup.find(id="job_results")
#     li_jobs = jobs.find_all("li")

#     print(url)

#     for li_job in li_jobs:
#         a_tag = li_job.find("a")
#         # print(a_tag)
#         a_id = a_tag.get('id')
#         job_name = a_tag.get_text(strip=True)
#         href_link = a_tag['href']
#         p_tag = li_job.find('p')
#         p_tag = str(p_tag)[3:-4]
#         details = p_tag.split("<br/>")

#         # print(f"ID: {a_id}")
#         # print(f"Job: {job_name}")
#         # print(type(details[0]))
#         # print(f"Department: {details[0]}")
#         # print(type(details[1]))
#         # print(f"Location: {details[1]}")
#         # print(f"Link: www.evertz.com{href_link}")
#         # print("-----------------------")
        

#         job_list.append({
#             'id':a_id,
#             'Job name':job_name,
#             'Department':details[0],
#             'Location': details[1],
#             'Link': 'www.evertz.com'+ href_link
#         })

# with open('jobs.json', 'w', encoding='utf-8') as f:
#     json.dump(job_list, f, ensure_ascii=False, indent=4)

# print("Job data saved to jobs.json")


# print(pagination.get("class"))

# if class is "d-none" there is not pagination. 
# if class is empty there is pagination


# def main():
#     print("Hello from evertz-jobs-webscrap!")


# if __name__ == "__main__":
#     main()
