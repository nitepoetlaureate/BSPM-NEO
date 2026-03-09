# BSPM-ULTRA: AI-Native Game Development Platform

An advanced AI-powered automation platform for GB Studio game development, featuring multi-agent collaboration and real-time asset generation.

## Core Features

- Multi-agent AI system (PM, Art, Writing, Code, QA agents)
- ComfyUI integration for visual asset generation
- Real-time WebSocket updates
- Direct GB Studio project manipulation
- Docker-based hybrid architecture

## Project Structure

```
gbstudio_hub/
├── scripts/           # FastAPI backend + AI agents
├── static/           # Frontend assets
├── tools/            # GB Studio automation tools
├── workflows/        # ComfyUI workflows
├── project_files/    # GB Studio projects
└── comfyui_models/  # Asset generation models
```

## Requirements

- Python 3.8+
- Node.js 14+
- Docker and Docker Compose
- GB Studio CLI
- ComfyUI (local installation)

## Environment Setup

1. Copy `.env.example` to `.env` and configure:
   - COMFYUI_OUTPUT_PATH
   - GBS_CLI_PATH
   - OLLAMA_API_URL
   - COMFYUI_API_URL

2. Install dependencies:
```bash
pip install -r requirements.txt
cd gbstudio_hub && npm install
```

## Running the Platform

Start all services:
```bash
./start-all.sh
```

Or use tmux for monitored startup:
```bash
./start-tmux.sh
```

Access points:
- Command Deck: http://localhost:8000
- ComfyUI: http://localhost:8188
- Ollama API: http://localhost:11434

## Development

1. Run tests:
```bash
pytest tests/
```

2. Check API health:
```bash
curl http://localhost:8000/health
```

3. Monitor logs:
```bash
docker-compose logs -f
```

## Contributing

1. Create a feature branch
2. Make changes following project conventions
3. Run tests and linting
4. Submit pull request

## License

[License details to be added]