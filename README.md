# 🛍️ E-Commerce Chatbot

An intelligent e-commerce chatbot that uses **Semantic Routing** to automatically classify questions and respond in two ways:
- **FAQ** – Answers policy, shipping, refund questions etc. via vector search + Groq LLM.
- **SQL** – Searches products from a SQLite database by auto-generating SQL queries.

---

## 🏗️ Architecture

```
User Query
    │
    ▼
Semantic Router (HuggingFace bge-small-en-v1.5)
    ├── FAQ Route  → ChromaDB (sentence-transformers) → Groq LLM → Answer
    └── SQL Route  → Groq LLM (generate SQL) → SQLite → Groq LLM → Answer
```

---

## 📁 Project Structure

```
project-ecomerce-tool/
├── app/
│   ├── main.py              # Main Streamlit application
│   ├── router.py            # Semantic Router for question classification
│   ├── faq.py               # FAQ answer pipeline via ChromaDB + Groq
│   ├── sql.py               # SQL answer pipeline via Groq + SQLite
│   ├── db.sqlite            # Product database (SQLite)
│   ├── resources/
│   │   └── faq_data.csv     # FAQ data (question, answer)
│   └── .env                 # Environment variables (API key, model)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd project-ecomerce-tool
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create the `app/.env` file with the following content:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

> Get a free API key at [https://console.groq.com](https://console.groq.com)

---

## 🚀 Running the App

```bash
cd app
streamlit run main.py
```

Open your browser at: **http://localhost:8501**

---

## 💬 Example Queries

| Type | Example Query |
|------|--------------|
| **FAQ** | "What is the return policy?" |
| **FAQ** | "How can I track my order?" |
| **FAQ** | "Do you offer free shipping?" |
| **SQL** | "Show me Nike shoes with 50% discount" |
| **SQL** | "Are there any shoes under Rs. 3000?" |
| **SQL** | "Do you have formal shoes in size 9?" |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| [Streamlit](https://streamlit.io) | Web chat interface |
| [Groq](https://groq.com) | Fast LLM inference (Llama 3.3) |
| [ChromaDB](https://www.trychroma.com) | Vector database for FAQ |
| [Sentence Transformers](https://www.sbert.net) | Text embedding (`all-MiniLM-L6-v2`) |
| [Semantic Router](https://github.com/aurelio-labs/semantic-router) | Query intent classification |
| SQLite | Product database |
| Pandas | Data processing |

---

## 📌 Notes

- The `app/.env` file contains your API key and **should not** be committed to git. Add to `.gitignore`:
  ```
  app/.env
  venv/
  __pycache__/
  *.pyc
  ```
- On first run, ChromaDB will automatically ingest FAQ data from `faq_data.csv` into in-memory storage.
- The product database `db.sqlite` contains a `product` table with fields: `product_link`, `title`, `brand`, `price`, `discount`, `avg_rating`, `total_ratings`.
