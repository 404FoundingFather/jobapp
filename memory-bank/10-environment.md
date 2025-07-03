# Development Environment & Deployment

## Environment Overview

### Environment Types
- **Local Development** - Individual developer machines with Docker Compose
- **Development/Testing** - Shared development environment on AWS ECS
- **Staging** - Pre-production testing environment with production-like data
- **Production** - Live production environment with full monitoring

### Environment URLs
- **Local:** http://localhost:3000 (frontend), http://localhost:8000 (API)
- **Development:** https://dev-api.jobapplyai.com
- **Staging:** https://staging-api.jobapplyai.com
- **Production:** https://api.jobapplyai.com

## Local Development Setup

### Prerequisites
- **Operating System:** macOS 10.15+, Windows 10+, or Ubuntu 18.04+
- **Node.js:** Version 20.19.3 LTS (updated for Next.js compatibility)
- **Python:** Version 3.11 or higher
- **Docker:** Version 24.0+ with Docker Compose
- **PostgreSQL:** Version 15+ (or use Docker)
- **Redis:** Version 7.0+ (or use Docker)
- **Code Editor:** VS Code with recommended extensions

### Installation Steps

#### 1. Clone Repository
```bash
git clone https://github.com/404FoundingFather/jobapp.git
cd jobapp
```

#### 2. Install Dependencies
```bash
# Frontend dependencies (Next.js)
cd apps/web-frontend
npm install

# Backend dependencies (using Poetry)
cd ../api-gateway
poetry install

# Service dependencies
cd ../../services/job-discovery
poetry install

cd ../resume-processor
poetry install

cd ../cover-letter-gen
poetry install

cd ../automation-engine
poetry install
```

#### 3. Environment Configuration
```bash
# Copy environment template files
cp .env.example .env
cp apps/web-frontend/.env.example apps/web-frontend/.env.local
cp apps/api-gateway/.env.example apps/api-gateway/.env

# Edit environment files with your configuration
# See "Environment Variables" section below
```

#### 4. Database Setup
```bash
# Start database services with Docker
docker-compose up -d postgres redis

# Wait for services to be ready
sleep 10

# Initialize database and run migrations
cd apps/api-gateway
poetry run alembic upgrade head

# Seed development data (optional)
poetry run python scripts/seed_dev_data.py
```

#### 5. Start Development Servers
```bash
# Terminal 1: Frontend (Next.js)
cd apps/web-frontend
npm run dev

# Terminal 2: API Gateway (FastAPI)
cd apps/api-gateway
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 3: Background services (Celery)
cd services/job-discovery
poetry run celery -A app.celery_app worker --loglevel=info
```

### Verification Checklist
- [ ] Frontend accessible at http://localhost:3000
- [ ] API responding at http://localhost:8000/docs (FastAPI docs)
- [ ] Database connections working (check logs)
- [ ] Hot reload functional for both frontend and backend
- [ ] All environment variables loaded correctly
- [ ] Redis accessible at localhost:6379

## Environment Variables

### Frontend Environment Variables (.env.local)
```env
# Application Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_TITLE=Job Application Automation
NEXT_PUBLIC_APP_VERSION=0.1.0

# Authentication
NEXT_PUBLIC_AUTH_PROVIDER=jwt
NEXT_PUBLIC_AUTH_DOMAIN=localhost

# External Services
NEXT_PUBLIC_ANALYTICS_ID=GA-MEASUREMENT-ID
NEXT_PUBLIC_SENTRY_DSN=your-sentry-dsn

# Development Settings
NEXT_PUBLIC_DEBUG_MODE=true
NEXT_PUBLIC_LOG_LEVEL=debug

# Next.js Configuration
NODE_ENV=development
NEXT_TELEMETRY_DISABLED=1
```

