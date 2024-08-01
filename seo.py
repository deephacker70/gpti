import requests
from bs4 import BeautifulSoup

# Define keywords to check for in the page content
keywords_to_check = ['python', 'programming', 'tutorial']

def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}. Exception: {e}")
        return None

def analyze_page_content(html_content):
    if html_content is None:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')

    # Count number of <p> tags (paragraphs)
    paragraphs = soup.find_all('p')
    num_paragraphs = len(paragraphs)

    # Extract and print the title of the page
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.text.strip()
        print(f"Title of the page: {title}")
    else:
        title = ''

    # Check if keywords are present in the page content
    keyword_counts = {keyword: 0 for keyword in keywords_to_check}
    for keyword in keywords_to_check:
        keyword_counts[keyword] = soup.text.lower().count(keyword)

    # Print keyword counts
    print("Keyword Counts:")
    for keyword, count in keyword_counts.items():
        print(f"{keyword}: {count}")

    # You can add more SEO analysis here based on your requirements

    return num_paragraphs, title, keyword_counts

if __name__ == "__main__":
    url = input("Enter the URL to analyze: ").strip()

    html_content = fetch_page(url)
    if html_content:
        num_paragraphs, title, keyword_counts = analyze_page_content(html_content)
        print(f"Number of paragraphs: {num_paragraphs}")
        print(f"Title of the page: {title}")
        print("Keyword Counts:")
        for keyword, count in keyword_counts.items():
            print(f"{keyword}: {count}")
    else:
        print("Failed to fetch or analyze the page.")
