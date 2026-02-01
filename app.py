import os
import json
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import pytesseract
from agno.agent import Agent
from agno.models.groq import Groq
from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv

if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
load_dotenv()

app = Flask(__name__)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
E2B_API_KEY = os.getenv("E2B_API_KEY", "")

# In-memory history storage (reset on server restart)
# In production, this would be a database like MongoDB or PostgreSQL
history_storage = []

code_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    markdown=True,
    description="You are an expert polyglot developer who provides solutions in multiple programming languages."
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/workspace", methods=["GET", "POST"])
def index():
    extracted = None
    solution = None
    result = None

    if request.method == "POST":
        query = request.form.get("query")
        image = request.files.get("image")

        if image and not query:
            try:
                img = Image.open(image.stream)
                extracted_text = pytesseract.image_to_string(img).strip()
                extracted = extracted_text if extracted_text else "❌ No text detected in image."
            except Exception as e:
                extracted = f"❌ OCR Error: Tesseract is likely not installed on the server. {str(e)}"

            if extracted and extracted != "❌ No text detected in image.":
                code_prompt = f"""You're an expert Polyglot developer. Provide complete, optimal solutions for the problem below in the following languages: Python, JavaScript, C++, and Java.

Problem:
{extracted}

For the Python solution, ensure it is in a single code block marked with ```python so I can execute it.
Include comments and explanations for each language."""
                response = code_agent.run(code_prompt)
                content = response.content if response.content else ""
                solution = content
                python_code = extract_code_from_markdown(content, "python")

                if python_code and E2B_API_KEY:
                    os.environ["E2B_API_KEY"] = E2B_API_KEY
                    sandbox = Sandbox(timeout=30)
                    execution = sandbox.run_code(python_code)

                    if execution.error:
                        result = f"<div class='text-rose-400'><strong>⚠️ Error:</strong><br><pre>{execution.error}</pre></div>"
                    else:
                        output_lines = execution.logs.stdout if hasattr(execution.logs, "stdout") else str(execution.logs).splitlines()
                        result = "<br>".join(line.strip() for line in output_lines if line.strip())
                
                # Add to history
                history_storage.insert(0, {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "extracted": extracted,
                    "query": None,
                    "languages": ["Python", "JS", "C++", "Java"]
                })

        elif query and not image:
            code_prompt = f"""You're an expert Polyglot developer. Provide complete, optimal solutions for the problem below in the following languages: Python, JavaScript, C++, and Java.

Problem:
{query}

For the Python solution, ensure it is in a single code block marked with ```python so I can execute it.
Include comments and explanations for each language."""
            response = code_agent.run(code_prompt)
            content = response.content if response.content else ""
            solution = content
            python_code = extract_code_from_markdown(content, "python")

            if python_code and E2B_API_KEY:
                os.environ["E2B_API_KEY"] = E2B_API_KEY
                sandbox = Sandbox(timeout=30)
                execution = sandbox.run_code(python_code)

                if execution.error:
                    result = f"<div class='text-rose-400'><strong>⚠️ Error:</strong><br><pre>{execution.error}</pre></div>"
                else:
                    output_lines = execution.logs.stdout if hasattr(execution.logs, "stdout") else str(execution.logs).splitlines()
                    result = "<br>".join(line.strip() for line in output_lines if line.strip())
            
            # Add to history
            history_storage.insert(0, {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "extracted": None,
                "query": query,
                "languages": ["Python", "JS", "C++", "Java"]
            })
        else:
            extracted = "⚠️ Please provide either a query or image (not both)."

    return render_template("index.html", extracted=extracted, solution=solution, result=result)

@app.route("/history")
def history():
    return render_template("history.html", history=history_storage)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/docs")
def docs():
    return render_template("docs.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

def extract_code_from_markdown(markdown: str, language: str = "python") -> str:
    if not markdown:
        return ""
    pattern = f"``` {language}" if f"``` {language}" in markdown else f"```{language}"
    if pattern in markdown:
        try:
            return markdown.split(pattern)[1].split("```")[0].strip()
        except IndexError:
            return markdown.strip()
    return ""

if __name__ == "__main__":
    app.run(debug=True)
