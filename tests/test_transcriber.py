"""Tests for the PhoneticTranscriber class."""

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path

from yamato_transcriber import PhoneticTranscriber, SUPPORTED_LANGUAGES


class TestPhoneticTranscriberInit:
    """Test PhoneticTranscriber initialization."""

    def test_init_default_language(self):
        """Test initialization with default language."""
        transcriber = PhoneticTranscriber()
        assert transcriber.language == 'en'
        assert transcriber.low_resource is True

    def test_init_custom_language(self):
        """Test initialization with custom language."""
        for lang_code in ['es', 'fr', 'ja']:
            transcriber = PhoneticTranscriber(language=lang_code)
            assert transcriber.language == lang_code

    def test_init_unsupported_language(self):
        """Test initialization with unsupported language raises error."""
        with pytest.raises(ValueError):
            PhoneticTranscriber(language='xx')

    def test_init_auto_detect(self):
        """Test initialization with auto-detect enabled."""
        transcriber = PhoneticTranscriber(auto_detect_language=True)
        assert transcriber.auto_detect_language is True


class TestTextToPhonemes:
    """Test text-to-phoneme conversion."""

    @patch('yamato_transcriber.transcriber.PHONEMIZER_AVAILABLE', True)
    @patch('yamato_transcriber.transcriber.phonemize')
    def test_text_to_phonemes_basic(self, mock_phonemize):
        """Test basic text to phoneme conversion."""
        mock_phonemize.return_value = "h ə l ˈoʊ"
        
        transcriber = PhoneticTranscriber(language='en')
        # Mock the phonemizer loading
        transcriber._phonemizer = MagicMock()
        
        result = transcriber.text_to_phonemes("hello")
        
        assert isinstance(result, str)
        mock_phonemize.assert_called_once()

    @patch('yamato_transcriber.transcriber.PHONEMIZER_AVAILABLE', True)
    def test_text_normalization(self):
        """Test text normalization before phonemization."""
        transcriber = PhoneticTranscriber(language='en')
        transcriber._phonemizer = MagicMock()
        
        # Test with extra whitespace
        normalized = transcriber._normalize_text("  hello   world  ")
        assert normalized == "hello world"


class TestBatchTranscribe:
    """Test batch transcription."""

    @patch('yamato_transcriber.transcriber.PHONEMIZER_AVAILABLE', True)
    @patch('yamato_transcriber.transcriber.phonemize')
    def test_batch_transcribe(self, mock_phonemize):
        """Test batch transcription of multiple texts."""
        mock_phonemize.side_effect = ["h ə l ˈoʊ", "w ɜr l d"]
        
        transcriber = PhoneticTranscriber(language='en')
        transcriber._phonemizer = MagicMock()
        
        texts = ["hello", "world"]
        results = transcriber.batch_transcribe(texts)
        
        assert len(results) == 2
        assert all(isinstance(r, str) for r in results)

    @patch('yamato_transcriber.transcriber.PHONEMIZER_AVAILABLE', True)
    def test_batch_transcribe_with_errors(self):
        """Test batch transcription handles errors gracefully."""
        transcriber = PhoneticTranscriber(language='en')
        transcriber._phonemizer = MagicMock()
        transcriber._phonemizer.phonemize.side_effect = Exception("Error")
        
        texts = ["hello", "world"]
        results = transcriber.batch_transcribe(texts)
        
        # Should return empty strings for failed transcriptions
        assert len(results) == 2


class TestLanguageInfo:
    """Test language information retrieval."""

    def test_get_language_info(self):
        """Test getting language information."""
        transcriber = PhoneticTranscriber(language='en')
        info = transcriber.get_language_info()
        
        assert 'code' in info
        assert 'name' in info
        assert 'script' in info
        assert 'phonemizer_lang' in info
        assert info['code'] == 'en'


class TestAudioTranscription:
    """Test audio-to-phoneme transcription."""

    @patch('yamato_transcriber.transcriber.SPEECHBRAIN_AVAILABLE', False)
    def test_audio_without_speechbrain(self):
        """Test audio transcription raises error when SpeechBrain unavailable."""
        transcriber = PhoneticTranscriber(language='en')
        
        with pytest.raises(ImportError):
            transcriber.audio_to_phonemes("fake.wav")

    @patch('yamato_transcriber.transcriber.SPEECHBRAIN_AVAILABLE', True)
    def test_audio_file_not_found(self):
        """Test audio transcription with non-existent file."""
        transcriber = PhoneticTranscriber(language='en')
        
        with pytest.raises(FileNotFoundError):
            transcriber.audio_to_phonemes("nonexistent.wav")
