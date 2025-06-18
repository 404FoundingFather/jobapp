# Job Application Automation System

AI-powered job application automation platform that discovers relevant jobs, tailors resumes, generates personalized cover letters, and creates application packages for manual submission.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.11+
- Poetry

### Setup (5 minutes)
```bash
# 1. Clone and setup
git clone <repository-url>
cd jobapp
./scripts/setup-dev.sh

# 2. Configure environment
cp .env.example .env
# Edit .env with your API keys (OpenAI, AWS)

# 3. Start development environment
docker-compose up

# 4. Verify setup
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
# Flower (Tasks): http://localhost:5555
```

## 📖 Overview

### Problem Statement
Job seekers spend 20+ hours weekly on manual job searching and application customization, limiting them to 2-3 quality applications per day with poor response rates (<5%) due to generic applications.

### Solution
This system automates job discovery across multiple platforms, provides intelligent job matching using semantic similarity, generates tailored resumes and personalized cover letters, and creates complete application packages for manual submission.

### Key Features (MVP)
- **Intelligent Job Discovery** - Multi-platform aggregation with semantic matching
- **Resume Optimization** - Dynamic tailoring based on job requirements  
- **AI Cover Letters** - Personalized content with company research
- **Application Packages** - Complete packages with job URL, tailored resume, and cover letter
- **Multi-Select Interface** - Select multiple jobs for bulk processing
- **Manual Application Process** - User maintains control over final submission

## 🏗️ Architecture

### Technology Stack
- **Frontend:** React 18+ with TypeScript, Vite, Tailwind CSS, shadcn/ui
- **Backend:** Python 3.11+ with FastAPI, async architecture
- **Database:** PostgreSQL 15+ with pgvector for semantic search
- **Cache/Queue:** Redis 7+ for caching and Celery task processing
- **AI/ML:** OpenAI GPT-4, sentence-transformers for embeddings
- **Infrastructure:** Docker, AWS ECS/Fargate, S3, RDS

### System Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │───►│   API Gateway   │───►│   Microservices │
│  (React TS)     │    │   (FastAPI)     │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
┌─────────────────┐    ┌─────────────────┐           ▼
│   PostgreSQL    │◄───│      Redis      │    ┌─────────────────┐
│   + pgvector    │    │  Cache/Queue    │    │ Job Discovery   │
└─────────────────┘    └─────────────────┘    │ Resume Processor│
                                              │ Cover Letter Gen│
┌─────────────────┐    ┌─────────────────┐    │ Package Manager │
│   OpenAI API    │◄───│   AWS S3        │    └─────────────────┘
│   (GPT-4)       │    │  File Storage   │
└─────────────────┘    └─────────────────┘
```

## 📁 Project Structure

```
jobapp/
├── apps/
│   ├── web-frontend/           # React TypeScript application
│   └── api-gateway/            # FastAPI gateway service
├── services/
│   ├── job-discovery/          # Job scraping and aggregation
│   ├── resume-processor/       # Resume parsing and tailoring
│   ├── cover-letter-gen/       # AI-powered content generation
│   └── automation-engine/      # Package management
├── packages/
│   ├── shared-types/           # TypeScript type definitions
│   ├── ui-components/          # React component library
│   └── python-shared/          # Python utilities
├── scripts/                    # Development and deployment scripts
├── config/                     # Configuration files
├── memory-bank/                # AI documentation system
└── docs/                       # Project documentation
```

## 🛠️ Development

### Development Commands
```bash
# Start all services
docker-compose up

# Start individual components
npm run dev:frontend          # React development server
npm run dev:api               # FastAPI gateway
npm run dev:services          # Infrastructure only

# Testing
npm run test                  # Run all tests
npm run test:frontend         # Frontend tests only
npm run test:backend          # Backend tests only

# Code quality
npm run lint                  # Lint all code
npm run format               # Format all code
npm run type-check           # TypeScript type checking

