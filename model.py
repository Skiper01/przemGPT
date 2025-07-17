from config import client

def get_available_models():
    """Get list of available OpenAI models"""
    try:
        return sorted([model.id for model in client.models.list().data])
    except Exception as e:
        print("Model list error:", str(e))
        return None

def get_default_model():
    """Get default model name"""
    return "gpt-3.5-turbo"

def get_supported_features():
    """Get supported features dictionary"""
    return {
        "text_generation": True,
        "image_generation": True,
        "video_generation": False
    }