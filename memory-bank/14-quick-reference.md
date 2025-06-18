# Quick Reference Guide

## AI Population Instructions
When working with this template:
- Replace `[technology-specific]` placeholders with actual commands, tools, and references
- Adapt the file structure and command examples to match your chosen technology stack
- Update glossary terms to reflect your project's domain and technical choices
- Maintain the quick reference format while customizing content for easy developer lookup

## Project Glossary

### Technical Terms
- **ADR:** Architectural Decision Record - Documents important technical decisions
- **API:** Application Programming Interface - Service communication layer
- **CRUD:** Create, Read, Update, Delete operations
- **CI/CD:** Continuous Integration/Continuous Deployment
- **JWT:** JSON Web Token - Authentication mechanism for stateless sessions
- **pgvector:** PostgreSQL extension for vector similarity search
- **ATS:** Applicant Tracking System - Software used by companies to manage job applications

### Business/Domain Terms
- **Job Discovery:** Automated process of finding relevant job postings across multiple platforms
- **Resume Tailoring:** Dynamic modification of resume content to match specific job requirements
- **Semantic Matching:** AI-powered similarity comparison between user skills and job requirements
- **Application Automation:** Automated submission of job applications through browser automation
- **Cover Letter Generation:** AI-powered creation of personalized cover letters

### Project-Specific Terms
- **Job Card:** UI component displaying job posting information with actions
- **Application Pipeline:** End-to-end workflow from job discovery to application submission
- **Vector Embedding:** Numerical representation of text for semantic similarity calculations
- **Stealth Browser:** Browser automation with anti-detection measures
- **Application Status:** Current state of a job application (pending, submitted, interviewed, etc.)

## Key File Locations

### Configuration Files
```
├── .env.example                    # Environment variables template
├── .gitignore                      # Version control ignore rules
├── docker-compose.yml              # Local development services
├── package.json                    # Frontend dependencies and scripts
├── pyproject.toml                  # Python project configuration (Poetry)
├── tailwind.config.js              # Tailwind CSS configuration
├── eslint.config.js                # ESLint configuration
├── vitest.config.ts                # Testing configuration
└── tsconfig.json                   # TypeScript configuration
```

### Source Code Structure
```
apps/
├── web-frontend/                   # React TypeScript application
│   ├── src/
│   │   ├── components/             # Reusable UI components
│   │   │   ├── ui/                 # Basic UI elements (shadcn/ui)
│   │   │   ├── job/                # Job-related components
│   │   │   └── application/        # Application management components
│   │   ├── pages/                  # Page/route components
│   │   ├── hooks/                  # Custom React hooks
│   │   ├── services/               # API client services
│   │   ├── stores/                 # Zustand state stores
│   │   ├── utils/                  # Utility functions
│   │   ├── types/                  # TypeScript type definitions
│   │   └── constants/              # Application constants
│   └── public/                     # Static assets
└── api-gateway/                    # FastAPI gateway service
    ├── app/
    │   ├── routers/                # API route handlers
    │   ├── middleware/             # Authentication, CORS, etc.
    │   ├── models/                 # Pydantic models
    │   ├── core/                   # Configuration and utilities
    │   └── deps/                   # Dependency injection
    └── requirements.txt            # Python dependencies
```

### Backend Services Structure
```
services/
├── job-discovery/                  # Job scraping and aggregation
│   ├── scrapers/                   # Platform-specific scrapers
│   ├── processors/                 # Data processing and deduplication
│   └── models/                     # Job data models
├── resume-processor/               # Resume parsing and tailoring
│   ├── parsers/                    # Document parsing utilities
│   ├── analyzers/                  # Skills and experience analysis
│   └── generators/                 # Tailored resume generation
├── cover-letter-gen/               # AI-powered cover letter service
│   ├── generators/                 # Content generation logic
│   ├── research/                   # Company research utilities
│   └── templates/                  # Letter templates and styles
└── automation-engine/              # Browser automation service
    ├── drivers/                    # Browser automation drivers
    ├── platforms/                  # ATS-specific automation
    └── anti-detection/             # Anti-bot detection measures
```

### Documentation
```
├── README.md                      # Project overview and setup
├── docs/                          # Additional documentation
├── memory-bank/                   # AI Memory Bank (this system)
│   ├── 00-index.md               # Memory Bank navigation
│   ├── 01-productVision.md       # Product goals and vision
│   ├── 02-techContext.md         # Technology stack details
│   └── ...                       # Other Memory Bank files
└── CHANGELOG.md                   # Version history
```

## Common Commands

