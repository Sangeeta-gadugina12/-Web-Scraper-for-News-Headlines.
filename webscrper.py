import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.deccanherald.com/"
    
    response = requests.get(url)
    response.raise_for_status()  
    
    soup = BeautifulSoup(response.text, "html.parser") 
    headlines = soup.find_all("h2")
    
    print(f" {len(headlines)} headlines saved to 'headlines.txt'")

if __name__ == "__main__":
    scrape_headlines()
