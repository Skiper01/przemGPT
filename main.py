import os
import platform
from textGenerator import textGenerator, createTextFile
from imageGenerator import imageGenerator, createPngFile
from model import get_available_models, get_default_model, get_supported_features
from config import configure_encoding

configure_encoding()

def clear_screen():
    """Clear console screen"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def show_help():
    """Display help information"""
    help_text = """
    Chatbot Commands:
    /help - Show this help
    /clear - Clear screen
    /models - List available models
    /features - Show supported features
    /exit - Exit chatbot
    /save <filename> - Save last response to file
    """
    print(help_text)

def main():
    clear_screen()
    print("Welcome to AI Chatbot!")
    print("Type /help for commands or ask anything")
    
    last_response = None
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() == '/exit':
                print("Goodbye!")
                break
                
            if user_input.lower() == '/help':
                show_help()
                continue
                
            if user_input.lower() == '/clear':
                clear_screen()
                continue
                
            if user_input.lower() == '/models':
                if models := get_available_models():
                    print("\nAvailable models:")
                    for model in models[:15]:
                        print(f"- {model}")
                continue
                
            if user_input.lower() == '/features':
                features = get_supported_features()
                print("\nSupported features:")
                for feat, status in features.items():
                    print(f"- {feat}: {'✓' if status else '✗'}")
                continue
                
            if user_input.lower().startswith('/save '):
                if not last_response:
                    print("No response to save")
                    continue
                    
                filename = user_input[6:].strip()
                if createTextFile(last_response, filename):
                    print(f"Saved to {filename}")
                continue

            # Process normal prompt
            last_response = textGenerator(user_input)
            if last_response:
                try:
                    print("\nAI:", last_response)
                except UnicodeEncodeError:
                    print("\nAI:", last_response.encode('utf-8', errors='replace').decode('utf-8'))
            else:
                print("Error generating response")
            
        except KeyboardInterrupt:
            print("\nUse /exit to quit")
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()