# Quick Reference Guide

## Project Overview
**Project Name:** Job Application Assistance System  
**Current Status:** 🔄 **SPRINT 1 IN PROGRESS** - Database Complete, UI in Progress  
**Last Updated:** July 2025  
**Phase:** Sprint 1 - User Management & Authentication (35% Complete)

## Key Technologies
- **Frontend:** Next.js 14.2.30 + TypeScript + Tailwind CSS
- **Backend:** FastAPI + Python 3.11+ + PostgreSQL + Redis
- **Infrastructure:** Docker Compose + AWS (production ready)
- **AI/ML:** OpenAI GPT-4 + pgvector for semantic search

## Quick Start Commands

### Development Environment
```bash
# Start all services (database, Redis)
docker-compose up -d postgres redis

# Frontend (Next.js)
cd apps/web-frontend
npm install
npm run dev  # http://localhost:3000

# Backend (FastAPI)
cd apps/api-gateway
poetry install
poetry run uvicorn app.main:app --reload  # http://localhost:8000
```

### Database Setup
```bash
# Initialize database with extensions
docker exec -it jobapp-postgres-1 psql -U postgres -d jobapp -f /docker-entrypoint-initdb.d/init-extensions.sql
docker exec -it jobapp-postgres-1 psql -U postgres -d jobapp -f /docker-entrypoint-initdb.d/init-db.sql
```

### Project Setup
```bash
# Run automated setup script
./scripts/setup-dev.sh

# Install all dependencies
npm install  # Frontend
poetry install  # Backend services
```

## File Structure Quick Reference

### Frontend (Next.js)
```
apps/web-frontend/
├── app/                    # Next.js app directory (routing)
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Dashboard page
│   ├── jobs/page.tsx      # Jobs page
│   ├── applications/page.tsx  # Applications page
│   └── profile/page.tsx   # Profile page
├── src/
│   ├── components/        # UI components
│   │   ├── ui/           # shadcn/ui components
│   │   └── Layout.tsx    # Main layout
│   ├── pages/            # Page components (legacy)
│   ├── stores/           # Zustand state stores
│   ├── services/         # API services
│   └── types/            # TypeScript types
├── next.config.js        # Next.js configuration
├── tailwind.config.js    # Tailwind CSS config
└── package.json          # Dependencies
```

### Backend (FastAPI)
```
apps/api-gateway/
├── app/
│   ├── main.py           # FastAPI application
│   ├── core/             # Configuration & database
│   ├── routers/          # API routes
│   ├── models/           # Pydantic models
│   └── middleware/       # CORS, logging, etc.
├── pyproject.toml        # Python dependencies
└── Dockerfile.dev        # Development container
```

### Services
```
services/
├── job-discovery/        # Job scraping & aggregation
├── resume-processor/     # Resume parsing & tailoring
├── cover-letter-gen/     # AI cover letter generation
└── automation-engine/    # Browser automation
```

## Key Configuration Files

### Frontend Configuration
- **`next.config.js`** - Next.js settings, API proxy
- **`tailwind.config.js`** - Tailwind CSS theme & plugins
- **`tsconfig.json`** - TypeScript configuration
- **`package.json`** - Dependencies & scripts

### Backend Configuration
- **`pyproject.toml`** - Python dependencies & project settings
- **`alembic.ini`** - Database migration configuration
- **`.env`** - Environment variables

### Infrastructure
- **`docker-compose.yml`** - Development environment
- **`scripts/init-db.sql`** - Database initialization
- **`scripts/init-extensions.sql`** - PostgreSQL extensions

## Environment Variables

### Required Environment Variables
```env
# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/jobapp
REDIS_URL=redis://localhost:6379/0

# API Configuration
API_HOST=localhost
API_PORT=8000
FRONTEND_URL=http://localhost:3000

# Authentication
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256

# OpenAI (User Action Required)
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4

# AWS (User Action Required)
AWS_REGION=us-east-1
AWS_S3_BUCKET=jobapp-documents-dev
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
```

## Common Commands

### Frontend Development
```bash
# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Type checking
npm run type-check

# Linting
npm run lint

# Format code
npm run format
```

