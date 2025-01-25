# from flask import Flask, request, jsonify
# from toxicity import get_toxicity_score
# from emotion import get_emotion_score
# from db import LogEntry, Session

# app = Flask(__name__)

# @app.route('/score', methods=['POST'])
# def score_text():
#     data = request.json
#     text = data.get("text")

#     if not text:
#         return jsonify({"error": "Text is required"}), 400

#     toxicity_score = get_toxicity_score(text)
#     emotion_score = get_emotion_score(text)["score"]

#     # Save to database
#     try:
#         log_entry = LogEntry(text=text, toxicity_score=toxicity_score, emotion_score=emotion_score)
#         session = Session()
#         session.add(log_entry)
#         session.commit()
#     except Exception as e:
#         session.rollback()
#         return jsonify({"error": str(e)}), 500
#     finally:
#         session.close()

#     return jsonify({
#         "text": text,
#         "toxicity_score": toxicity_score,
#         "emotion_score": emotion_score
#     })

# @app.route('/logs', methods=['GET'])
# def get_logs():
#     try:
#         session = Session()
#         logs = session.query(LogEntry).all()
#         results = [
#             {
#                 "id": log.id,
#                 "text": log.text,
#                 "toxicity_score": log.toxicity_score,
#                 "emotion_score": log.emotion_score,
#                 "timestamp": log.timestamp.isoformat()
#             }
#             for log in logs
#         ]
#         return jsonify(results)
#     finally:
#         session.close()

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from datetime import datetime
from toxicity import get_toxicity_score  
from emotion import get_emotion_score  

app = Flask(__name__)
logs = []

@app.route('/score', methods=['POST'])
def analyze_text():
    try:
        data = request.json
        text = data.get("text", "")
        if not text.strip():
            return jsonify({"error": "Text input is required"}), 400

        # Analyze text
        toxicity_score = get_toxicity_score(text)
        emotion_result = get_emotion_score(text)
        emotion_label = emotion_result["emotion"]
        emotion_score = emotion_result["score"]

        # Add to logs
        timestamp = datetime.now().isoformat()
        log_entry = {
            "id": len(logs) + 1,
            "text": text,
            "timestamp": timestamp,
            "toxicity_score": toxicity_score,
            "emotion_label": emotion_label,
            "emotion_score": emotion_score
        }
        logs.append(log_entry)

        return jsonify({
            "toxicity_score": toxicity_score,
            "emotion": emotion_result,
        })

    except Exception as e: 
        print(f"Error: {e}")  # Log the error for debugging
        return jsonify({"error": "Internal server error"}), 500
    

@app.route('/logs', methods=['GET'])
def fetch_logs():
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
