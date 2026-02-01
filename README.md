# 🚀 POLYGLOT.AI

**Synthesize Logic. Transcend Syntax.**

Polyglot AI is a high-performance, developer-first platform that converts visual coding problems (screenshots, whiteboard sketches, textbook images) into optimized, executable solutions across multiple programming languages simultaneously.

![Version](https://img.shields.io/badge/version-2.0.0--beta-indigo)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![Framework](https://img.shields.io/badge/framework-Flask-lightgrey)

---

## ✨ Key Features

- **📷 Visual Recognition (OCR)**: Powered by Tesseract to extract raw logic from images with high precision.
- **🌐 Polyglot Synthesis**: Generates optimized solutions in **Python, JavaScript, C++, and Java** instantly using Llama 3.3.
- **🛡️ Secure Sandbox**: Executes and verifies Python logic in isolated cloud environments via **E2B**.
- **🌗 Native Dark Mode**: A premium, responsive UI that adapts to your environment.
- **📜 Session History**: Automatically tracks your computations for future reference.
- **🔌 Developer First**: Clean API-style documentation and a robust workspace.

---

## 🛠️ Tech Stack

- **Backend**: Python / Flask
- **AI Inference**: Groq (Llama 3.3 70B)
- **OCR Engine**: Tesseract
- **Code Execution**: E2B Sandbox
- **Frontend**: Tailwind CSS, highlight.js, marked.js
- **Environment**: python-dotenv

---

## 🚀 Getting Started

### Prerequisites

1. **Python 3.9+**
2. **Tesseract OCR Engine**:
   - **Windows**: Install to `C:\Program Files\Tesseract-OCR\`
   - **Linux**: `sudo apt install tesseract-ocr`
3. **API Keys**:
   - [Groq API Key](https://console.groq.com/)
   - [E2B API Key](https://e2b.dev/)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/polyglot-ai.git
   cd polyglot-ai
   ```

2. **Setup environment variables**:
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_key
   E2B_API_KEY=your_e2b_key
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000` to start synthesizing.

---

## 📂 Project Structure

```text
├── static/
│   ├── css/          # Premium styles & Dark mode
│   └── js/           # UI Logic
├── templates/        # Jinja2 Multipage Templates
│   ├── base.html     # Layout Engine
│   ├── home.html     # Landing Page
│   ├── workspace.html# Logic Synthesis Engine
│   └── ...
├── app.py            # Main Application Logic
├── requirements.txt  # Project Dependencies
└── Procfile          # Deployment Config
```

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Built with ❤️ for the Global Developer Community
</p>