### Backend Environment Variables (.env)
```env
# Server Configuration
ENVIRONMENT=development
PORT=8000
HOST=0.0.0.0
DEBUG=true

# Database Configuration
DATABASE_URL=postgresql://postgres:password@localhost:5432/jobapp_dev
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=jobapp_dev
DATABASE_USER=postgres
DATABASE_PASSWORD=password

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Authentication & Security
JWT_SECRET_KEY=your-super-secret-jwt-key-change-in-production
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
ENCRYPTION_KEY=your-32-character-encryption-key

# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7

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
HEADLESS_MODE=true

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/1

# Development Settings
LOG_LEVEL=debug
SQLALCHEMY_ECHO=false
```

### Security Notes
- Never commit `.env` files to version control
- Use different secrets for each environment
- Rotate secrets regularly in production
- Use environment-specific service accounts and API keys

## Development Tools

### Required Tools
- **Code Editor:** VS Code with recommended extensions:
  - **Python** - Python language support and debugging
  - **Pylance** - Enhanced Python IntelliSense
  - **ES7+ React/Redux/React-Native snippets** - React development snippets
  - **TypeScript Importer** - Auto import for TypeScript
  - **Tailwind CSS IntelliSense** - CSS class autocomplete
  - **Thunder Client** - API testing within VS Code
  - **Next.js Snippets** - Next.js development snippets
  - **ESLint** - JavaScript/TypeScript linting
  - **Prettier** - Code formatting

### Development Scripts
```json
{
  "scripts": {
    "dev": "next dev --host 0.0.0.0 --port 3000",
    "build": "next build",
    "start": "next start",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "next lint",
    "lint:fix": "next lint --fix",
    "format": "prettier --write \"**/*.{ts,tsx,js,jsx,json,css,md}\"",
    "type-check": "tsc --noEmit"
  }
}
```

## Database Configuration

### Local Database Setup
```bash
# PostgreSQL installation and setup (if not using Docker)
# macOS
brew install postgresql@15
brew services start postgresql@15

# Ubuntu
sudo apt-get install postgresql-15 postgresql-contrib-15
sudo systemctl start postgresql

# Create development database
createdb jobapp_dev

# Install pgvector extension
psql jobapp_dev -c "CREATE EXTENSION vector;"
```

### Database Connection Configuration
```python
# apps/api-gateway/app/core/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

engine = create_async_engine(
    DATABASE_URL,
    echo=os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true",
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=20,
    max_overflow=30
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
```

### Migration/Schema Commands
```bash
# Create new migration
cd apps/api-gateway
poetry run alembic revision --autogenerate -m "migration_name"

# Apply migrations
poetry run alembic upgrade head

# Rollback migrations
poetry run alembic downgrade -1

# Reset database
poetry run python scripts/reset_db.py
```

## PostgreSQL Configuration & Troubleshooting

### Docker PostgreSQL Setup

#### 1. Start PostgreSQL Container
```bash
# Start only PostgreSQL and Redis (avoiding missing Dockerfile.dev issues)
cd /Users/ehammond/Documents/src/jobapp
docker-compose up -d postgres redis

# Verify containers are running and healthy
docker ps | grep -E "(postgres|redis)"
```

#### 2. Database Initialization
The PostgreSQL container automatically runs initialization scripts:
- `scripts/init-db.sql` - Creates databases and users
- `scripts/init-extensions.sql` - Installs pgvector and other extensions

#### 3. Connect to PostgreSQL Container
```bash
# Connect as postgres user to jobapp_dev database
docker exec -it jobapp_postgres psql -U postgres -d jobapp_dev

# List all databases
\l

# List all users/roles
\du

# Connect to a specific database
\c jobapp_dev
```

### User Management & Permissions

#### Default Users Created
- **postgres** - Superuser (created by Docker image)
- **jobapp_user** - Application user (created by init-db.sql)

