# 🥋 Jiu-Jitsu Chatbot

**Jiu-Jitsu Chatbot** is a lightweight, domain-specific AI assistant built to answer questions exclusively about Brazilian Jiu-Jitsu (BJJ). Whether you're a white belt or a seasoned black belt, this tool delivers fast, accurate, and grappling-focused responses—no fluff, no off-topic tangents.

Built with **Python**, **LangChain**, and **OpenAI’s API**, it uses a curated local knowledge base to stay grounded in BJJ fundamentals, techniques, and training strategies.

---

## Features

- **Domain-Specific Intelligence**: Focused solely on Brazilian Jiu-Jitsu  
- **Lightweight & Efficient**: Minimal token usage for cost-effective deployment  
- **Offline Knowledge Base**: Supports structured text and PDF ingestion  
- **Custom Prompt Engineering**: Reduces hallucinations and keeps answers on-topic  
- **Simple CLI Interface** (Optional: Streamlit UI coming soon)

---

## Demo

**Example Interaction:**
<img width="1437" alt="Screenshot 2025-07-09 at 17 27 00" src="https://github.com/user-attachments/assets/6340b7b9-372f-4dc0-8670-8d64cf659538" />

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/prasanna4264/Jiu-Jitsu-AI-Chatbot.git
cd Jiu-Jitsu-AI-Chatbot

python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your OpenAI key:

```env
OPENAI_API_KEY=your_openai_key_here
```

Then run the chatbot:

```bash
python bjjchatbot.py
```

You’ll see:  
`Jiu-Jitsu Chatbot ready! Type 'exit' to quit.`

---

## Folder Structure

```
Jiu-Jitsu-AI-Chatbot/
├── bjjchatbot.py            # Main chatbot script
├── data/                    # Custom BJJ PDFs or text files
├── .env                     # API key (excluded from Git)
├── requirements.txt         # Python dependencies
├── .gitignore               # Files to ignore in version control
└── README.md                # Project documentation
```

---

## Tech Stack

- **Python**  
- **OpenAI API** (GPT-3.5 / GPT-4)  
- **LangChain** for prompt orchestration  
- **FAISS** for semantic vector search  
- **PyPDF2** for PDF ingestion  
- **dotenv** for secure API key handling

---

## Security

- API key is stored securely in a `.env` file  
- `.env` is excluded from version control via `.gitignore`  
- Each user must provide their own OpenAI API key

---

## Limitations

- Relies on static local data (no live web scraping)  
- Cannot fetch or analyze video content  
- Will reject non-BJJ-related queries by design

---

## Roadmap

- [ ] Add optional **Streamlit UI**  
- [ ] Expand knowledge base with structured grappling manuals  
- [ ] Integrate clip search using pre-tagged metadata (no YouTube scraping)

---

## 📜 License

**MIT License** — free to fork, extend, or integrate into your own martial arts platform.

---

## 👤 Author

**Prasanna Adhikari**  
Built for fun, focus, and martial arts fluency.

---
