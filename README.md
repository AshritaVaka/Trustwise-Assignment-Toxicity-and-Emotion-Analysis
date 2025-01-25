# Trustwise Project: Toxicity and Emotion Analysis

This project analyzes text to calculate **toxicity scores** and identify the most dominant **emotion**. It consists of:
- A REST API built with Flask for backend processing.
- A Streamlit web interface for user interaction and visualization.
- Pre-trained models for toxicity and emotion analysis from Hugging Face.

---

## Features
- Analyze the toxicity of a given text.
- Identify the dominant emotion and its score.
- Visualize toxicity and emotion scores over time.

---

## Requirements
- Python 3.8 or higher
- `pip` for installing dependencies
- Pre-trained Hugging Face models:
  - `s-nlp/roberta_toxicity_classifier`
  - `SamLowe/roberta-base-go_emotions`

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. Create a new environment
3. pip install -r requirements.txt

---
## Usage


1. Initialize the database:
   ```bash
   python db.py
2. Initialize the database:
   ```bash
   python api.py
3. Start the streamlit web application in a new terminal:
   ```bash
   streamlit run app.py
4. Access the web interface: Open the streamlit app in your browser at:http://localhost:8501

---
## Project Architecture

1. **api.py**: Flask REST API for backend text processing.
2. **app.py**: Streamlit web app for user interaction.
3. **toxicity.py**: Module for toxicity analysis.
4. **emotion.py**: Module for emotion analysis.
5. **db.py**: Database setup using SQLite and SQLAlchemy.
---
## Docker Instructions
This project is containerized using Docker for easy deployment.

1. Build the Docker image:
   ```bash
   docker build -t trustwise-project.
2. Run the container:
   ```bash
   docker run -p 5000:5000 -p 8501:8501 trustwise-project
---
### Notes
Models are downloaded automatically when you run the application.
The REST API is hosted on http://localhost:5000.
The Streamlit app is hosted on http://localhost:8501.
