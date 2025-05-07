from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin

def check_robots_txt(base_url, user_agent="*"):
    robots_url = urljoin(base_url,"/robots.txt")
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except:
        print(f"Could not read {robots_url}")
        return
    print(f"Checking Rules for : {base_url}")
    test_paths = [
        "/", "/jobs", "/viewjob", "/cmp/", "/api/", "/admin/", "/search", "/company/google", "/robots.txt"
    ]
    for path in test_paths:
        full_url = urljoin(base_url,path)
        allowed = rp.can_fetch(user_agent,full_url)
        print(f"{'Allowed' if allowed else 'Disallowed'} : {full_url}")

# example
check_robots_txt("https://www.reed.co.uk/jobs")