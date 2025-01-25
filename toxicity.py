import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification

from transformers import logging
logging.set_verbosity_error()


# Load pre-trained tokenizer and model for toxicity
tokenizer = RobertaTokenizer.from_pretrained('s-nlp/roberta_toxicity_classifier')
model = RobertaForSequenceClassification.from_pretrained('s-nlp/roberta_toxicity_classifier')

def get_toxicity_score(text):
    """
    Calculates and returns the toxicity score of the given text.
    
    Args:
        text (str): The input text to be evaluated.
        
    Returns:
        float: The probability score of the text being toxic.
    """
    # Tokenize the input text
    batch = tokenizer.encode(text, return_tensors="pt")
    
    # Get model predictions
    output = model(batch)
    logits = output.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    
    # Toxicity probability is at index 1
    toxicity_score = float(probabilities[0][1].item())
    return toxicity_score