### Development Commands
```bash
# Start development servers
npm run dev                        # Start frontend development server
poetry run uvicorn app.main:app --reload  # Start API gateway
docker-compose up -d               # Start all development services

# Building
npm run build                      # Build frontend for production
poetry run python -m build        # Build Python packages

# Type checking
npm run type-check                 # Run TypeScript type checking
npm run type-check:watch           # Run type checking in watch mode
```

### Testing Commands
```bash
# Run tests
npm test                           # Run all frontend tests
poetry run pytest                 # Run all backend tests
npm run test:unit                  # Run unit tests only
npm run test:e2e                   # Run end-to-end tests
npm run test:watch                 # Run tests in watch mode
npm run test:coverage              # Run tests with coverage report

# Test specific files
npm test JobCard                   # Test specific component
poetry run pytest tests/api/test_auth.py  # Test specific backend module
```

### Code Quality Commands
```bash
# Linting
npm run lint                       # Run ESLint
npm run lint:fix                   # Fix linting issues automatically
poetry run ruff check              # Run Python linting

# Formatting
npm run format                     # Format code with Prettier
npm run format:check               # Check if code is formatted
poetry run black .                 # Format Python code
poetry run isort .                 # Sort Python imports

# Pre-commit checks
npm run validate                   # Run all frontend checks
poetry run pre-commit run --all-files  # Run Python pre-commit hooks
```

### Database Commands
```bash
# Migrations
poetry run alembic upgrade head    # Run database migrations
poetry run alembic revision --autogenerate -m "description"  # Create new migration
poetry run alembic downgrade -1    # Rollback one migration
poetry run alembic history         # View migration history

# Database operations
createdb jobapp_dev                # Create local database
dropdb jobapp_dev                  # Drop local database
psql jobapp_dev                    # Connect to database
```

### Deployment Commands
```bash
# Production deployment
docker build -t jobapp-frontend .  # Build frontend Docker image
docker build -t jobapp-api .       # Build API Docker image
docker-compose -f docker-compose.prod.yml up  # Deploy to production

# Environment management
cp .env.example .env               # Set up environment variables
docker-compose up -d postgres redis  # Start infrastructure services

# Health checks
curl http://localhost:8000/health   # Check API health
curl http://localhost:3000         # Check frontend health
```

## Environment Variables

### Required Variables
```env
# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/jobapp_dev
REDIS_URL=redis://localhost:6379/0

# Authentication
JWT_SECRET_KEY=your-super-secret-jwt-key-change-in-production
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
ENVIRONMENT=development
API_PORT=8000
FRONTEND_URL=http://localhost:3000
```

### Optional Variables
```env
# External Services
OPENAI_API_KEY=your-openai-api-key
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=jobapp-documents-dev

# Development
DEBUG=true
LOG_LEVEL=debug
HEADLESS_MODE=true

# Browser Automation
PLAYWRIGHT_BROWSER_PATH=/usr/bin/chromium
USER_DATA_DIR=/tmp/playwright-profiles
```

## Troubleshooting Guide

### Common Issues

#### Port Already in Use
```bash
# Find process using port
lsof -i :3000                     # macOS/Linux
netstat -ano | findstr :3000      # Windows

# Kill the process
kill -9 $(lsof -t -i:3000)        # macOS/Linux
taskkill /PID <process-id> /F      # Windows

# Alternative: Use different port
VITE_PORT=3001 npm run dev
```

#### Dependencies Issues
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm cache clean --force
npm install

# Python dependencies
poetry cache clear . --all
rm poetry.lock
poetry install
```

#### Database Connection Issues
```bash
# Check database status
docker-compose ps                  # Check if PostgreSQL is running
psql -h localhost -U postgres -l  # List databases

# Reset database
dropdb jobapp_dev && createdb jobapp_dev
poetry run alembic upgrade head
```

#### Build Failures
```bash
# Clear build cache
rm -rf dist/ .vite/
npm run clean

# Check for linting errors
npm run lint
poetry run ruff check

# Check dependencies
npm audit
npm audit fix
```

### Performance Issues
```bash
# Analyze bundle size
npm run build
npm run analyze                    # Bundle analyzer

# Check for memory leaks
npm run dev --profile

