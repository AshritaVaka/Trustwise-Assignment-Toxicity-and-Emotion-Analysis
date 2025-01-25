##this is our model file for the model: emotion 
import torch
from transformers import pipeline

# Loading model pipeline
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

def get_emotion_score(text):
    """
    Returns the most dominant emotion and its score.

    Args:
        text (str): The input text to be evaluated.
        
    Returns:
        dict: A dictionary with the dominant emotion and its score.
    """
    model_outputs = classifier(text)
    
    if not isinstance(model_outputs, list) or not model_outputs:
        raise ValueError("Unexpected output format from the emotion model")
    
    emotions = model_outputs[0]
    
    # Find the emotion with the highest score as dominant emotion to give label for the input sentence
    dominant_emotion = max(emotions, key=lambda x: x['score'])
    
    return {
        "emotion": dominant_emotion['label'], 
        "score": round(dominant_emotion['score'], 4)  
    }

