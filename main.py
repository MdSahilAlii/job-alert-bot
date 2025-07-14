from job_scraper import get_job_listings
from emailer import send_email

def run_job():
    keywords = ["Software Developer Fresher", "Web Developer Fresher", "Frontend Developer Fresher"]
    job_listings = get_job_listings(keywords)
    send_email(job_listings)

if __name__ == "__main__":
    run_job()
