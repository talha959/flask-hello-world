GEMINI_API_KEY = 'AIzaSyCpEdh6bNP712yRrwO1Tfn8_s8GLSAtTN0'

# Prompt template for CAD generation
CAD_PROMPT_TEMPLATE = """
Generate detailed CAD model instructions for the following description:
{text_input}

Please provide:
1. Basic dimensions and measurements
2. Key geometric features
3. Assembly instructions if applicable
4. Material suggestions
5. Step-by-step modeling instructions
"""