# Database query performance
EXPLAIN ANALYZE SELECT * FROM job_postings WHERE ...
```

## API Endpoints Reference

### Authentication
```
POST   /api/v1/auth/login          # User login
POST   /api/v1/auth/register       # User registration
POST   /api/v1/auth/refresh        # Refresh token
POST   /api/v1/auth/logout         # User logout
GET    /api/v1/auth/me             # Get current user
```

### Jobs
```
GET    /api/v1/jobs                # List jobs
POST   /api/v1/jobs/search         # Search jobs
GET    /api/v1/jobs/{id}           # Get job by ID
POST   /api/v1/jobs/{id}/save      # Save job
DELETE /api/v1/jobs/{id}/save      # Unsave job
```

### Applications
```
GET    /api/v1/applications        # List user applications
POST   /api/v1/applications        # Create application
GET    /api/v1/applications/{id}   # Get application by ID
PUT    /api/v1/applications/{id}   # Update application
DELETE /api/v1/applications/{id}   # Delete application
POST   /api/v1/applications/{id}/submit  # Submit application
```

### Users
```
GET    /api/v1/users/profile       # Get user profile
PUT    /api/v1/users/profile       # Update user profile
POST   /api/v1/users/resume        # Upload resume
GET    /api/v1/users/preferences   # Get search preferences
PUT    /api/v1/users/preferences   # Update search preferences
```

## Testing Utilities

### Test Data Factories
```typescript
// Create test user
const testUser = createTestUser({ 
  email: 'test@example.com',
  firstName: 'John',
  lastName: 'Doe'
});

// Create test job
const testJob = createTestJob({
  title: 'Software Engineer',
  company: 'Test Company',
  location: 'San Francisco, CA'
});
```

### Mock Functions
```typescript
// Mock API calls
const mockJobApi = vi.mocked(jobApi);
mockJobApi.searchJobs.mockResolvedValue({ data: [testJob] });

// Mock React Query
const mockUseQuery = vi.mocked(useQuery);
mockUseQuery.mockReturnValue({ data: null, isLoading: false, error: null });
```

## Development Tools

### IDE/Editor Shortcuts (VS Code)
- **Cmd/Ctrl + P:** Quick file open
- **Cmd/Ctrl + Shift + P:** Command palette
- **Cmd/Ctrl + `:** Toggle terminal
- **Cmd/Ctrl + B:** Toggle sidebar
- **F12:** Go to definition
- **Shift + F12:** Find references

### Browser DevTools
- **F12:** Toggle DevTools
- **Cmd/Ctrl + Shift + C:** Inspect element
- **Cmd/Ctrl + R:** Refresh page
- **Cmd/Ctrl + Shift + R:** Hard refresh

### Debug Commands
```typescript
// Check environment
console.log('Environment:', import.meta.env.VITE_API_URL);

// Debug React Query
import { useQueryClient } from '@tanstack/react-query';
const queryClient = useQueryClient();
console.log('Query cache:', queryClient.getQueryCache());

// Performance timing
console.time('API Request');
// ... code ...
console.timeEnd('API Request');
```

## Platform-Specific Commands

### macOS Development
```bash
# Install dependencies
brew install postgresql@15 redis
brew services start postgresql@15
brew services start redis

# Python setup
pyenv install 3.11.0
pyenv local 3.11.0
```

### Windows Development
```cmd
# Install dependencies with Chocolatey
choco install postgresql redis-64
choco install python --version=3.11.0

# Start services
net start postgresql-x64-15
net start Redis
```

### Linux Development
```bash
# Install dependencies (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql-15 redis-server python3.11
sudo systemctl start postgresql
sudo systemctl start redis
```

## Contact Information

### Team Contacts
- **Project Lead:** [Name] - [email]
- **Tech Lead:** [Name] - [email]
- **Frontend Lead:** [Name] - [email]
- **Backend Lead:** [Name] - [email]

### Resources
- **Repository:** https://github.com/404FoundingFather/jobapp
- **Documentation:** `/docs` folder in repository
- **Issue Tracker:** GitHub Issues
- **Team Communication:** [Slack/Discord/Teams channel]

## Project-Specific Notes

### Important Conventions
- **File Naming:** PascalCase for components, camelCase for utilities
- **Component Structure:** One component per file, co-located tests
- **State Management:** React Query for server state, Zustand for client state
- **Testing Approach:** Test behavior, not implementation

### Performance Targets
- **Page Load Time:** < 2 seconds
- **API Response Time:** < 500ms average, < 2s 95th percentile
- **Job Search Results:** < 1 second for 50+ jobs
- **Application Processing:** < 30 seconds end-to-end

### Known Limitations
- **OpenAI API Costs:** Monitor usage to avoid budget overrun
- **Browser Detection:** Some platforms may detect automation, requiring manual fallback
- **Rate Limiting:** Job platforms may limit scraping frequency
- **Vector Search:** Performance degrades with very large datasets (>1M jobs)

### Current Sprint Focus
- **Sprint 0:** Infrastructure setup and environment configuration
- **Priority:** Complete Docker development environment and external service integration
- **Blockers:** OpenAI API approval, AWS account setup
- **Next:** User management and job discovery service implementation

---
*This quick reference should be updated as the project evolves. Keep it current with the most frequently used commands, patterns, and project-specific information.* 