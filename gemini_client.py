import google.generativeai as genai
from config import GEMINI_API_KEY, CAD_PROMPT_TEMPLATE

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_cad_instructions(self, text_input):
        try:
            prompt = CAD_PROMPT_TEMPLATE.format(text_input=text_input)
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating CAD instructions: {str(e)}"