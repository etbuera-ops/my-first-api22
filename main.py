from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

# Permit your local frontend file to read this stream safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def scrape_local_price(url: str, price_selector: str) -> str:
    """
    Launches a real headless browser instance locally, loads the target page,
    waits for dynamic JavaScript loads, and extracts the current live price text.
    """
    async with async_playwright() as p:
        # Launch Chromium headless (change to headless=False if you want to watch it work!)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        try:
            # Navigate to the real store link
            await page.goto(url, timeout=30000, wait_until="domcontentloaded")
            
            # Wait for the specific HTML price container class/id to load into existence
            await page.wait_for_selector(price_selector, timeout=5000)
            
            # Extract the raw inner text value
            raw_price = await page.locator(price_selector).first.inner_text()
            await browser.close()
            return raw_price.strip()
        except Exception as e:
            print(f"Extraction timeout or structural change at URL: {e}")
            await browser.close()
            return "Checking Feed..."

@app.get("/get-prices")
async def get_prices():
    # True Live Product Manifest targeting unblocked local retail pathways
    # We use stable, standard HTML price hooks (selectors) to grab raw live digits
    catalog = [
        {
            "name": "AULA F75 Mechanical Keyboard",
            "url": "https://ecommerce.pinnacle-tech.cf/products/aula-f75", # Replace with your target local tech shop link
            "selector": ".price-item--sale", # The exact CSS class name of the price text
            "img": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=500"
        },
        {
            "name": "Logitech G502 Hero Mouse",
            "url": "https://ecommerce.pinnacle-tech.cf/products/logitech-g502",
            "selector": ".current-price-hook",
            "img": "https://images.unsplash.com/photo-1625842268584-8f3290462a41?w=500"
        }
    ]
    
    live_scraped_data = []
    
    for item in catalog:
        # Scrape the real active marketplace numbers using your local machine browser
        live_price = await scrape_local_price(item["url"], item["selector"])
        
        live_scraped_data.append({
            "item_name": item["name"],
            "observed_price_ph": live_price,
            "discount_tag": "LIVE ACTIVE VALUE",
            "status": "In Stock" if "₱" in live_price or any(char.isdigit() for char in live_price) else "Out of Stock",
            "image_url": item["img"],
            "store_url": item["url"]
        })
        
    return {
        "status": "success",
        "total_items_tracked": len(live_scraped_data),
        "data": live_scraped_data
    }
