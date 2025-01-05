from flask import Flask, render_template, request
from gemini_client import GeminiClient
from utils.template_filters import blueprint as filters_blueprint

app = Flask(__name__)
app.register_blueprint(filters_blueprint)
gemini_client = GeminiClient()

@app.route('/', methods=['GET', 'POST'])
def index():
    cad_instructions = None
    if request.method == 'POST':
        text_input = request.form.get('description', '').strip()
        if text_input:
            cad_instructions = gemini_client.generate_cad_instructions(text_input)
    return render_template('index.html', cad_instructions=cad_instructions)

if __name__ == '__main__':
    app.run(debug=True)