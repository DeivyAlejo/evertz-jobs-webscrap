import requests
from bs4 import BeautifulSoup

url = "https://evertz.com/contact/careers/"

response = requests.get(url)

html = '''
<ul class="no-marker ps-0" id="job_results">
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250707192319_IESJHVVVDJL5XLCW" id="job_20250707192319_IESJHVVVDJL5XLCW">Administrative Assistant (Entry Level)</a></h6>
<p>Administration<br/>Burlington, ON, Canada</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250708134504_JLMCGYSBMHJJNGOM" id="job_20250708134504_JLMCGYSBMHJJNGOM">Broadcast Engineer - Pittsburgh</a></h6>
<p><br/>Indiana/Pittsburgh, PA, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250708152218_ISSNNDNKR2ULGOIF" id="job_20250708152218_ISSNNDNKR2ULGOIF">Broadcast Engineer, Burbank, California</a></h6>
<p>Technical Support<br/>Burbank, CA, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250708135025_VWACJLG6LNGLUANH" id="job_20250708135025_VWACJLG6LNGLUANH">Broadcast Engineer, Long Island, New York</a></h6>
<p>Technical Support<br/>Hauppauge, Long Island, NY, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250708135613_ML1MT6WWEVAZ8P2T" id="job_20250708135613_ML1MT6WWEVAZ8P2T">Broadcast Engineer, New York</a></h6>
<p>USA<br/>New York, NY, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250707174812_RJPZM5VMZCR3Q9QB" id="job_20250707174812_RJPZM5VMZCR3Q9QB">Customer Order Coordinator</a></h6>
<p>Administration<br/>Burlington, ON, Canada</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250414173001_RCN7CXAL6JESOPCM" id="job_20250414173001_RCN7CXAL6JESOPCM">DSP Engineer</a></h6>
<p><br/>Pittsburgh, PA, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250630123406_AQCRWBX3Y2DC5JGJ" id="job_20250630123406_AQCRWBX3Y2DC5JGJ">Electronics Manufacturing Inspector - Evertz USA</a></h6>
<p>SMT<br/>Indiana, PA, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250630123156_AIE6ONWLKZEDNYCR" id="job_20250630123156_AIE6ONWLKZEDNYCR">Electronics Manufacturing Operator, Evertz USA</a></h6>
<p>SMT<br/>Indiana, PA, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250630123231_VFNCKKYPRT6S0SX2" id="job_20250630123231_VFNCKKYPRT6S0SX2">Electronics Manufacturing Programmer, Evertz USA</a></h6>
<p>SMT<br/>Indiana, PA, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250331131622_BYLKABUIWLDIYNNQ" id="job_20250331131622_BYLKABUIWLDIYNNQ">Embedded Software Engineer - Pittsburgh</a></h6>
<p>R&amp;D<br/>Pittsburgh, PA, United States</p>
</li>
<li class="mb-3 pb-3 border-bottom border-1 border-secondary no-replace">
<h6><a data-bs-target="#modalJobDetails" data-bs-toggle="modal" href="/contact/careers/job_20250127165234_MHKMCENYRVQELPNR" id="job_20250127165234_MHKMCENYRVQELPNR">Enterprise Support Engineer</a></h6>
<p><br/>Warsaw, Poland</p>
</li>
</ul>
'''

# soup = BeautifulSoup(html, "html.parser")

# # print(soup)

# pagination = soup.find(id="job_paginate")

# # print(pagination)

# multiple_pages = pagination.get("class")

soup = BeautifulSoup(html, "html.parser")
jobs = soup.find(id="job_results")
# print(jobs)
li_jobs = jobs.find_all("li")

# li_job = li_jobs[12]
# a_tag = li_job.find("a")
# job_name = a_tag.get_text(strip=True)
# href_link = a_tag['href']
# p_tag = li_job.find('p')
# p_tag = str(p_tag)[3:-4]
# details = p_tag.split("<br/>")
# print(details)
for li_job in li_jobs:
    a_tag = li_job.find("a")
    # print(a_tag)
    job_name = a_tag.get_text(strip=True)
    href_link = a_tag['href']
    p_tag = li_job.find('p')
    p_tag = str(p_tag)[3:-4]
    details = p_tag.split("<br/>")

    print(f"Job: {job_name}")
    print(f"Department: {details[0]}")
    print(f"Location: {details[1]}")
    print("-----------------------")






# This is to extract all the listing when I know how to extract one. Do not delete this
# if (not multiple_pages):
#     # print("Multiple pages")

#     li_items = pagination.find_all("li")

#     for li in li_items:
#         print(li.get_text(strip=True))

# print(pagination.get("class"))

# if class is "d-none" there is not pagination. 
# if class is empty there is pagination


# def main():
#     print("Hello from evertz-jobs-webscrap!")


# if __name__ == "__main__":
#     main()
