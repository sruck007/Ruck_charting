from flask import Flask, request, jsonify
from transcribe import transcribe_audio
from nlp import process_text
from export import create_export

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    transcription = transcribe_audio(audio_file)
    refined_text = process_text(transcription)
    return jsonify({'transcription': refined_text})

@app.route('/export', methods=['GET'])
def export_data():
    format = request.args.get('format', 'csv')
    export_file = create_export(format)
    return jsonify({'export_url': export_file})

if __name__ == '__main__':
    app.run(debug=True)
