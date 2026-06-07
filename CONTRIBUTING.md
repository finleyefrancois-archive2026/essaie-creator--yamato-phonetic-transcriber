# Contributing to Yamato Phonetic Transcriber

Thank you for considering contributing to Yamato Phonetic Transcriber! This guide will help you get started.

## Code of Conduct

Please be respectful and inclusive in all interactions.

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/yamato-phonetic-transcriber.git
cd yamato-phonetic-transcriber
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### 3. Run Tests

```bash
pytest tests/ -v
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed

### 3. Run Quality Checks

```bash
# Format code
black yamato_transcriber/ tests/

# Lint
flake8 yamato_transcriber/ tests/

# Type check
mypy yamato_transcriber/

# Run tests
pytest tests/ -v --cov=yamato_transcriber
```

### 4. Commit Changes

```bash
git add .
git commit -m "feat: add your feature description"
```

We follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Project Structure

```
yamato-phonetic-transcriber/
├── yamato_transcriber/    # Main package
│   ├── __init__.py
│   ├── transcriber.py     # Core transcription logic
│   ├── config.py          # Configuration
│   ├── cli.py             # Command-line interface
│   └── gui.py             # Graphical interface
├── tests/                 # Test suite
├── app.py                 # Streamlit web app
├── pyproject.toml         # Project configuration
└── requirements*.txt      # Dependencies
```

## Adding New Languages

To add support for a new language:

1. Add the language to `SUPPORTED_LANGUAGES` in `config.py`
2. Ensure eSpeak supports the language
3. Add appropriate ASR model if needed
4. Add tests for the new language
5. Update documentation

## Reporting Issues

When reporting issues, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

## Questions?

Feel free to open an issue for questions or discussions.
