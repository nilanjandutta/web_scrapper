from playwright.sync_api import sync_playwright
import pandas as pd
import time
import os

def scrape_naukri_jobs(keyword="data analyst", pages=5, save_path="data/naukri_jobs.csv"):
    all_jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        for page_num in range(1, pages + 1):
            print(f"\n🔄 Scraping page {page_num}...")
            url = f"https://www.naukri.com/{keyword.replace(' ', '-')}-jobs-{page_num}?k={keyword}"
            page.goto(url, timeout=60000)
            time.sleep(3)

            job_cards = page.locator(".srp-jobtuple-wrapper")
            count = job_cards.count()

            if count == 0:
                print(f"⚠️ No jobs found on page {page_num}")
                continue

            for i in range(count):
                card = job_cards.nth(i)

                title = card.locator("a.title").inner_text() if card.locator("a.title").count() else "Not specified"
                url = card.locator("a.title").get_attribute("href") if card.locator("a.title").count() else "Not specified"
                company = card.locator("a.comp-name").inner_text() if card.locator("a.comp-name").count() else "Not specified"
                location = card.locator("span.locWdth").inner_text() if card.locator("span.locWdth").count() else "Not specified"
                experience = card.locator("span.expwdth").inner_text() if card.locator("span.expwdth").count() else "Not specified"
                posted = card.locator("span.job-post-day").inner_text() if card.locator("span.job-post-day").count() else "Not specified"

                skills_elements = card.locator("ul.tags-gt li")
                skill_count = skills_elements.count()
                skills = [skills_elements.nth(j).inner_text().strip() for j in range(skill_count)] if skill_count else []
                skill_string = ", ".join(skills) if skills else "Not specified"

                all_jobs.append({
                    "Title": title.strip(),
                    "Company": company.strip(),
                    "Location": location.strip(),
                    "Experience": experience.strip().replace("–", "-"),
                    "Posted": posted.strip(),
                    "Skills": skill_string.strip(),
                    "URL": url.strip() if url else "Not specified"
                })

        browser.close()

    # Save Data
    if all_jobs:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df = pd.DataFrame(all_jobs)
        df.to_csv(save_path, index=False)
        print(f"\n✅ Scraping complete. {len(df)} jobs saved to: {save_path}")
    else:
        print("\n⚠️ No job data was found.")

# Run the scraper
scrape_naukri_jobs()
