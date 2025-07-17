from config import client
import requests

def imageGenerator(prompt, model="dall-e-3"):
    """Generate image from text prompt"""
    try:
        response = client.images.generate(
            model=model,
            prompt=prompt,
            n=1,
            size="1024x1024",
            quality="standard"
        )
        return response.data[0].url
    except Exception as e:
        print("Image generation error:", str(e))
        return None

def createPngFile(img_url, filename):
    """Download and save image"""
    if not img_url:
        return False

    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
        
        if int(response.headers.get('content-length', 0)) > 10_000_000:
            raise ValueError("File too large")
            
        with open(filename, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print("Image save error:", str(e))
        return False
    
def textGenerator(prompt, model="gpt-3.5-turbo"):
    pass

def createTextFile(prompt, filename, model="gpt-3.5-turbo"):
    pass