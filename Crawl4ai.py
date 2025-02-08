import asyncio
import streamlit as st
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def fetch_markdown(url):
    browser_config = BrowserConfig()  # Default browser configuration
    run_config = CrawlerRunConfig()   # Default crawl run configuration

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Ensure the crawler respects robots.txt
        run_config.respect_robots_txt = True
        result = await crawler.arun(
            url=url,
            config=run_config
        )
        return result.markdown

def main():
    st.title("Web Scraping using Crawl4AI")
    
    # Inject custom CSS to style the button and text input
    st.markdown("""
        <style>
        .stButton > button {
            font-size: 30px;
            padding: 20px 40px;
        }
        input {
            font-size: 60px;
            padding: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    url = st.text_input("Enter URL to get the data from the website:")
    
    if st.button("Fetch Markdown"):
        if url:
            markdown = asyncio.run(fetch_markdown(url))
            st.code(markdown, language='markdown')   
        else:
            st.error("Please enter a valid URL.")

if __name__ == "__main__":
    main()