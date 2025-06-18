# Technical Context

## AI Population Instructions
When working with this template:
- **First, identify your project type** to determine which sections are relevant
- Replace `[technology-type]` placeholders with actual technology choices
- **Remove sections that don't apply** to your project type (e.g., remove frontend sections for API-only projects)
- Adapt examples to the chosen tech stack while maintaining the structure
- Keep the organizational principles but update specific implementations
- Document the reasoning behind technology choices in the project context

## Project Type Assessment

### Application Type: Web Application with Backend Services
**Primary Type:** Full-stack web application with microservices architecture  
**Secondary Types:** API/Backend services, CLI tools (for data processing)

**Relevant Sections:** Frontend, Backend, Database, Infrastructure & DevOps, API Design, Service Architecture

---

## Technology Stack

### Frontend (Web Application)
- **Framework:** React 18+ with TypeScript 5.0+
- **Language:** TypeScript for type safety and better development experience
- **Build Tool:** Vite 5.0+ for fast development and optimized production builds
- **Styling:** Tailwind CSS with shadcn/ui component library for consistent design system
- **State Management:** Zustand for global state, React Query for server state management

### Backend (Server Applications)
- **Runtime/Language:** Python 3.11+ for ML/NLP ecosystem advantages
- **Framework:** FastAPI 0.104+ for async support, automatic docs, and type safety
- **API Type:** RESTful APIs with GraphQL for complex dashboard queries
- **Authentication:** JWT tokens with OAuth2 for third-party platform integration
- **Task Processing:** Celery 5.3+ with Redis as message broker

### Database & Storage
- **Primary Database:** PostgreSQL 15+ for complex relational data and JSON support
- **Caching:** Redis 7.0+ for session management, task queues, and API caching
- **Search:** PostgreSQL full-text search with pg_trgm for fuzzy matching
- **File Storage:** AWS S3 for resume documents, generated files, and static assets
- **Vector Database:** pgvector extension for semantic similarity searches

### Web Automation & ML/NLP
- **Browser Automation:** Playwright 1.40+ for modern anti-detection capabilities
- **NLP Processing:** spaCy 3.7+ for text processing and entity extraction
- **Semantic Similarity:** sentence-transformers for local embeddings
- **Content Generation:** OpenAI GPT-4 API for cover letter and content generation
- **Resume Parsing:** PyMuPDF and python-docx for document processing

### Infrastructure & DevOps
- **Deployment Target:** AWS ECS/Fargate with containerized microservices
- **Containerization:** Docker with multi-stage builds for optimized images
- **CI/CD:** GitHub Actions for automated testing, building, and deployment
- **Monitoring:** AWS CloudWatch with custom metrics and Sentry for error tracking
- **Load Balancing:** AWS Application Load Balancer with auto-scaling

### Development Tools
- **Version Control:** Git with GitHub for code repository and project management
- **Package Manager:** npm for frontend, pip with Poetry for Python dependencies
- **Code Quality:** ESLint + Prettier for TypeScript, Black + isort for Python
- **Testing:** Vitest + React Testing Library for frontend, pytest for backend
- **Build Tool:** Vite 5.0+ for optimized development and production builds
- **Design System:** Tailwind CSS + shadcn/ui component library

## Project Structure

