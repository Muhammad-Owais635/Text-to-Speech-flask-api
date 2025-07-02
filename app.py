from flask import Flask, render_template, request, send_file
from TTS.api import TTS
import os
import uuid
from pydub import AudioSegment

app = Flask(__name__)
api_folder = "audio_files"  # Folder to store audio files



# Get a list of available TTS models
available_tts_models = {
    "Model 1": "tts_models/en/ljspeech/glow-tts",
    "Model 2": "tts_models/en/ek1/tacotron2",
    "Model 3": "tts_models/en/ljspeech/tacotron2-DDC",
    "Model 4": "tts_models/en/ljspeech/tacotron2-DDC_ph",
    "Model 5": "tts_models/en/ljspeech/speedy-speech",
    "Model 6": "tts_models/en/ljspeech/tacotron2-DCA",
    "Model 7": "tts_models/en/ljspeech/vits",
    "Model 8": "tts_models/en/ljspeech/vits--neon",
    "Model 9": "tts_models/en/ljspeech/fast_pitch",
    "Model 10": "tts_models/en/ljspeech/overflow",
    "Model 11": "tts_models/en/ljspeech/neural_hmm",
    "Model 12": "tts_models/en/vctk/vits",
    "Model 13": "tts_models/en/vctk/fast_pitch",
    "Model 14": "tts_models/en/sam/tacotron-DDC",
    "Model 15": "tts_models/en/blizzard2013/capacitron-t2-c50",
    "Model 16": "tts_models/en/blizzard2013/capacitron-t2-c150_v2",
    "Model 17": "tts_models/en/multi-dataset/tortoise-v2",
    "Model 18": "tts_models/en/jenny/jenny",
    "Model 19": "vocoder_models/en/ek1/wavegrad",
    "Model 20": "vocoder_models/en/ljspeech/multiband-melgan",
    "Model 21": "vocoder_models/en/ljspeech/hifigan_v2",
    "Model 22": "vocoder_models/en/ljspeech/univnet",
    "Model 23": "vocoder_models/en/blizzard2013/hifigan_v2",
    "Model 24": "vocoder_models/en/vctk/hifigan_v2",
    "Model 25": "vocoder_models/en/sam/hifigan_v2",
    # Add more models here as needed
}

# Function to generate a unique filename
def generate_unique_filename():
    return str(uuid.uuid4()) + ".wav"

# Route for the main HTML page
@app.route('/')
def index():
    return render_template('index.html', tts_models=available_tts_models)

# Route to generate audio based on selected TTS model
@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    text = request.form['text']
    tts_model = request.form['tts_model']

    tts = TTS(model_name=available_tts_models[tts_model], progress_bar=False)
    
    # Generate TTS audio
    filename = generate_unique_filename()
    file_path = os.path.join(api_folder, filename)
    tts.tts_to_file(text=text, speaker_wav="my/cloning/audio.wav", file_path=file_path)
    
    return filename

# Route to play the audio
@app.route('/play_audio/<filename>')
def play_audio(filename):
    audio_path = os.path.join(api_folder, filename)
    return send_file(audio_path, as_attachment=False)

if __name__ == '__main__':
    os.makedirs(api_folder, exist_ok=True)  # Create a directory to store audio files
    app.run(debug=True)

