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
    items = [
        {
            "item_name": "AULA F75 Mechanical Keyboard (Wireless/Gasket Mount)", 
            "observed_price_ph": "₱2,199.00", 
            "status": "In Stock",
            "image_url": "https://i.imgur.com/KdfQ9Pz.png",
            "store_url": "https://www.lazada.com.ph/tag/aula-f75/"
        },
        {
            "item_name": "Govee RGBIC LED Strip Light (5 Meters)", 
            "observed_price_ph": "₱1,150.00", 
            "status": "In Stock",
            "image_url": "https://i.imgur.com/39A1Sle.png",
            "store_url": "https://www.lazada.com.ph/tag/govee-rgbic/"
        },
        {
            "item_name": "Premium Felt Desk Mat & Mousepad (900x400mm)", 
            "observed_price_ph": "₱380.00", 
            "status": "In Stock",
            "image_url": "https://i.imgur.com/8N69wZ0.png",
            "store_url": "https://www.lazada.com.ph/tag/felt-desk-mat/"
        },
        {
            "item_name": "Delux M618DB Ergonomic Vertical Wireless Mouse", 
            "observed_price_ph": "₱945.00", 
            "status": "Out of Stock",
            "image_url": "https://i.imgur.com/6XzW79B.png",
            "store_url": "https://www.lazada.com.ph/tag/delux-m618/"
        },
        {
            "item_name": "HyperX QuadCast S RGB USB Condenser Microphone", 
            "observed_price_ph": "₱7,990.00", 
            "status": "In Stock",
            "image_url": "https://i.imgur.com/b7NoxXF.png",
            "store_url": "https://www.lazada.com.ph/tag/hyperx-quadcast-s/"
        },
        {
            "item_name": "Logitech G502 Hero High Performance Gaming Mouse", 
            "observed_price_ph": "₱2,450.00", 
            "status": "In Stock",
            "image_url": "https://i.imgur.com/Z42533w.png",
            "store_url": "https://www.lazada.com.ph/tag/logitech-g502-hero/"
        }
    ]
    return {
        "status": "success", 
        "total_items_tracked": len(items), 
        "currency": "PHP", 
        "data": items
    }
