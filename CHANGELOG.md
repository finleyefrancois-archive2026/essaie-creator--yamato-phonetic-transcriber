# Changelog

All notable changes to Yamato Phonetic Transcriber will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Automatic language detection from audio files
- GitHub Actions CI/CD pipeline for automated testing and releases
- Python package configuration with pyproject.toml
- Test suite with pytest
- Pre-commit hooks for code quality
- CONTRIBUTING.md guide for contributors
- CLI entry points: `yamato-transcribe` and `yamato-gui`

### Changed
- Improved repository structure following Python packaging best practices
- Enhanced error handling and messaging
- Updated dependencies with proper version constraints
- Moved CLI logic to dedicated module

### Fixed
- torchaudio compatibility issues with newer versions
- File handle leaks in batch processing
- Memory management for ASR models

## [1.0.0] - 2024-03-06

### Added
- Initial release
- Multilingual support: English, Spanish, French, Japanese, Haitian Creole
- IPA phonetic transcription
- SpeechBrain integration for ASR
- Phonemizer backend with eSpeak
- ONNX runtime optimization
- Low-resource mode
- Tkinter GUI
- Streamlit web app
- Android mobile app support
- Automatic GitHub Actions builds for Python packages and Android APKs

### Features
- Text-to-phoneme conversion
- Audio-to-phoneme transcription
- Batch processing
- Automatic language detection (experimental)
- Multiple output formats (IPA, ARPABET)
- Command-line interface
- Graphical user interface
- Web application via Streamlit

[Unreleased]: https://github.com/essaie-creator/yamato-phonetic-transcriber/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/essaie-creator/yamato-phonetic-transcriber/releases/tag/v1.0.0
