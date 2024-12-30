// Recorder Logic
const startRecording = () => {
    const recorder = new MediaRecorder(stream);
    const chunks = [];

    recorder.ondataavailable = (e) => chunks.push(e.data);

    recorder.onstop = () => {
        const blob = new Blob(chunks, { type: 'audio/webm' });
        const formData = new FormData();
        formData.append('audio', blob, 'audio.webm');

        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then((response) => response.json())
        .then((data) => console.log('Transcription:', data))
        .catch((error) => console.error('Error:', error));
    };

    recorder.start();
    setTimeout(() => recorder.stop(), 5000); // Stops recording after 5 seconds
};
