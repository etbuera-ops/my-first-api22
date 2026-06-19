from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-prices")
def get_prices():
    # Adding rich data attributes (images and real store paths) to the fallback catalog array
    items = [
        {
            "item_name": "Mechanical Keyboard (60% Layout)", 
            "observed_price_ph": "₱1,499.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&auto=format&fit=crop&q=60",
            "store_url": "https://www.lazada.com.ph"
        },
        {
            "item_name": "RGB LED Light Strip (5M)", 
            "observed_price_ph": "₱349.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1565814636199-ae8133055c1c?w=500&auto=format&fit=crop&q=60",
            "store_url": "https://www.lazada.com.ph"
        },
        {
            "item_name": "Minimalist Felt Desk Mat", 
            "observed_price_ph": "₱450.00", 
            "status": "Out of Stock",
            "image_url": "https://images.unsplash.com/photo-1632292224971-0d45778b3af8?w=500&auto=format&fit=crop&q=60",
            "store_url": "https://www.lazada.com.ph"
        },
        {
            "item_name": "Ergonomic Vertical Wireless Mouse", 
            "observed_price_ph": "₱899.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&auto=format&fit=crop&q=60",
            "store_url": "https://www.lazada.com.ph"
        },
        {
            "item_name": "HyperX QuadCast S Microphone", 
            "observed_price_ph": "₱8,450.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500&auto=format&fit=crop&q=60",
            "store_url": "https://www.lazada.com.ph"
        },
        {
            "item_name": "Logitech G502 Hero Gaming Mouse", 
            "observed_price_ph": "₱2,350.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1625842268584-8f3290462a41?w=500&auto=format&fit=crop&q=60",
            "store_url": "https://www.lazada.com.ph"
        }
    ]
    return {"status": "success", "total_items_tracked": len(items), "currency": "PHP", "data": items}