#### Granting Permissions to jobapp_user
```sql
-- Connect as postgres user first
docker exec -it jobapp_postgres psql -U postgres -d jobapp_dev

-- Grant schema usage and create permissions
GRANT USAGE ON SCHEMA public TO jobapp_user;
GRANT CREATE ON SCHEMA public TO jobapp_user;

-- Grant all privileges on all tables (current and future)
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO jobapp_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO jobapp_user;

-- Set default privileges for future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO jobapp_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO jobapp_user;

-- Alternative: Make jobapp_user the owner of public schema
ALTER SCHEMA public OWNER TO jobapp_user;
```

### Connection String Configuration

#### For Local Development (Outside Docker)
```python
# apps/api-gateway/app/core/config.py
DATABASE_URL: str = "postgresql+asyncpg://jobapp_user:jobapp_password@localhost:5432/jobapp_dev"
```

#### For Docker Compose Services
```python
# Inside Docker containers (use service name as host)
DATABASE_URL: str = "postgresql+asyncpg://jobapp_user:jobapp_password@postgres:5432/jobapp_dev"
```

### Common PostgreSQL Issues & Solutions

#### Issue 1: "role 'postgres' does not exist"
**Cause:** API gateway trying to connect to wrong PostgreSQL instance or wrong user
**Solution:**
```bash
# 1. Stop local Homebrew PostgreSQL (if running)
brew services stop postgresql

# 2. Verify Docker PostgreSQL is running
docker ps | grep postgres

# 3. Update DATABASE_URL to use jobapp_user instead of postgres
# In apps/api-gateway/app/core/config.py:
DATABASE_URL: str = "postgresql+asyncpg://jobapp_user:jobapp_password@localhost:5432/jobapp_dev"
```

#### Issue 2: "permission denied for schema public"
**Cause:** jobapp_user lacks permissions to create tables
**Solution:**
```sql
-- Connect as postgres user and grant permissions
docker exec -it jobapp_postgres psql -U postgres -d jobapp_dev

-- Grant all necessary permissions
GRANT USAGE ON SCHEMA public TO jobapp_user;
GRANT CREATE ON SCHEMA public TO jobapp_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO jobapp_user;

-- Or make jobapp_user the schema owner
ALTER SCHEMA public OWNER TO jobapp_user;
```

#### Issue 3: "invalid input syntax for type uuid: 'gen_random_uuid()'"
**Cause:** SQLAlchemy model using incorrect UUID default syntax
**Solution:**
```python
# In SQLAlchemy models, use text() wrapper for function calls
from sqlalchemy import text

# Correct syntax:
id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))

# Wrong syntax:
id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
```

#### Issue 4: Port conflicts between local and Docker PostgreSQL
**Cause:** Both local Homebrew PostgreSQL and Docker PostgreSQL trying to use port 5432
**Solution:**
```bash
# Option 1: Stop local PostgreSQL (recommended)
brew services stop postgresql

# Option 2: Change Docker port mapping
# In docker-compose.yml:
ports:
  - "5433:5432"  # Map Docker 5432 to host 5433

# Then update DATABASE_URL:
DATABASE_URL: str = "postgresql+asyncpg://jobapp_user:jobapp_password@localhost:5433/jobapp_dev"
```

### Database Verification Commands

#### Check Database Health
```bash
# Verify PostgreSQL container is healthy
docker ps | grep postgres

# Test database connection
docker exec -it jobapp_postgres pg_isready -U postgres -d jobapp_dev

# Check if pgvector extension is installed
docker exec -it jobapp_postgres psql -U postgres -d jobapp_dev -c "SELECT * FROM pg_extension WHERE extname = 'pgvector';"
```

#### Verify Tables Created
```bash
# Connect to database and list tables
docker exec -it jobapp_postgres psql -U jobapp_user -d jobapp_dev -c "\dt"

# Check specific table structure
docker exec -it jobapp_postgres psql -U jobapp_user -d jobapp_dev -c "\d users"
```

### Environment-Specific Configuration

