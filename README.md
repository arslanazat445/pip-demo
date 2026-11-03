# pip-demo

A minimal Python project demonstrating environment variables, virtual environments, and dependency management.

## Requirements

- Python 3.10 or newer
- pip

## Installation

1. Clone the repository:

```bash
git clone https://github.com/arslanazat445/pip-demo.git
cd pip-demo
```

2. Create a virtual environment:

```bash
python3 -m venv .venv
```

3. Activate the virtual environment:

macOS / Linux:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Copy the example configuration:

```bash
cp .env.example .env
```

Edit `.env` and provide the required values:

| Variable | Description |
|---|---|
| APP_NAME | Application name |
| API_KEY | Application secret key |
| DATABASE_URL | Database connection URL |
| OPENAI_API_KEY | OpenAI API key |
| DEBUG | Debug mode setting |

Never commit your `.env` file or share real API keys.

## Run

```bash
python main.py
```

Expected output:

```text
Application: pip-demo
API_KEY loaded: True
```

The program displays whether the API key is configured without revealing its value.
