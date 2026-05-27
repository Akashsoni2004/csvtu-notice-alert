import os

def check_notice():
    
    # for sending email
    import smtplib
    from email.mime.text import MIMEText

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    def send_email(subject, body):

        to_email = ["akashkrsoni2004@gmail.com"]
        cc_email = [
            "aditiverma00300@gmail.com", 
            "sinhajayanshi@gmail.com"
        ]

        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = ", ".join(to_email)
        msg["Cc"] = ", ".join(cc_email)

        recipients = to_email + cc_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(EMAIL, PASSWORD)

        server.sendmail(
            EMAIL,
            recipients,
            msg.as_string()
        )

        server.quit()

        print("Email sent successfully")


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
    notice = soup.find("a", rel="bookmark")

    if notice:

        notice_div = soup.find("div", class_="news")
        notice_id = notice_div["id"].replace("post-", "")

        title = notice.text.strip()
        link = notice["href"]

    else:
        print("Notice not found")
        return


    # Read old notice
    try:
        with open("last_notice.txt", "r") as file:
            old_notice_id = file.read().strip()
    except:
        old_notice_id=""

    if notice_id != old_notice_id:
        send_email(
            "📢 New CSVTU Notice",
            f"{title}\n\n{link}"
        )

        with open("last_notice.txt", "w") as file:
            file.write(notice_id)

    else:
        print("No new notice.")



# Run immediately once
check_notice()