### Backend Development
```bash
# Start development server
poetry run uvicorn app.main:app --reload

# Run tests
poetry run pytest

# Database migrations
poetry run alembic upgrade head

# Create new migration
poetry run alembic revision --autogenerate -m "description"
```

### Docker Commands
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild containers
docker-compose build --no-cache

# Access database
docker exec -it jobapp-postgres-1 psql -U postgres -d jobapp
```

## API Endpoints

### Authentication & User Management
```http
# User Registration
POST /api/v1/users/register
Content-Type: application/json
{
  "email": "user@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe"
}

# User Login
POST /api/v1/users/login
Content-Type: application/json
{
  "email": "user@example.com",
  "password": "password123"
}

# Get Current User
GET /api/v1/users/me
Authorization: Bearer <jwt_token>

# Update User
PUT /api/v1/users/me
Authorization: Bearer <jwt_token>
Content-Type: application/json
{
  "first_name": "John",
  "last_name": "Smith"
}
```

### User Profile Management
```http
# Get User Profile
GET /api/v1/users/me/profile
Authorization: Bearer <jwt_token>

# Create User Profile
POST /api/v1/users/me/profile
Authorization: Bearer <jwt_token>
Content-Type: application/json
{
  "resume_text": "Experienced software engineer...",
  "linkedin_url": "https://linkedin.com/in/johndoe",
  "location_city": "San Francisco",
  "years_experience": 5
}

# Update User Profile
PUT /api/v1/users/me/profile
Authorization: Bearer <jwt_token>
Content-Type: application/json
{
  "current_title": "Senior Software Engineer"
}
```

### User Skills & Experience
```http
# Get User Skills
GET /api/v1/users/me/skills
Authorization: Bearer <jwt_token>

# Add User Skill
POST /api/v1/users/me/skills
Authorization: Bearer <jwt_token>
Content-Type: application/json
{
  "skill_name": "Python",
  "skill_category": "technical",
  "proficiency_level": "advanced",
  "years_experience": 3.5
}

# Get User Experience
GET /api/v1/users/me/experiences
Authorization: Bearer <jwt_token>

# Add User Experience
POST /api/v1/users/me/experiences
Authorization: Bearer <jwt_token>
Content-Type: application/json
{
  "company_name": "Tech Corp",
  "job_title": "Software Engineer",
  "start_date": "2022-01-01",
  "is_current": true,
  "description": "Developed web applications..."
}
```

### Health Checks
- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed health with database/Redis status

### Authentication (Planned)
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/refresh` - Token refresh
- `GET /auth/me` - Current user info

### Jobs (Planned)
- `GET /jobs` - List jobs
- `POST /jobs` - Create job
- `GET /jobs/{id}` - Get job details
- `PUT /jobs/{id}` - Update job
- `DELETE /jobs/{id}` - Delete job

### Applications (Planned)
- `GET /applications` - List applications
- `POST /applications` - Create application
- `GET /applications/{id}` - Get application details
- `PUT /applications/{id}` - Update application

## Database Schema

### Core Tables (Planned)
```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Jobs table
CREATE TABLE jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    description TEXT,
    url VARCHAR(500),
    user_id UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Applications table
CREATE TABLE applications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id UUID REFERENCES jobs(id),
    user_id UUID REFERENCES users(id),
    status VARCHAR(50) DEFAULT 'applied',
    applied_at TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

## Troubleshooting

### Common Issues

#### Frontend Issues
- **"can't detect preamble" error** - ✅ **RESOLVED** - Migrated to Next.js
- **Port conflicts** - Change port in `next.config.js` or kill existing process
- **TypeScript errors** - Run `npm run type-check` to identify issues
- **Styling issues** - Check Tailwind CSS configuration and imports

#### Backend Issues
- **Database connection** - Ensure PostgreSQL is running: `docker-compose up -d postgres`
- **Redis connection** - Ensure Redis is running: `docker-compose up -d redis`
- **Port conflicts** - Change API_PORT in environment or kill existing process
- **Import errors** - Run `poetry install` to install dependencies

#### Docker Issues
- **Container won't start** - Check logs: `docker-compose logs [service-name]`
- **Volume permissions** - Ensure proper file permissions on mounted volumes
- **Network issues** - Restart Docker: `docker-compose down && docker-compose up -d`

### Debug Commands
```bash
# Check service status
docker-compose ps

