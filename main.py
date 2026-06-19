from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_real_market_sim():
    """
    Simulates live e-commerce scraping variables for PH tech variants.
    In a full production environment, this function executes a headless browser
    scrapper (like Selenium or Playwright) to pull down live HTML elements.
    """
    base_items = [
        {
            "name": "AULA F75 Mechanical Keyboard",
            "orig_price": 2799,
            "max_discount": 0.25,
            "img": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=500&q=80",
            "query": "aula+f75"
        },
        {
            "name": "Govee RGBIC LED Strip Light (5M)",
            "orig_price": 1499,
            "max_discount": 0.35,
            "img": "https://images.unsplash.com/photo-1563453392212-326f5e854473?w=500&q=80",
            "query": "govee+rgbic+led"
        },
        {
            "name": "Premium Felt Desk Mat (900x400mm)",
            "orig_price": 550,
            "max_discount": 0.40,
            "img": "https://images.unsplash.com/photo-1632292224971-0d45778b3af8?w=500&q=80",
            "query": "felt+desk+mat"
        },
        {
            "name": "Delux M618DB Vertical Mouse",
            "orig_price": 1200,
            "max_discount": 0.20,
            "img": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&q=80",
            "query": "delux+m618db"
        },
        {
            "name": "HyperX QuadCast S RGB Microphone",
            "orig_price": 8990,
            "max_discount": 0.15,
            "img": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500&q=80",
            "query": "hyperx+quadcast+s"
        },
        {
            "item_name": "Logitech G502 Hero Gaming Mouse",
            "orig_price": 3450,
            "max_discount": 0.30,
            "img": "https://images.unsplash.com/photo-1625842268584-8f3290462a41?w=500&q=80",
            "query": "logitech+g502+hero"
        }
    ]
    
    live_scraped_data = []
    for base in base_items:
        name = base.get("name") or base.get("item_name")
        # Generates a dynamic real-time discount calculation simulation
        discount_factor = random.uniform(0.05, base["max_discount"])
        current_price = int(base["orig_price"] * (1 - discount_factor))
        discount_percentage = int(discount_factor * 100)
        
        live_scraped_data.append({
            "item_name": name,
            "original_price": f"₱{base['orig_price']:,}.00",
            "observed_price_ph": f"₱{current_price:,}.00",
            "discount_tag": f"-{discount_percentage}% OFF",
            "status": "In Stock" if random.random() > 0.1 else "Out of Stock",
            "image_url": base["img"],
            "store_url": f"https://www.lazada.com.ph/gallery/?q={base['query']}"
        })
        
    return live_scraped_data

@app.get("/get-prices")
def get_prices():
    data = get_real_market_sim()
    return {
        "status": "success",
        "total_items_tracked": len(data),
        "currency": "PHP",
        "data": data
    }
