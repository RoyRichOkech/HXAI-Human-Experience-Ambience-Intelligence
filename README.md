# HXAI - Human Experience Ambient Intelligence

An Ambient Intelligence Operating System designed as a lifelong cognitive partner.

## Project Structure

```
HXAI/
├── backend/           # FastAPI + Python
├── frontend/          # React Dashboard
├── database/          # PostgreSQL schema
├── docs/              # Architecture documentation
└── phase-*.md         # Phase guides
```

## Phase 1: Foundation (Weeks 1-2)
- ✅ Authentication system
- ✅ Core database schema
- ✅ API structure
- ✅ Dashboard skeleton

## Tech Stack (Free & Open)
- **Backend**: FastAPI + Python
- **Frontend**: React + TypeScript
- **Database**: PostgreSQL + pgvector
- **Cache**: Redis
- **AI Models**: Mistral (free API), Ollama (local), DeepSeek
- **Infrastructure**: Docker

## Quick Start

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

API will be at: `http://localhost:8000`

### Frontend
```bash
cd frontend
npm install
npm start
```

Dashboard will be at: `http://localhost:3000`

### Database
```bash
# Using Docker
docker run --name hxai-postgres -e POSTGRES_PASSWORD=dev -p 5432:5432 -d postgres:15

# Run migrations
cd backend
alembic upgrade head
```

## Environment Setup

Create `.env` in `backend/`:
```
DATABASE_URL=postgresql://postgres:dev@localhost/hxai_db
JWT_SECRET=your-super-secret-key-change-this
ALLOWED_ORIGINS=http://localhost:3000
MISTRAL_API_KEY=your-key-here
```

## Documentation

- [Architecture Overview](./docs/ARCHITECTURE.md)
- [API Reference](./docs/API.md)
- [Database Schema](./database/schema.sql)
- [Phase 1 Guide](./docs/PHASE_1.md)

## Status

**Current Phase**: 1 - Foundation
**Target Completion**: 2 weeks
**Lead Developer**: RoyRichOkech
