 # 🚀 Selenium Dynamic Scraping Practice

This repository documents my learning journey of scraping dynamic websites using **Selenium in Python**.  
Each script focuses on a specific concept such as login, pagination, modals, dropdowns, CAPTCHA awareness and ethical scraping practices.

---

## 📂 Scripts Included

### `00_check_robots_txt.py`
Check a site's `robots.txt` to understand its scraping rules and ensure respectful web scraping.

### `01_scrape_first_page.py`
Scrapes quotes from the **first page** of [quotes.toscrape.com](http://quotes.toscrape.com).

### `02_scrape_few_pages.py`
Logs in and scrapes quotes from the **first 5 pages** using the "Next" button with wait conditions from [quotes.toscrape.com](http://quotes.toscrape.com/login).

### `03_scrape_all_pages.py`
Logs in and scrapes quotes from **all the pages** using the "Next" button and EC.staleness_of() to ensure new content is loaded properly with wait conditions from [quotes.toscrape.com](http://quotes.toscrape.com/login).

### `04_scrape_infinite_scroll.py`
Scrapes quotes and authors from start to the bottom of the page using **.execute_script** with proper time intervals from [quotes.toscrape.com](http://quotes.toscrape.com/scroll).

### `05_modal_and_form_interaction.py`
Interacts with a modal popup to extract content, fills out a complete form including a dropdown selection, and takes a screenshot on submission. Source: [www.lambdatest.com](https://www.lambdatest.com/selenium-playground/)

### `06_captcha_awareness.py`
Detects CAPTCHA on a demo page, pauses for manual solving, and resumes the script afterward. Source: [www.google.com]("https://www.google.com/recaptcha/api2/demo)

---

## 🧠 Learning Goals

- Understand how to respect scraping rules via `robots.txt`.
- Learn how to interact with login forms using Selenium.
- Handle **pagination** in dynamic web pages using WebDriver waits and navigation logic.
- Use explicit waits to avoid common timing issues.
- Deal with **infinite scrolling** and dynamic loading with delays.
- Interact with modals, forms and dropdowns.
- Detect and pause for CAPTCHAs

---

## 🔧 Tools Used

- Python 3
- Selenium WebDriver
- ChromeDriver
- WebDriverWait / ExpectedConditions

---

## 💡 Personal Goals

- Stay consistent with small, focused scripts
- Push every meaningful update to GitHub
- Document what I learn in README and comments
- Build confidence to take on freelance scraping gigs

---

## ▶️ How to Run

- Clone this repo.
- Install dependencies.
- Update the path to chromedriver.exe in each script.
- Run any script.

---