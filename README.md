# 🎬 Personal Movie Collection
A Django-based web application for managing a personal cinema library, built using an AI-native development workflow.

## 🚀 Features
- **Movie Management:** Track titles, directors, release years, and genres.
- **Rating System:** Personal 1-10 star rating for every entry.
- **Admin Dashboard:** Fully configured Django Admin interface with search and filtering.
- **Public Gallery:** A clean, Bootstrap-powered frontend to view the collection.

## 🤖 AI-Native Workflow
This project was developed using:
- **Model:** `Qwen 2.5 Coder` (via Ollama)
- **Agent:** `Claude Code` CLI
- **Orchestration:** Directed via `CLAUDE.md` for environment-aware code generation.

---

## 🛠️ Setup & Installation

### Prerequisites
- [Python 3.12+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) (Fast Python package manager)

### 1. Clone & Environment
```bash
git clone git@github.com:cloudbuster/my-movie-collection.git
cd my-movie-collection 
uv sync
source .venv/bin/activate
