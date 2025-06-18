#!/bin/bash

# =============================================================================
# Job Application Automation System - Development Setup Script
# =============================================================================
# This script sets up the complete development environment

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."
    
    local missing_deps=()
    
    if ! command_exists docker; then
        missing_deps+=("docker")
    fi
    
    if ! command_exists docker-compose; then
        missing_deps+=("docker-compose")
    fi
    
    if ! command_exists node; then
        missing_deps+=("node")
    fi
    
    if ! command_exists python3; then
        missing_deps+=("python3")
    fi
    
    if ! command_exists poetry; then
        missing_deps+=("poetry")
    fi
    
    if [ ${#missing_deps[@]} -ne 0 ]; then
        log_error "Missing dependencies: ${missing_deps[*]}"
        log_error "Please install the missing dependencies and try again."
        exit 1
    fi
    
    log_success "All prerequisites satisfied"
}

# Create project directory structure
create_project_structure() {
    log_info "Creating project directory structure..."
    
    # Main directories
    mkdir -p apps/web-frontend/{src/{components/{ui,job,application,user},pages,hooks,services,stores,utils,types,constants},public}
    mkdir -p apps/api-gateway/{app/{routers,middleware,models,core,deps,services},tests,migrations}
    
    # Service directories
    mkdir -p services/job-discovery/{app/{scrapers,processors,models,core},tests}
    mkdir -p services/resume-processor/{app/{parsers,analyzers,generators,core},tests}
    mkdir -p services/cover-letter-gen/{app/{generators,research,templates,core},tests}
    mkdir -p services/automation-engine/{app/{drivers,platforms,anti-detection,core},tests}
    
    # Shared packages
    mkdir -p packages/{shared-types,ui-components,python-shared,api-client}
    
    # Infrastructure and config
    mkdir -p infrastructure/{docker,aws,kubernetes}
    mkdir -p config/{nginx,ssl}
    mkdir -p scripts/{database,deployment,development}
    mkdir -p logs
    mkdir -p uploads
    
    log_success "Project structure created"
}

# Create environment files
create_environment_files() {
    log_info "Creating environment files..."
    
    # Main .env file
    if [ ! -f .env ]; then
        cat > .env << EOF
# =============================================================================
# DEVELOPMENT ENVIRONMENT CONFIGURATION
# =============================================================================

# Application Settings
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=debug

# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/jobapp_dev
REDIS_URL=redis://localhost:6379/0

# Authentication
JWT_SECRET_KEY=dev-secret-key-change-in-production-32-chars
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# External APIs (add your keys here)
OPENAI_API_KEY=your-openai-api-key-here
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=jobapp-documents-dev

# Celery
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/1

# Frontend
VITE_API_URL=http://localhost:8000
VITE_APP_TITLE=Job Application Automation
VITE_DEBUG_MODE=true
EOF
        log_success "Created .env file"
    else
        log_warning ".env file already exists, skipping"
    fi
    
    # Frontend environment
    if [ ! -f apps/web-frontend/.env.local ]; then
        cat > apps/web-frontend/.env.local << EOF
VITE_API_URL=http://localhost:8000
VITE_APP_TITLE=Job Application Automation
VITE_DEBUG_MODE=true
VITE_LOG_LEVEL=debug
EOF
        log_success "Created frontend .env.local file"
    fi
}

# Create basic package.json files
create_package_files() {
    log_info "Creating package.json files..."
    
    # Root package.json
    if [ ! -f package.json ]; then
        cat > package.json << EOF
{
  "name": "job-application-automation",
  "version": "0.1.0",
  "description": "AI-powered job application automation system",
  "private": true,
  "workspaces": [
    "apps/*",
    "packages/*"
  ],
  "scripts": {
    "dev": "concurrently \"npm run dev:frontend\" \"npm run dev:api\"",
    "dev:frontend": "cd apps/web-frontend && npm run dev",
    "dev:api": "cd apps/api-gateway && poetry run uvicorn app.main:app --reload",
    "dev:services": "docker-compose up -d postgres redis",
    "dev:full": "docker-compose up",
    "build": "npm run build:frontend",
    "build:frontend": "cd apps/web-frontend && npm run build",
    "test": "npm run test:frontend && npm run test:backend",
    "test:frontend": "cd apps/web-frontend && npm run test",
    "test:backend": "cd apps/api-gateway && poetry run pytest",
    "lint": "npm run lint:frontend && npm run lint:backend",
    "lint:frontend": "cd apps/web-frontend && npm run lint",
    "lint:backend": "cd apps/api-gateway && poetry run ruff check",
    "format": "npm run format:frontend && npm run format:backend",
    "format:frontend": "cd apps/web-frontend && npm run format",
    "format:backend": "cd apps/api-gateway && poetry run black . && poetry run isort .",
    "setup": "npm run setup:frontend && npm run setup:backend",
    "setup:frontend": "cd apps/web-frontend && npm install",
    "setup:backend": "cd apps/api-gateway && poetry install",
    "db:migrate": "cd apps/api-gateway && poetry run alembic upgrade head",
    "db:reset": "cd apps/api-gateway && poetry run python scripts/reset_db.py",
    "docker:up": "docker-compose up -d",
    "docker:down": "docker-compose down",
    "docker:logs": "docker-compose logs -f"
  },
  "devDependencies": {
    "concurrently": "^8.2.2"
  },
  "engines": {
    "node": ">=18.17.0",
    "npm": ">=9.0.0"
  }
}
EOF
        log_success "Created root package.json"
    fi
    
    # Frontend package.json
    if [ ! -f apps/web-frontend/package.json ]; then
        cat > apps/web-frontend/package.json << EOF
{
  "name": "@jobapp/web-frontend",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite --host 0.0.0.0",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "test": "vitest",
    "test:watch": "vitest --watch",
    "test:coverage": "vitest --coverage",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "lint:fix": "eslint . --ext ts,tsx --fix",
    "format": "prettier --write \"src/**/*.{ts,tsx,js,jsx,json,css,md}\"",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.0",
    "@tanstack/react-query": "^5.0.0",
    "zustand": "^4.4.0",
    "react-hook-form": "^7.48.0",
    "@hookform/resolvers": "^3.3.0",
    "zod": "^3.22.0",
    "axios": "^1.6.0",
    "tailwindcss": "^3.3.0",
    "@radix-ui/react-slot": "^1.0.0",
    "@radix-ui/react-dialog": "^1.0.0",
    "@radix-ui/react-dropdown-menu": "^2.0.0",
    "@radix-ui/react-select": "^2.0.0",
    "@radix-ui/react-toast": "^1.1.0",
    "lucide-react": "^0.290.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@typescript-eslint/eslint-plugin": "^6.0.0",
    "@typescript-eslint/parser": "^6.0.0",
    "@vitejs/plugin-react": "^4.0.0",
    "autoprefixer": "^10.4.0",
    "eslint": "^8.45.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.0",
    "postcss": "^8.4.0",
    "prettier": "^3.0.0",
    "typescript": "^5.0.0",
    "vite": "^5.0.0",
    "vitest": "^1.0.0"
  }
}
EOF
        log_success "Created frontend package.json"
    fi
}

