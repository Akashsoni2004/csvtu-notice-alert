import requests
from bs4 import BeautifulSoup

print("Checking notices...")

URL = "https://csvtu.ac.in/ew/notices/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find latest notice
notice_div = soup.find("div", class_="news")

notice_id = notice_div["id"].replace("post-", "")

notice_link = notice_div.find("a")["href"]

notice_title = notice_div.find("a").text.strip()

print(notice_id)
print(notice_title)
print(notice_link)

# if notice:
#     title = notice.text.strip()
#     link = notice["href"]
    
#     current_notice = title + "\n" + link

# else:
#     print("Notice not found")


# # Read old notice
# try:
#     with open("last_notice.txt", "r") as file:
#         old_notice = file.read()
# except:
#     old_notice=""

# if current_notice != old_notice:
#     send_email(
#         "📢 New CSVTU Notice",
#         f"{title}\n\n{link}"
#     )

#     with open("last_notice.txt", "w") as file:
#         file.write(current_notice)

# else:
#     print("No new notice.")