from google.cloud import speech, firestore
from google.oauth2 import service_account
import uuid

# GCP configuration
key_file_path = "path_to_service_account"
credentials = service_account.Credentials.from_service_account_file(key_file_path)
firestore_client = firestore.Client(credentials=credentials)
speech_client = speech.SpeechClient(credentials=credentials)

def transcribe_and_store(filename):
    try:
        gcs_uri = f"gs://hippa-compliant-audio/{filename}"
        audio = speech.RecognitionAudio(uri=gcs_uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
            language_code="en-US",
            enable_automatic_punctuation=True
        )
        response = speech_client.recognize(config=config, audio=audio)
        transcription = " ".join(result.alternatives[0].transcript for result in response.results)
        
        # Store metadata and transcription in Firestore
        transcription_data = {
            "filename": filename,
            "gcs_uri": gcs_uri,
            "transcription": transcription,
            "status": "transcribed",
            "timestamp": firestore.SERVER_TIMESTAMP
        }
        firestore_client.collection('transcriptions').add(transcription_data)
        print(f"Transcription for {filename} stored successfully.")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Example usage:
transcribe_and_store("recording.webm")
