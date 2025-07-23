# Example MCP loader (simplified)

def predict(image_bytes: bytes, metadata: dict) -> dict:
    # Load model and run inference here
    # For now, return dummy values
    return {
        "style": "impressionism",
        "emotion": "calm",
        "price": 3500.0,
    }
