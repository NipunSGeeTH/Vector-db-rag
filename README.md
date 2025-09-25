# AI with Vector Database

A simple Q&A system using FAISS vector database and Google's Generative AI (Gemini) for answering questions in Sinhala based on biology text.

## Features

- **Vector Database**: Uses FAISS for efficient similarity search
- **AI Integration**: Powered by Google Generative AI (Gemini)
- **Sinhala Support**: Answers questions in Sinhala language
- **Biology Focus**: Trained on biology-related content

## Files

- `app.py` - Main application file
- `bio_faiss.index` - FAISS vector database index
- `bio_paragraphs.pkl` - Stored biology text paragraphs
- `.env` - Environment variables (API keys)

## Setup

1. **Install dependencies**:
   ```bash
   pip install faiss-cpu google-generativeai python-dotenv numpy
   ```

2. **Set up environment variables**:
   Create a `.env` file and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

## Usage

The application loads pre-built FAISS index and biology text data, then answers questions in Sinhala about biology topics.

Example question: `ප්‍රභාසස්ලේශණය  විස්තර කරන්න ?` (Describe photosynthesis?)

## Requirements

- Python 3.7+
- FAISS
- Google Generative AI
- NumPy
- python-dotenv

## How it works

1. Loads the FAISS vector database and biology text paragraphs
2. Takes a question as input
3. Uses all paragraphs as context for the AI model
4. Returns an answer in Sinhala using Google's Gemini model