### Monorepo Structure
```
jobapp/
├── apps/
│   ├── web-frontend/             # React TypeScript dashboard
│   │   ├── src/
│   │   │   ├── components/       # Reusable UI components
│   │   │   ├── pages/           # Application pages/routes
│   │   │   ├── hooks/           # Custom React hooks
│   │   │   ├── stores/          # Zustand state stores
│   │   │   ├── services/        # API client services
│   │   │   └── types/           # TypeScript type definitions
│   │   ├── public/              # Static assets
│   │   └── package.json
│   └── api-gateway/             # FastAPI gateway service
│       ├── app/
│       │   ├── routers/         # API route handlers
│       │   ├── middleware/      # Authentication, CORS, etc.
│       │   ├── models/          # Pydantic models
│       │   └── core/            # Configuration and utilities
│       └── requirements.txt
├── services/
│   ├── job-discovery/           # Job scraping and aggregation
│   │   ├── scrapers/            # Platform-specific scrapers
│   │   ├── processors/          # Data processing and deduplication
│   │   └── models/              # Job data models
│   ├── resume-processor/        # Resume parsing and tailoring
│   │   ├── parsers/             # Document parsing utilities
│   │   ├── analyzers/           # Skills and experience analysis
│   │   └── generators/          # Tailored resume generation
│   ├── cover-letter-gen/        # AI-powered cover letter service
│   │   ├── generators/          # Content generation logic
│   │   ├── research/            # Company research utilities
│   │   └── templates/           # Letter templates and styles
│   └── automation-engine/       # Browser automation service
│       ├── drivers/             # Browser automation drivers
│       ├── platforms/           # ATS-specific automation
│       └── anti-detection/      # Anti-bot detection measures
├── packages/
│   ├── shared-types/            # TypeScript types shared across services
│   ├── ui-components/           # React component library
│   ├── python-shared/           # Python utilities and models
│   └── api-client/              # TypeScript API client
├── docs/                        # Documentation
├── memory-bank/                 # AI Memory Bank
└── infrastructure/              # Docker, AWS CDK, deployment configs
```

## Key Dependencies

### Frontend Dependencies (Implemented)
```json
{
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
    "tailwind-merge": "^2.0.0",
    "tailwindcss-animate": "^1.0.7"
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
```

### Backend Dependencies
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
sqlalchemy==2.0.23
asyncpg==0.29.0
redis==5.0.1
celery==5.3.4
playwright==1.40.0
spacy==3.7.2
sentence-transformers==2.2.2
openai==1.3.0
PyMuPDF==1.23.0
python-docx==1.1.0
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
pytest==7.4.3
pytest-asyncio==0.21.1
```

## Development Environment Setup

### Prerequisites
- **Node.js:** v18.17.0+ with npm 9.0+
- **Python:** 3.11+ with pip and Poetry
- **PostgreSQL:** 15+ for local development
- **Redis:** 7.0+ for caching and task queues
- **Docker:** 24.0+ for containerization
- **AWS CLI:** For cloud resource management

### Quick Start
```bash
# Clone repository
git clone <repository-url>
cd jobapp

# Install frontend dependencies
cd apps/web-frontend
npm install

# Install backend dependencies (using Poetry)
cd ../api-gateway
poetry install
cd ../../services/job-discovery
poetry install
# Repeat for other services

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Set up local database
createdb jobapp_dev
poetry run alembic upgrade head

# Start development services
docker-compose up -d redis postgres
npm run dev  # Frontend
poetry run uvicorn app.main:app --reload  # Backend
```

### Environment Variables

#### Core Application Settings
```env
# Environment
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=debug

# API Configuration
API_HOST=localhost
API_PORT=8000
FRONTEND_URL=http://localhost:3000

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/jobapp_dev
REDIS_URL=redis://localhost:6379/0

# Authentication & Security
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4

# AWS Configuration (for file storage)
AWS_REGION=us-east-1
AWS_S3_BUCKET=jobapp-documents-dev
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key

# External Service APIs
LINKEDIN_API_KEY=your-linkedin-key
INDEED_API_KEY=your-indeed-key

# Browser Automation
PLAYWRIGHT_BROWSER_PATH=/usr/bin/chromium
USER_DATA_DIR=/tmp/playwright-profiles
```

#### Production Environment
```env
# Production settings
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info

# Production URLs
API_HOST=0.0.0.0
FRONTEND_URL=https://app.jobapplyai.com

# Production Database (AWS RDS)
DATABASE_URL=postgresql://user:password@jobapp-prod.xyz.rds.amazonaws.com:5432/jobapp
REDIS_URL=redis://jobapp-prod.xyz.cache.amazonaws.com:6379