#### Development Environment
```env
# .env file for local development
DATABASE_URL=postgresql+asyncpg://jobapp_user:jobapp_password@localhost:5432/jobapp_dev
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=jobapp_dev
DATABASE_USER=jobapp_user
DATABASE_PASSWORD=jobapp_password
```

#### Test Environment
```env
# .env.test file
DATABASE_URL=postgresql+asyncpg://jobapp_user:jobapp_password@localhost:5432/jobapp_test
DATABASE_NAME=jobapp_test
```

#### Production Environment
```env
# Production environment variables
DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
DATABASE_HOST=${DB_HOST}
DATABASE_PORT=${DB_PORT}
DATABASE_NAME=${DB_NAME}
DATABASE_USER=${DB_USER}
DATABASE_PASSWORD=${DB_PASSWORD}
```

### Database Reset Procedures

#### Complete Database Reset
```bash
# Stop all services
docker-compose down

# Remove PostgreSQL volume (WARNING: This deletes all data)
docker volume rm jobapp_postgres_data

# Restart services
docker-compose up -d postgres redis

# Wait for initialization
sleep 15

# Verify databases created
docker exec -it jobapp_postgres psql -U postgres -c "\l"
```

#### Reset Specific Database
```bash
# Drop and recreate specific database
docker exec -it jobapp_postgres psql -U postgres -c "DROP DATABASE IF EXISTS jobapp_dev;"
docker exec -it jobapp_postgres psql -U postgres -c "CREATE DATABASE jobapp_dev OWNER jobapp_user;"

# Re-run initialization scripts
docker exec -it jobapp_postgres psql -U postgres -d jobapp_dev -f /docker-entrypoint-initdb.d/01-init-db.sql
docker exec -it jobapp_postgres psql -U postgres -d jobapp_dev -f /docker-entrypoint-initdb.d/02-init-extensions.sql
```

## Testing Environment

### Test Environment Setup
```env
# Test-specific environment variables (.env.test)
ENVIRONMENT=test
DATABASE_URL=postgresql://postgres:password@localhost:5432/jobapp_test
DATABASE_NAME=jobapp_test
REDIS_URL=redis://localhost:6379/2
```

### Running Tests
```bash
# Run all tests
npm run test              # Frontend tests
poetry run pytest        # Backend tests

# Run specific test suite
npm run test JobCard      # Specific component tests
poetry run pytest tests/api/test_auth.py  # Specific API tests

# Run tests with coverage
npm run test:coverage
poetry run pytest --cov=app --cov-report=html

# Run end-to-end tests
npm run test:e2e
poetry run pytest tests/e2e/
```

### Test Data Management
```bash
# Setup test data
poetry run python tests/fixtures/setup_test_data.py

# Cleanup test data
poetry run python tests/fixtures/cleanup_test_data.py

# Reset test database
poetry run python tests/fixtures/reset_test_db.py
```

## Deployment

### Staging Deployment
**Trigger:** Push to `develop` branch  
**Process:** Automated via GitHub Actions
```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to Staging
on:
  push:
    branches: [develop]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          cd apps/web-frontend && npm ci
          cd ../api-gateway && poetry install
      - name: Run tests
        run: |
          cd apps/web-frontend && npm run test
          cd ../api-gateway && poetry run pytest
      - name: Build frontend
        run: cd apps/web-frontend && npm run build
      - name: Deploy to AWS ECS
        run: |
          aws ecs update-service --cluster staging --service jobapp-staging --force-new-deployment
```

### Production Deployment
**Trigger:** Push to `main` branch  
**Process:** 
1. Automated testing and security scanning
2. Build and tag Docker images
3. Update ECS service with blue-green deployment
4. Run health checks
5. Complete deployment or rollback

### Deployment Checklist
- [ ] All tests passing (frontend and backend)
- [ ] Code review completed and approved
- [ ] Database migrations tested in staging
- [ ] Environment variables updated for target environment
- [ ] Monitoring and alerts configured
- [ ] Rollback plan prepared and tested
- [ ] Stakeholders notified of deployment window