# Create Python project files
create_python_files() {
    log_info "Creating Python project files..."
    
    # API Gateway pyproject.toml
    if [ ! -f apps/api-gateway/pyproject.toml ]; then
        cat > apps/api-gateway/pyproject.toml << EOF
[tool.poetry]
name = "jobapp-api-gateway"
version = "0.1.0"
description = "API Gateway for Job Application Automation System"
authors = ["Job App Team <team@jobapp.com>"]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.0"
uvicorn = {extras = ["standard"], version = "^0.24.0"}
pydantic = "^2.5.0"
pydantic-settings = "^2.1.0"
sqlalchemy = "^2.0.0"
asyncpg = "^0.29.0"
alembic = "^1.13.0"
redis = "^5.0.0"
celery = "^5.3.0"
python-jose = {extras = ["cryptography"], version = "^3.3.0"}
passlib = {extras = ["bcrypt"], version = "^1.7.0"}
python-multipart = "^0.0.6"
openai = "^1.3.0"
httpx = "^0.25.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-asyncio = "^0.21.0"
black = "^23.0.0"
isort = "^5.12.0"
ruff = "^0.1.0"
mypy = "^1.7.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 88

[tool.ruff]
target-version = "py311"
line-length = 88
EOF
        log_success "Created API Gateway pyproject.toml"
    fi
}

