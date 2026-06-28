import requests
from send_email import send_email

topic = "tesla"
api_key = "YOUR_API_KEY"  # Replace with your actual NewsAPI key


url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2026-05-28&sortBy=publishedAt&" \
    f"apiKey={api_key}"
request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] and  article["description"] is not None:
        body = body + article["title"] + "\n" \
        + article["description"] + "\n"\
        + article["url"] + 2*"\n"
        
message = f"""Subject: Today's news
          {body}
          """
message = message.encode("utf-8")
send_email(message=message)
    