## Infrastructure

### Cloud Provider: AWS
- **Compute:** ECS Fargate for containerized microservices
- **Database:** RDS PostgreSQL 15 with pgvector extension
- **Storage:** S3 for resumes, cover letters, and generated documents
- **CDN:** CloudFront for static assets and API caching
- **Monitoring:** CloudWatch for logs, metrics, and alerting

### Resource Configuration
```yaml
# infrastructure/ecs-task-definition.json
production:
  frontend-service:
    cpu: 256
    memory: 512
    instances: 2
  api-gateway:
    cpu: 512
    memory: 1024
    instances: 3
  job-discovery-service:
    cpu: 1024
    memory: 2048
    instances: 2
  database:
    instance_type: db.t3.medium
    storage: 100GB
    backup_retention: 7_days
```

## Monitoring & Logging

### Application Monitoring
- **Performance:** AWS X-Ray for request tracing and performance monitoring
- **Errors:** Sentry for exception monitoring and alerting
- **Uptime:** AWS Route 53 health checks for availability monitoring
- **User Analytics:** Google Analytics 4 for user behavior tracking

### Log Aggregation
```python
# app/core/logging.py
import logging
import sys
from typing import Any, Dict

class StructuredFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_obj: Dict[str, Any] = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        if hasattr(record, "user_id"):
            log_obj["user_id"] = record.user_id
        if hasattr(record, "request_id"):
            log_obj["request_id"] = record.request_id
            
        return json.dumps(log_obj)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(StructuredFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

### Key Metrics to Monitor
- **Response Time:** API endpoint response times (target: <2s)
- **Error Rate:** Application error frequency (target: <1%)
- **Database Performance:** Query execution times and connection health
- **Resource Usage:** CPU, memory, disk, and network utilization
- **User Activity:** Active users, feature usage, application success rates

## Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Find process using port
lsof -i :3000    # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Kill process
kill -9 [process-id]         # macOS/Linux
taskkill /PID [process-id] /F  # Windows

# Alternative: Use different port
PORT=3001 npm run dev
```

#### Database Connection Issues
- Verify database service is running: `docker-compose ps`
- Check connection string and credentials in environment variables
- Ensure database exists: `psql -h localhost -U postgres -l`
- Verify network connectivity: `telnet localhost 5432`

#### Dependency Issues
```bash
# Clear npm cache
npm cache clean --force
rm -rf node_modules package-lock.json
npm install

# Clear Poetry cache
poetry cache clear . --all
rm poetry.lock
poetry install
```

#### Environment Variable Issues
- Verify `.env` files exist and have correct values
- Check environment variable naming matches exactly (case-sensitive)
- Restart development servers after changing environment variables
- Use `printenv | grep NEXT_` to check loaded variables

### Getting Help
- **Documentation:** https://github.com/your-org/jobapp/wiki
- **Team Communication:** Slack #jobapp-dev channel
- **Issue Tracker:** https://github.com/your-org/jobapp/issues
- **Code Repository:** https://github.com/your-org/jobapp

## Platform-Specific Notes

### Windows Development
- Use PowerShell or Git Bash for terminal commands
- Install Windows Subsystem for Linux (WSL2) for better compatibility
- Consider using Docker Desktop for Windows

### macOS Development  
- Install Homebrew for dependency management: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Use Terminal.app or iTerm2
- Consider using pyenv for Python version management

### Linux Development
- Use apt (Ubuntu/Debian) or yum (RHEL/CentOS) for system packages
- Ensure proper permissions for Docker: `sudo usermod -aG docker $USER`
- Consider using pyenv for Python version management

---
*Keep this environment documentation updated as infrastructure, tools, and setup processes evolve. Regular reviews ensure new team members can set up their development environment efficiently.* 