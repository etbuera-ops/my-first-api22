from fastapi import FastAPI

app = FastAPI()

# 1. The Gateway Route (Prevents the Vercel 404 Home Page Error)
@app.get("/")
def home_landing_page():
    return {
        "message": "PH Local Tech API is Live!",
        "go_to_data": "/get-prices"
    }

# 2. Your Production Data Feed Route
@app.get("/get-prices")
def scrape_local_data():
    data_list = [
        {"item_name": "Mechanical Keyboard (60% Layout)", "observed_price_ph": "₱1,499.00", "status": "In Stock"},
        {"item_name": "RGB LED Light Strip (5M)", "observed_price_ph": "₱349.00", "status": "In Stock"},
        {"item_name": "Minimalist Felt Desk Mat", "observed_price_ph": "₱450.00", "status": "Out of Stock"},
        {"item_name": "Ergonomic Vertical Wireless Mouse", "observed_price_ph": "₱899.00", "status": "In Stock"}
    ]
    return {
        "status": "success", 
        "total_items_tracked": len(data_list),
        "currency": "PHP",
        "data": data_list
    }
