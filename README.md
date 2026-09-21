# 📰 News by Email

A simple Python automation project that fetches the latest news based on a chosen topic using the **NewsAPI** and sends the news directly to an email inbox.

The project uses the NewsAPI to retrieve recent articles and Gmail's SMTP service to automatically deliver the news by email.

## ✨ Features

* 📰 Fetches the latest news using NewsAPI
* 🔍 Supports topic-based news searching
* 📧 Sends news directly to an email inbox
* 🔗 Includes article titles, descriptions, and URLs
* 📊 Retrieves up to 20 news articles
* 🔐 Uses Gmail SMTP with SSL
* 🐍 Simple Python implementation
* ⚡ Lightweight and easy to configure

## 🛠️ Technologies Used

* **Python**
* **Requests** – For making API requests to NewsAPI
* **NewsAPI** – For retrieving news articles
* **SMTP / Gmail** – For sending emails
* **SSL** – For secure email communication

## 📂 Project Structure

```text
News-by-Email/
│
├── main.py
├── send_email.py
├── requirements.txt
└── .gitignore
```

### `main.py`

Responsible for:

* Defining the news topic
* Connecting to NewsAPI
* Retrieving news articles
* Extracting article titles, descriptions, and URLs
* Preparing the email content
* Calling the email-sending function

The current implementation uses `tesla` as the default search topic and processes the first 20 returned articles.

### `send_email.py`

Responsible for:

* Connecting to Gmail SMTP
* Authenticating the sender
* Sending the generated news email

The project uses Gmail's SMTP SSL connection on port `465`.

### `requirements.txt`

Contains the Python dependencies required by the project, including `requests` and its related dependencies.

## ⚙️ How It Works

```text
        ┌─────────────────┐
        │     main.py     │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │    NewsAPI      │
        │  Fetch Articles │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Process Articles│
        │ Title/Description│
        │      / URL      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │  send_email.py  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   Gmail SMTP    │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │  📧 Your Inbox  │
        └─────────────────┘
```

### Step 1 — Select a Topic

The topic is defined in `main.py`:

```python
topic = "tesla"
```

You can change it to another topic, for example:

```python
topic = "technology"
```

### Step 2 — Fetch News

The application sends a request to the NewsAPI using the selected topic, date, sorting option, and API key.

### Step 3 — Process Articles

The application extracts:

* Article title
* Article description
* Article URL

The first 20 articles are included in the email.

### Step 4 — Send Email

The generated news content is passed to `send_email()`.

The application then connects to:

```text
smtp.gmail.com
Port: 465
```

and sends the email securely using SSL.

## 🚀 Installation

### Prerequisites

Make sure Python 3.x is installed.

Check your Python installation:

```bash
python --version
```

### Clone the Repository

```bash
git clone https://github.com/Ashwin16052002/News-by-Email.git
```

Navigate to the project:

```bash
cd News-by-Email
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configuration

Before running the project, configure your API and email credentials.

### 1. NewsAPI Key

Create an account with NewsAPI and obtain an API key.

In `main.py`, replace:

```python
api_key = "YOUR_API_KEY"
```

with your actual API key.

### 2. Gmail Configuration

Open `send_email.py` and configure:

```python
username = "YOUR_EMAIL@gmail.com"
password = "YOUR_APP_PASSWORD"
receiver = "YOUR_EMAIL@gmail.com"
```

**Important:** Use a Gmail **App Password** rather than your normal Gmail password.

### 🔐 Security Recommendation

Do **not** commit API keys, email passwords, or other credentials to GitHub.

For a production-ready version, these values should be stored using environment variables or a `.env` file.

## ▶️ Usage

After configuring your API key and email credentials, run:

```bash
python main.py
```

The application will:

1. Request news from NewsAPI.
2. Retrieve the latest articles.
3. Extract the relevant information.
4. Create the email message.
5. Connect to Gmail SMTP.
6. Send the news to the configured recipient.

## 📧 Email Content

The generated email contains:

```text
Subject: Today's news

Article Title

Article Description

Article URL
```

Each article is separated from the next article for readability.

## 🔧 Customization

### Change the News Topic

In `main.py`:

```python
topic = "tesla"
```

Change it to any topic supported by NewsAPI:

```python
topic = "artificial intelligence"
```

or:

```python
topic = "Python programming"
```

### Change the Number of Articles

The current implementation processes the first 20 articles:

```python
content["articles"][:20]
```

You can change `20` to another number.

For example:

```python
content["articles"][:10]
```

will process the first 10 articles.

### Change the Email Subject

The current email subject is:

```text
Today's news
```

You can modify it in `main.py` to create a more descriptive subject.

## 💡 Future Improvements

Some possible improvements for future versions:

* [ ] Move API keys to environment variables
* [ ] Move email credentials to environment variables
* [ ] Allow users to enter the news topic dynamically
* [ ] Add multiple news categories
* [ ] Add HTML-formatted emails
* [ ] Add article images
* [ ] Add automatic daily scheduling
* [ ] Add duplicate article filtering
* [ ] Add error handling for failed API requests
* [ ] Add logging
* [ ] Add configurable number of articles
* [ ] Add support for multiple email recipients
* [ ] Add a simple web interface

## 📚 Use Cases

This project can be used to:

* Receive daily news updates
* Monitor a specific company or technology
* Track industry-related news
* Create a personal news notification system
* Learn API integration using Python
* Learn automated email delivery using SMTP

## 👨‍💻 Author

**Ashwin**

GitHub:
https://github.com/Ashwin16052002

LinkedIn:
https://www.linkedin.com/in/ashwin-v-5124992a9/


## 📜 License

This project is available for educational and personal use.

---

⭐ If you find this project useful, consider giving the repository a star!
