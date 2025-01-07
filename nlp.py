import spacy
from google.cloud import speech
from google.oauth2 import service_account

# Initialize SpaCy model
nlp = spacy.load("en_core_web_sm")

# GCP configuration for Speech-to-Text
key_file_path = "path_to_your_service_account.json"
credentials = service_account.Credentials.from_service_account_file(key_file_path)
speech_client = speech.SpeechClient(credentials=credentials)

def transcribe_audio(gcs_uri):
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        language_code="en-US",
        enable_automatic_punctuation=True
    )
    response = speech_client.recognize(config=config, audio=audio)
    transcription = " ".join(result.alternatives[0].transcript for result in response.results)
    return transcription

def process_transcription(transcription):
    doc = nlp(transcription)
    # Example NLP tasks: entity recognition, sentence segmentation
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentences = [sent.text for sent in doc.sents]
    return entities, sentences

# Example usage
gcs_uri = "gs://your_bucket_name/your_audio_file.webm"
transcription = transcribe_audio(gcs_uri)
entities, sentences = process_transcription(transcription)
print("Entities:", entities)
print("Sentences:", sentences)

