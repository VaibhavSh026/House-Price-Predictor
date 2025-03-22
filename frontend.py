import gradio as gr
import requests
def predict_price(area, rooms, age):
    input_data = {
        "feature1": area,
        "feature2": rooms,
        "feature3": age
    }
    url = "https://house-price-predictor-19d5.onrender.com/predict"
    
    try:
        response = requests.post(url, json=input_data)
        prediction = response.json().get("predicted_price", "Error: No response")
        return f"🏠 Estimated House Price: ${prediction}"
    
    except Exception as e:
        return f"⚠️ Error: {e}"
iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Total Area (sqft)", value=1000),
        gr.Number(label="Number of Rooms", value=3),
        gr.Number(label="Building Age (years)", value=5)
    ],
    outputs="text",
    title="🏡 House Price Prediction",
    description="Enter house details to get the estimated price."
)
iface.launch()
