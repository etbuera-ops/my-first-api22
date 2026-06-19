from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Enable cross-origin resource sharing so your Vercel app can pull the data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "Backend engine active"}

@app.get("/get-prices")
async def get_prices():
    target_url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=50"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(target_url)
            if response.status_code == 200:
                raw_deals = response.json()[:6]
                usd_to_php = 58.50
                
                live_scraped_data = []
                for deal in raw_deals:
                    orig_usd = float(deal.get("normalPrice", 0))
                    sale_usd = float(deal.get("salePrice", 0))
                    discount_pct = int(float(deal.get("savings", 0)))
                    
                    live_scraped_data.append({
                        "item_name": deal.get("title", "Unknown Item"),
                        "original_price": f"₱{orig_usd * usd_to_php:,.2f}",
                        "observed_price_ph": f"₱{sale_usd * usd_to_php:,.2f}",
                        "discount_tag": f"-{discount_pct}% OFF",
                        "status": "In Stock",
                        "image_url": deal.get("thumb", ""),
                        "store_url": f"https://www.cheapshark.com/redirect?dealID={deal.get('dealID')}"
                    })
                return {"status": "success", "data": live_scraped_data}
    except Exception as e:
        return {"status": "error", "reason": str(e)}

    return {"status": "error", "message": "Failed web request validation"}