# Create basic Dockerfiles
create_dockerfiles() {
    log_info "Creating Dockerfiles..."
    
    # API Gateway Dockerfile
    mkdir -p apps/api-gateway
    if [ ! -f apps/api-gateway/Dockerfile.dev ]; then
        cat > apps/api-gateway/Dockerfile.dev << EOF
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Configure Poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EOF
        log_success "Created API Gateway Dockerfile.dev"
    fi
    
    # Frontend Dockerfile
    mkdir -p apps/web-frontend
    if [ ! -f apps/web-frontend/Dockerfile.dev ]; then
        cat > apps/web-frontend/Dockerfile.dev << EOF
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

CMD ["npm", "run", "dev"]
EOF
        log_success "Created Frontend Dockerfile.dev"
    fi
}

# Create basic application files
create_basic_app_files() {
    log_info "Creating basic application files..."
    
    # API Gateway main.py
    mkdir -p apps/api-gateway/app
    if [ ! -f apps/api-gateway/app/main.py ]; then
        cat > apps/api-gateway/app/main.py << EOF
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Job Application Automation System API"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Job Application Automation System API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": settings.VERSION}
EOF
        log_success "Created API Gateway main.py"
    fi
    
    # API Gateway config
    if [ ! -f apps/api-gateway/app/core/config.py ]; then
        mkdir -p apps/api-gateway/app/core
        cat > apps/api-gateway/app/core/config.py << EOF
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Job Application Automation System"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/jobapp_dev"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    JWT_SECRET_KEY: str = "dev-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"

settings = Settings()
EOF
        log_success "Created API Gateway config.py"
    fi
    
    # Frontend basic files
    mkdir -p apps/web-frontend/src
    if [ ! -f apps/web-frontend/src/main.tsx ]; then
        cat > apps/web-frontend/src/main.tsx << EOF
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
EOF
        log_success "Created Frontend main.tsx"
    fi
    
    if [ ! -f apps/web-frontend/src/App.tsx ]; then
        cat > apps/web-frontend/src/App.tsx << EOF
import React from 'react'

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4">
          <h1 className="text-3xl font-bold text-gray-900">
            Job Application Automation
          </h1>
        </div>
      </header>
      <main className="max-w-7xl mx-auto py-6 px-4">
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold mb-4">Welcome!</h2>
          <p className="text-gray-600">
            Your job application automation system is ready for development.
          </p>
        </div>
      </main>
    </div>
  )
}

export default App
EOF
        log_success "Created Frontend App.tsx"
    fi
}

# Initialize git repository
init_git() {
    log_info "Initializing git repository..."
    
    if [ ! -d .git ]; then
        git init
        log_success "Git repository initialized"
    else
        log_warning "Git repository already exists"
    fi
    
    # Create .gitignore
    if [ ! -f .gitignore ]; then
        cat > .gitignore << EOF
# Environment variables
.env
.env.local
.env.production

# Dependencies
node_modules/
__pycache__/
*.pyc
.venv/

# Build outputs
dist/
build/
.vite/

# Logs
logs/
*.log

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
*.swp
*.swo

# Database
*.db
*.sqlite

# Uploads
uploads/
temp/

# Python
*.egg-info/
.pytest_cache/
.coverage
.mypy_cache/
.ruff_cache/

# Docker
.dockerignore
EOF
        log_success "Created .gitignore"
    fi
}

# Main setup function
main() {
    echo "========================================"
    echo "Job Application Automation System Setup"
    echo "========================================"
    echo
    
    check_prerequisites
    create_project_structure
    create_environment_files
    create_package_files
    create_python_files
    create_dockerfiles
    create_basic_app_files
    init_git
    
    echo
    log_success "Development environment setup completed!"
    echo
    echo "Next steps:"
    echo "1. Update .env file with your API keys"
    echo "2. Run 'npm run setup' to install dependencies"
    echo "3. Run 'docker-compose up -d postgres redis' to start services"
    echo "4. Run 'npm run dev' to start development servers"
    echo
    echo "For more information, see the documentation in the memory-bank/ directory."
}

# Run main function
main "$@" 