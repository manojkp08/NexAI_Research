import requests
from bs4 import BeautifulSoup

def get_company_info(company_name):
    # Format the company name for the URL (replace spaces with underscores)
    company_name = company_name.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{company_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Get the introductory section (first few paragraphs)
        intro_paragraphs = soup.find_all("p", limit=3)  # Adjust limit for more or fewer paragraphs
        intro_text = " ".join([p.text for p in intro_paragraphs])

        # Get key sections (e.g., History, Products, Key People)
        sections = {}
        for header in soup.find_all(['h2', 'h3']):
            header_text = header.text.strip()
            if header_text in ["History", "Products", "Key people", "Operations"]:
                section_content = []
                for sibling in header.find_next_siblings():
                    if sibling.name and sibling.name.startswith("h"):
                        break  # Stop at the next header section
                    if sibling.name == "p":
                        section_content.append(sibling.text)
                sections[header_text] = " ".join(section_content)

        # Return all collected information in a structured way
        return {
            "company_name": company_name,
            "intro": intro_text
        }
    else:
        return {"error": "Company information could not be retrieved"}