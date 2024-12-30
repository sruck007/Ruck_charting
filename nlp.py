import json

def process_text(transcription):
    # Simple NLP processing
    transcription = transcription.lower().replace('um', '').strip()
    return transcription

def apply_template(transcription, template_path='templates/soap_template.json'):
    with open(template_path, 'r') as file:
        template = json.load(file)
    template['content'] = transcription
    return template
