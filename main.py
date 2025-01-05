from gemini_client import GeminiClient

def main():
    print("Welcome to Text-to-CAD Generator!")
    print("Enter your description (or 'quit' to exit):")
    
    gemini_client = GeminiClient()
    
    while True:
        text_input = input("\nDescribe what you want to create: ").strip()
        
        if text_input.lower() == 'quit':
            print("Thank you for using Text-to-CAD Generator!")
            break
            
        if not text_input:
            print("Please enter a description.")
            continue
            
        print("\nGenerating CAD instructions...")
        cad_instructions = gemini_client.generate_cad_instructions(text_input)
        print("\nCAD Model Instructions:")
        print("-" * 50)
        print(cad_instructions)
        print("-" * 50)

if __name__ == "__main__":
    main()