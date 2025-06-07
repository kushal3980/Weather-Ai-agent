# ☀️ Weather AI Agent

A lightweight conversational AI that provides real-time weather updates using Hugging Face’s SmolAgent API. Built with Gradio for a clean UI and powered by `uv` for fast environment and dependency management.

---

## 🚀 Features

- 🔗 SmolAgent integration with Hugging Face API token
- 🖥️ Gradio-based interactive interface
- ⚡ Managed via `uv` (fast Python dependency manager)
- 🧠 Understands natural language queries like:
  - "What's the weather in Mumbai?"
  - "Do I need an umbrella in Delhi today?"

---

## 🛠️ Tech Stack

- [SmolAgent](https://huggingface.co/docs/smol-agent)
- [Gradio](https://gradio.app)
- [uv](https://github.com/astral-sh/uv)

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/kushal3980/weather-ai-agent
cd weather-ai-agent
```
### 2. Create environment and install dependencies using `uv`

```bash
uv venv
uv pip install -r requirements.txt
```

### 3. Add your Hugging Face API token

Create a `.env` file in your project root with the following content:

```ini
HUGGINGFACE_API_TOKEN=your_token_here
```

### 4. Run the app
```bash
uv run main.py
```
