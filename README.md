
# 🗣️ Flask TTS Model Selector & Audio Generator

A Flask-based web app that lets users input text and select from a variety of pre-trained TTS (Text-to-Speech) models to generate and play back audio. Powered by [coqui-ai/TTS](https://github.com/coqui-ai/TTS) and `pydub`.

---

## 🚀 Features

- Choose from 25+ TTS & vocoder models
- Input custom text and generate speech
- Stream generated audio directly from the browser
- Easy web interface using Flask + Jinja2
- Audio saved as `.wav` files with unique names

---

## 🛠️ Requirements

- Python 3.7+
- Flask
- TTS (from Coqui-AI)
- pydub

Install requirements:
```bash
pip install -r requirements.txt
```

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/Text-to-Speech-flask-api.git
cd Text-to-Speech-flask-api
```

2. Download or create a speaker wav (optional)

Some models require a reference voice:
```
my/cloning/audio.wav
```

3. Run the app:
```bash
python app.py
```

4. Open in browser:
```
http://localhost:5000
```

---

## 📁 Project Structure

```
flask-tts-generator/
├── app.py
├── templates/
│   └── index.html
├── audio_files/
│   └── *.wav
├── static/
├── requirements.txt
└── README.md
```

---

## 🔊 Example TTS Models

Some models included:

- `tts_models/en/ljspeech/glow-tts`
- `tts_models/en/ek1/tacotron2`
- `tts_models/en/ljspeech/vits`
- `vocoder_models/en/ljspeech/hifigan_v2`
- ...and many more

See the dropdown list in the app for the full model list.

---

## ✅ requirements.txt

```
Flask
TTS
pydub
```

Also ensure ffmpeg is installed:
```bash
sudo apt install ffmpeg        # Ubuntu/Debian
brew install ffmpeg            # macOS
```

---

## 📤 To-Do

- Add support for saving audio metadata
- Add download button for generated audio
- Add speaker style/voice cloning customization