# Database operations
npm run db:migrate           # Run database migrations
npm run db:reset             # Reset database with seed data
```

### Development Workflow
1. **Start Environment:** `docker-compose up -d postgres redis`
2. **Start Dev Servers:** `npm run dev`
3. **Make Changes:** Edit code with hot reload
4. **Run Tests:** `npm run test`
5. **Check Quality:** `npm run lint && npm run type-check`
6. **Commit Changes:** Git commit with conventional commits

## 📚 Documentation

### Core Documentation (Read First)
- [Product Vision](memory-bank/01-productVision.md) - Goals and user experience
- [System Architecture](memory-bank/03-systemArchitecture.md) - Technical design
- [Development Plan](memory-bank/07-developmentPlan.md) - 20-week roadmap
- [Development Readiness](memory-bank/15-dev-readiness.md) - Setup guide and checklist

### Technical References
- [Database Schema](memory-bank/05-database.md) - PostgreSQL with pgvector
- [UI Design](memory-bank/06-uidesign.md) - React components and patterns
- [Code Patterns](memory-bank/12-code-snippets.md) - Reusable implementation patterns
- [Quick Reference](memory-bank/14-quick-reference.md) - Commands and troubleshooting

### Current Status
- [Kanban Board](memory-bank/08-kanban.md) - Sprint progress and task tracking
- [Changelog](memory-bank/09-changelog.md) - Project history and milestones
- [Technical Decisions](memory-bank/13-decisions.md) - Architectural decision records

## 🎯 Current Phase

**Sprint 0: Pre-Development Setup (Weeks 1-2)**
- ✅ Complete project structure and documentation
- ✅ Docker development environment
- ✅ Database setup with pgvector
- ✅ Environment configuration
- 🚧 Basic API Gateway implementation
- 🚧 Frontend application foundation

**Next: Phase 1 - Foundation & Core Infrastructure (Weeks 3-8)**
- User management with JWT authentication
- Database migrations and schema implementation
- API routing and middleware
- Frontend routing and basic UI components

## 🔐 Security & Compliance

- **Data Protection:** End-to-end encryption, GDPR/CCPA compliance
- **Authentication:** JWT with refresh token rotation
- **API Security:** Rate limiting, input validation, CORS configuration
- **Infrastructure:** VPC, security groups, secret management
- **Ethical AI:** Content transparency, user control, no bias introduction

## 📊 Success Metrics

### User Experience Goals
- Generate tailored resume + cover letter in <60 seconds
- Find 50+ relevant jobs per search query
- Maintain 80%+ semantic similarity to job requirements
- 80%+ of users find suggested jobs relevant

### Technical Performance
- API response time <2 seconds
- Content generation <60 seconds
- 99.5% system uptime
- Support 1,000+ concurrent users

## 🤝 Contributing

1. **Read Documentation:** Start with [Product Vision](memory-bank/01-productVision.md)
2. **Setup Environment:** Follow [Development Readiness Guide](memory-bank/15-dev-readiness.md)
3. **Follow Patterns:** Use established patterns in [Code Snippets](memory-bank/12-code-snippets.md)
4. **Run Tests:** Ensure all tests pass before submitting
5. **Update Documentation:** Keep memory bank current with changes

### Code Standards
- **Frontend:** TypeScript strict mode, ESLint + Prettier
- **Backend:** Python 3.11+, Black + isort formatting, Ruff linting
- **Testing:** 80%+ coverage for business logic
- **Commits:** Conventional commit format

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation:** Complete setup guide in `memory-bank/15-dev-readiness.md`
- **Troubleshooting:** Common issues in `memory-bank/14-quick-reference.md`
- **Architecture Questions:** See `memory-bank/03-systemArchitecture.md`
- **Development Issues:** Check `memory-bank/08-kanban.md` for known issues

---

**Ready to start?** Run `./scripts/setup-dev.sh` and follow the [Development Readiness Guide](memory-bank/15-dev-readiness.md)! 