# Production Security
JWT_SECRET_KEY=${AWS_SECRET_MANAGER_JWT_KEY}
ENCRYPTION_KEY=${AWS_SECRET_MANAGER_ENCRYPTION_KEY}

# Production File Storage
AWS_S3_BUCKET=jobapp-documents-prod
```

## Deployment

### Development Environment (Active)
- **Frontend:** http://localhost:3000 (React + Vite dev server) ✅ **RUNNING**
- **API Gateway:** http://localhost:8000 (FastAPI with hot reload) ✅ **RUNNING**
- **Database:** PostgreSQL with pgvector on http://localhost:5432 ✅ **HEALTHY**
- **Cache:** Redis on http://localhost:6379 ✅ **HEALTHY**
- **Deployment:** Docker Compose for infrastructure, npm/uvicorn for development servers
- **Status:** All services healthy and verified working

### Staging Environment
- **Platform:** AWS ECS with Fargate
- **Infrastructure:** RDS PostgreSQL, ElastiCache Redis, S3 for file storage
- **Deployment:** GitHub Actions CI/CD with automated testing

### Production Environment
- **Target Platform:** AWS ECS/Fargate with auto-scaling
- **Infrastructure:** Multi-AZ RDS, ElastiCache cluster, CloudFront CDN
- **Deployment:** Blue-green deployment with health checks and rollback capabilities

## External Services & APIs
- **OpenAI GPT-4:** Cover letter generation and content creation
- **LinkedIn API:** Job discovery and profile integration (where available)
- **Indeed API:** Job aggregation and posting details
- **AWS Services:** S3 (file storage), RDS (database), ElastiCache (Redis), CloudWatch (monitoring)
- **Sentry:** Error tracking and performance monitoring
- **SendGrid:** Email notifications and transactional emails

## Performance Considerations

### Application Performance
- **API Response Time:** <2 seconds for all endpoints
- **Job Discovery:** Process 100+ jobs per minute per platform
- **Resume Processing:** Parse and tailor resume in <30 seconds
- **Cover Letter Generation:** Generate personalized content in <10 seconds

### Scalability Strategies
- **Horizontal Service Scaling:** Independent scaling based on load patterns
- **Database Optimization:** Connection pooling, query optimization, read replicas
- **Caching Strategy:** Redis for API responses, browser cache for static assets
- **Queue Management:** Celery workers for background task processing

### Browser Automation Performance
- **Concurrent Sessions:** Support 10+ simultaneous browser instances per service
- **Resource Management:** Automatic browser cleanup and memory management
- **Anti-Detection:** Human-like timing patterns and fingerprint rotation

## Technology Decision Rationale

### Why This Stack?
- **Python FastAPI:** Superior ML/NLP ecosystem integration with async support for web scraping
- **React TypeScript:** Complex UI requirements with type safety for API integrations
- **PostgreSQL:** Complex relational data with JSON support for flexible job posting storage
- **Playwright:** Modern anti-detection capabilities crucial for reliable automation
- **Redis + Celery:** Battle-tested task queue system for background job processing

### Alternative Considerations
- **Node.js Backend:** Considered but Python's ML ecosystem is superior for our use case
- **Vue.js Frontend:** Considered but React ecosystem and team familiarity won out
- **MongoDB:** Considered but relational data patterns and consistency requirements favor PostgreSQL
- **Selenium:** Considered but Playwright offers better modern web app support

### Trade-offs Made
- **Development Speed vs. Performance:** Chose Python for rapid ML integration despite GIL limitations
- **Complexity vs. Flexibility:** Microservices architecture adds complexity but enables independent scaling
- **Cost vs. Quality:** Hybrid local/cloud ML approach balances OpenAI costs with processing speed

---
*Technology choices are documented in docs/technical-decisions.md and should be reviewed quarterly for optimization opportunities.* 