# View service logs
docker-compose logs -f [service-name]

# Check database connection
docker exec -it jobapp-postgres-1 psql -U postgres -d jobapp -c "SELECT version();"

# Check Redis connection
docker exec -it jobapp-redis-1 redis-cli ping

# Check frontend build
cd apps/web-frontend && npm run build

# Check backend startup
cd apps/api-gateway && poetry run python -c "import app.main; print('Backend imports OK')"
```

## Development Workflow

### Feature Development
1. **Create feature branch** - `git checkout -b feature/feature-name`
2. **Frontend changes** - Edit components in `apps/web-frontend/src/`
3. **Backend changes** - Edit API in `apps/api-gateway/app/`
4. **Test changes** - Run tests and manual verification
5. **Commit changes** - Use conventional commit format
6. **Create PR** - Submit pull request for review

### Code Quality
- **TypeScript strict mode** - All frontend code must be type-safe
- **ESLint rules** - Follow linting rules for consistent code style
- **Prettier formatting** - Automatic code formatting on save
- **Testing** - Write tests for new features and bug fixes

### Git Workflow
```bash
# Conventional commit format
git commit -m "feat: add user authentication"
git commit -m "fix: resolve frontend build error"
git commit -m "docs: update API documentation"
git commit -m "refactor: migrate to Next.js framework"
```

## Performance Monitoring

### Frontend Performance
- **Core Web Vitals** - Monitor LCP, FID, CLS
- **Bundle size** - Use `npm run build` to check bundle size
- **Lighthouse scores** - Run Lighthouse audits regularly

### Backend Performance
- **API response times** - Monitor endpoint performance
- **Database queries** - Use query logging and optimization
- **Memory usage** - Monitor container resource usage

### Infrastructure Monitoring
- **Docker resource usage** - `docker stats`
- **Database performance** - Monitor query execution times
- **Redis performance** - Monitor cache hit rates

## Security Checklist

### Frontend Security
- ✅ **HTTPS enforcement** - Configured for production
- ✅ **Content Security Policy** - Implemented in Next.js
- ✅ **Input validation** - Zod schemas for form validation
- ✅ **XSS protection** - React's built-in XSS protection

### Backend Security
- ✅ **JWT authentication** - Secure token handling
- ✅ **Password hashing** - bcrypt for password security
- ✅ **SQL injection protection** - Parameterized queries
- ✅ **CORS configuration** - Proper CORS settings

### Infrastructure Security
- ✅ **Environment variables** - Secure configuration management
- ✅ **Docker security** - Non-root containers
- ✅ **Network security** - VPC and security groups (production)
- ✅ **SSL/TLS** - End-to-end encryption

## Migration Notes

### Recent Changes (July 2024)
- ✅ **Frontend Migration** - Successfully migrated from Vite to Next.js 14
- ✅ **Build System Fix** - Resolved critical "can't detect preamble" error
- ✅ **Routing Update** - Migrated from React Router to Next.js App Router
- ✅ **Component Updates** - Updated all components for Next.js compatibility

### Benefits Achieved
- **Better React Integration** - Native React support without plugin conflicts
- **Improved Performance** - Built-in optimizations and code splitting
- **Enhanced Developer Experience** - Better TypeScript support and debugging
- **Production Ready** - Optimized build process and deployment
- **File-based Routing** - Simpler and more intuitive routing system

## Next Steps

### Immediate Actions (User Required)
1. **OpenAI API Key** - Obtain API key for AI features
2. **AWS Setup** - Configure AWS account for production deployment
3. **Environment Configuration** - Add API keys to `.env` file

### Development Priorities
1. **User Authentication** - Implement JWT-based authentication
2. **Database Schema** - Create and migrate database tables
3. **API Integration** - Connect frontend to backend APIs
4. **Job Management** - Implement job CRUD operations

### Production Deployment
1. **AWS Infrastructure** - Deploy to ECS/Fargate
2. **Database Migration** - Set up RDS with production data
3. **Monitoring Setup** - Configure CloudWatch and logging
4. **SSL/TLS** - Set up HTTPS with ACM certificates

---
*This quick reference should be updated as the project evolves. Keep it current with the most frequently used commands, patterns, and project-specific information.* 