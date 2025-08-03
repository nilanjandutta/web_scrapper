
# Naukri Job Scrapper using playwright

Scrape real-time job listings from [Naukri.com](https://www.naukri.com/) using Python and Playwright.  

Full-featured Job Scraper
Dynamic AJAX-rendered site ✔️
Pagination support (5 pages) ✔️
Fields extracted:
Title
Company
Location
Experience
Posted Date
URL
Saved to CSV ready for dashboarding or analytics

---

## Why Selenium Fails to Scrape Naukri.com
Scraping Naukri.com using Selenium often fails due to several advanced anti-scraping techniques implemented by the site. Here's a breakdown:
1. Dynamic Content with Delayed Rendering 
    - Job data is loaded dynamically 
    - Selenium often loads the HTML too early, before job cards appear
    - screenshot capture shows only the loading or false blank page 
    - Even with WebDriverWait, job elements may time out or appear as empty placeholders
2. Lazy Loading & Infinite Scroll
    - Selenium doesn’t simulate scrolling behavior well unless manually scripted
3. Anti-Bot Protection
    - Uses dynamic CSS classes, frequent class name shuffling
    - Pages may render but show “0 jobs found” if a bot-like browser is detected
4. Rate Limiting / Blocking
    - Frequent requests using Selenium can trigger rate limits, returning blank or redirected pages.

# What We Tried with Selenium (and Why It Failed)
We initially attempted to scrape Naukri.com using Selenium, but ran into multiple technical roadblocks. Here's what we tried—and what went wrong:

Attempt 1: Basic Selenium Script with ChromeDriver
Loaded the search results page using webdriver.Chrome()
Tried extracting job cards using find_elements_by_class_name

Result: Returned empty lists or undefined content

Attempt 2: Wait for Job Cards to Load
Used WebDriverWait with presence_of_all_elements_located
Increased wait time to 20+ seconds

Result: Still timed out or showed "0 jobs found"
Reason: Selenium returned DOM before JavaScript fully loaded content

Attempt 3: Scroll Simulation
Added JavaScript scroll with execute_script("window.scrollTo(...)")
Tried forcing lazy-loaded content to appear

Result: No improvement; many elements still didn't load or were stale

Attempt 4: Headless Off + Manual ChromeDriver Setup
Turned off headless mode to appear like a normal browser
Installed exact ChromeDriver version

Result: Still inconsistent — some pages worked, others didn't

Attempt 5: Screenshot Debugging
Captured page screenshots for every page
🔍 Observed that pages only showed loading animations, not job cards

Result: Confirmed content wasn't rendering even visually

Naukri.com uses:
Lazy loading
Dynamic CSS classes
Client-side rendering
Headless browser detection
Fingerprinting via navigator.webdriver and similar

# We Observed that
The saved debug_file.html file helped us inspect the job card layout offline.
We were able to see:
The real class names used (like ni-job-tuple-icon, row3, etc.)
The correct structure for extracting location, experience, and skills
Some content was hidden unless we scrolled (we later fixed this)

# How We Used the Debug File
Inspected actual tags
Like <span class="locWdth">Bengaluru</span> for location.
Verified posted date
Found inside <div class="row6"> → <span class="job-post-day">

# Features

- Scrapes job title, company, location, experience, posted date, and skills
- Uses **Playwright** for reliable browser automation
- Supports **pagination** across multiple job listing pages
- Saves data in **CSV** format for analytics or visualization
- Automatically creates the output folder if missing

---

## Example Output

| Title           | Company     | Location     | Experience | Posted   | Skills               | URL                     |
|----------------|-------------|--------------|------------|----------|----------------------|--------------------------|
| Data Analyst   | Capgemini   | Bengaluru    | 2-5 yrs    | 3 days ago | SQL, Python, Power BI | [View Job](https://...) |
| BI Developer   | TCS         | Mumbai       | 4-8 yrs    | 1 day ago | Tableau, Snowflake    | [View Job](https://...) |

---

## How to Run

### 1. Install dependencies

```bash
pip install pandas playwright
playwright install
```

### 2. Run the scraper

```bash
python scrapper.py
```

This will create a file:
```
data/naukri_jobs.csv
```

---

## Configuration

You can customize this line in `scrapper.py`:
```python
scrape_naukri_jobs(keyword="data analyst", pages=5)
```
Change the keyword or number of pages you want to scrape.

## What You Can Do With This

- Analyze **top in-demand skills** specially for the post of Data Analyst
- Filter jobs by **location or experience**
- Visualize insights using **Tableau**, **Power BI**, or **Python dashboards**
- Track **job trends over time**

---

## 🛠 Tech Stack

- 🕸️ [Playwright](https://playwright.dev/python/)
- 🐍 Python 3.9+
- 📄 pandas
- 📊 Tableau / Power BI (optional for dashboarding)

---

## 🙌 Author

**Nilanjan Dutta**  
Feel free to connect: [LinkedIn](https://www.linkedin.com/)
