# Selenium Dynamic Scraping Practice

This repository documents my learning journey of scraping dynamic websites using **Selenium in Python**.  
Each script focuses on a specific concept such as login, pagination, and ethical scraping practices.

---

## 📂 Scripts Included

### `00_check_robots_txt.py`
Check a site's `robots.txt` to understand its scraping rules and ensure respectful web scraping.

### `01_scrape_first_page.py`
Scrapes quotes from the **first page** of [quotes.toscrape.com](http://quotes.toscrape.com).

### `02_scrape_few_pages.py`
Logs in and scrapes quotes from the **first 5 pages** using the "Next" button with wait conditions.

---

## 🧠 Learning Goals

- Understand how to respect scraping rules via `robots.txt`.
- Learn how to interact with login forms using Selenium.
- Handle **pagination** in dynamic web pages using WebDriver waits and navigation logic.

---

## 🔧 Tools Used

- Python 3
- Selenium WebDriver
- ChromeDriver

---

# 🚀 What's Next in My Selenium Learning Journey

As I continue building my web scraping skills with Selenium, here are the next steps I plan to work on:

---

## 🔜 Upcoming Topics to Practice

- **Scraping all pages** (not just a few)
  - Loop through until there's no "Next" button
  - Handle unexpected pagination breaks
- **Infinite Scroll Handling**
  - Practice using `execute_script()` to scroll and load content
  - Wait for content to dynamically load with delays or conditions
- **Pop-up & Modal Interaction**
  - Detect and close popups
  - Extract content from modals and overlays
- **Dropdowns and Forms**
  - Select options from dropdowns (`Select` class)
  - Handle multiple form inputs
- **CAPTCHA Awareness**
  - Learn how to detect CAPTCHAs (only for awareness; never bypass illegally)
  - Understand limitations and ethical boundaries

---

## 💡 Personal Goals

- Stay consistent with small, focused scripts
- Push every meaningful update to GitHub
- Document what I learn in README and comments
- Build confidence to take on freelance scraping gigs

---