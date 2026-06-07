# Yamato Phonetic Transcriber

[![CI/CD](https://github.com/essaie-creator/yamato-phonetic-transcriber/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/essaie-creator/yamato-phonetic-transcriber/actions/workflows/ci-cd.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight multilingual phonetic transcription application designed for low-resource environments with automatic language detection.

## 🌟 Features

- **🎯 Automatic Language Detection**: Upload audio - AI detects the language automatically!
- **🌍 Multilingual Support**: English, Spanish, French, Japanese, Haitian Creole
- **📝 IPA Output**: International Phonetic Alphabet transcription
- **⚡ Low-Resource Optimized**: ONNX runtime for efficient inference
- **🧠 SpeechBrain Integration**: Advanced speech processing
- **💬 Phonemizer Backend**: Accurate text-to-phoneme conversion with eSpeak
- **🖥️ Multiple Interfaces**: CLI, Tkinter GUI, Streamlit web app
- **📱 Mobile Ready**: Native Android app for all Android devices including Huawei
- **🔧 Installable Package**: Available via pip (coming soon)

## 📦 Installation

### From Source (Development)

```bash
# Clone the repository
git clone https://github.com/essaie-creator/yamato-phonetic-transcriber.git
cd yamato-phonetic-transcriber

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install with development dependencies
pip install -e ".[dev]"

# Or install just the core package
pip install -r requirements.txt
```

### From PyPI (Coming Soon)

```bash
pip install yamato-phonetic-transcriber
```

### Web App (Streamlit Cloud)

Visit our live demo: [yamato-phonetic-transcriber.streamlit.app](https://yamato-phonetic-transcriber.streamlit.app)

### Mobile App (Android)

**Download Pre-built APK:**
Get the latest APK from [Releases](https://github.com/essaie-creator/yamato-phonetic-transcriber/releases).

**Build from Source:**
See [`mobile-android/README.md`](mobile-android/README.md) for detailed instructions.

## 🚀 Usage

### Command Line Interface

```bash
# Auto-detect language from audio (recommended)
yamato-transcribe --audio input.wav

# Or using python directly
python transcribe.py --audio input.wav

# Manually specify language
yamato-transcribe --audio input.wav --lang es

# Transcribe text to IPA
yamato-transcribe --text "Hello world" --lang en

# Batch processing
yamato-transcribe --input-file texts.txt --output-file transcriptions.txt --lang fr

# Launch GUI
yamato-gui
```

### Python API

```python
from yamato_transcriber import PhoneticTranscriber

# Initialize with auto-detection
transcriber = PhoneticTranscriber(auto_detect_language=True)

# Audio to phonemes with language detection
phonemes, detected_lang = transcriber.audio_to_phonemes("audio.wav")
print(f"Detected: {detected_lang}")  # e.g., 'es'
print(f"Phonemes: {phonemes}")

# Text to phonemes
transcriber = PhoneticTranscriber(language='en')
phonemes = transcriber.text_to_phonemes("Hello world")
print(phonemes)  # /həˈloʊ wɜrld/

# Batch processing
texts = ["Hello", "World"]
results = transcriber.batch_transcribe(texts)
```

### Web Interface

Run locally:
```bash
streamlit run app.py
```

Or use our hosted version on Streamlit Cloud.

## 🌐 Supported Languages

| Language | Code | Script | Auto-Detect |
|----------|------|--------|-------------|
| 🇺🇸 English | en | Latin | ✅ |
| 🇪🇸 Spanish | es | Latin | ✅ |
| 🇫🇷 French | fr | Latin | ✅ |
| 🇯🇵 Japanese | ja | Kana/Kanji | ✅ |
| 🇭🇹 Haitian Creole | ht | Latin | ✅ |

## 🏗️ Architecture

```
yamato-phonetic-transcriber/
├── yamato_transcriber/    # Core package
│   ├── transcriber.py     # Main transcription engine
│   ├── config.py          # Language configurations
│   ├── cli.py             # Command-line interface
│   └── gui.py             # Tkinter GUI
├── app.py                 # Streamlit web app
├── tests/                 # Test suite
├── mobile-android/        # Android app
└── .github/workflows/     # CI/CD pipelines
```

**Key Technologies:**
- **SpeechBrain**: ASR and language identification
- **Phonemizer**: Text-to-phoneme with eSpeak
- **ONNX Runtime**: Optimized inference
- **PyTorch**: Deep learning backend
- **Streamlit**: Web interface

## ⚡ Performance Optimizations

- Quantized ONNX models (50% smaller footprint)
- Lazy loading of language models
- CPU-optimized inference
- Minimal dependencies for offline use
- Memory-efficient batch processing

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# With coverage
pytest tests/ -v --cov=yamato_transcriber

# Run specific test file
pytest tests/test_transcriber.py -v
```

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

```bash
# Set up development environment
pip install -e ".[dev]"
pre-commit install

# Run quality checks
black yamato_transcriber/ tests/
flake8 yamato_transcriber/ tests/
mypy yamato_transcriber/
pytest tests/
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [SpeechBrain](https://speechbrain.github.io/) for ASR models
- [eSpeak](http://espeak.sourceforge.net/) for phonemization
- [ONNX Runtime](https://onnxruntime.ai/) for optimization

## 📞 Support

- 📧 Issues: [GitHub Issues](https://github.com/essaie-creator/yamato-phonetic-transcriber/issues)
- 📖 Documentation: [Wiki](https://github.com/essaie-creator/yamato-phonetic-transcriber/wiki)
- 💬 Discussions: [GitHub Discussions](https://github.com/essaie-creator/yamato-phonetic-transcriber/discussions)
