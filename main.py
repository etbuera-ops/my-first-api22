from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS layers to allow cross-origin requests from Vercel deployments
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-prices")
def get_prices():
    # Production-ready array with tracked tech properties and keyword parameters
    items = [
        {
            "item_name": "AULA F75 Mechanical Keyboard (Wireless/Gasket Mount)", 
            "observed_price_ph": "₱2,199.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=500&q=80",
            "store_url": "https://www.lazada.com.ph/tag/aula-f75/"
        },
        {
            "item_name": "Govee RGBIC LED Strip Light (5 Meters)", 
            "observed_price_ph": "₱1,150.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1563453392212-326f5e854473?w=500&q=80",
            "store_url": "https://www.lazada.com.ph/tag/govee-rgbic/"
        },
        {
            "item_name": "Premium Felt Desk Mat & Mousepad (900x400mm)", 
            "observed_price_ph": "₱380.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1632292224971-0d45778b3af8?w=500&q=80",
            "store_url": "https://www.lazada.com.ph/tag/felt-desk-mat/"
        },
        {
            "item_name": "Delux M618DB Ergonomic Vertical Wireless Mouse", 
            "observed_price_ph": "₱945.00", 
            "status": "Out of Stock",
            "image_url": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&q=80",
            "store_url": "https://www.lazada.com.ph/tag/delux-m618/"
        },
        {
            "item_name": "HyperX QuadCast S RGB USB Condenser Microphone", 
            "observed_price_ph": "₱7,990.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500&q=80",
            "store_url": "https://www.lazada.com.ph/tag/hyperx-quadcast-s/"
        },
        {
            "item_name": "Logitech G502 Hero High Performance Gaming Mouse", 
            "observed_price_ph": "₱2,450.00", 
            "status": "In Stock",
            "image_url": "https://images.unsplash.com/photo-1625842268584-8f3290462a41?w=500&q=80",
            "store_url": "https://www.lazada.com.ph/tag/logitech-g502-hero/"
        }
    ]
    return {
        "status": "success", 
        "total_items_tracked": len(items), 
        "currency": "PHP", 
        "data": items
    }
