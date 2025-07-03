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

## Technology Stack Overview

### Frontend Technology Stack
- **Framework:** Next.js 14.2.30 (migrated from Vite for better React integration)
- **Language:** TypeScript 5.0+
- **Styling:** Tailwind CSS 3.3+ with shadcn/ui components
- **State Management:** Zustand 4.4+ for client-side state
- **Data Fetching:** TanStack React Query 5.0+ for server state
- **Forms:** React Hook Form 7.48+ with Zod validation
- **UI Components:** Radix UI primitives with custom styling
- **Icons:** Lucide React for consistent iconography
- **Routing:** Next.js App Router (file-based routing)

### Backend Technology Stack
- **Framework:** FastAPI 0.104+ with async/await support
- **Language:** Python 3.11+
- **Database:** PostgreSQL 15+ with pgvector extension for semantic search
- **Caching:** Redis 7.0+ for session storage and task queues
- **Authentication:** JWT tokens with secure password hashing
- **API Documentation:** Automatic OpenAPI/Swagger generation
- **Background Tasks:** Celery with Redis broker
- **Testing:** Pytest with async test support

### Development & DevOps
- **Package Management:** Poetry for Python, npm for Node.js
- **Containerization:** Docker & Docker Compose for development
- **CI/CD:** GitHub Actions with automated testing
- **Code Quality:** ESLint, Prettier, Black, Ruff
- **Version Control:** Git with conventional commits
- **Environment:** Node.js 20 LTS for frontend development

### AI/ML Integration
- **Language Models:** OpenAI GPT-4 for content generation
- **Embeddings:** Sentence transformers for semantic search
- **NLP Processing:** spaCy for text analysis
- **Vector Database:** PostgreSQL with pgvector extension

### Infrastructure (Production Ready)
- **Cloud Platform:** AWS (ECS/Fargate, RDS, ElastiCache, S3)
- **Load Balancing:** Application Load Balancer
- **Monitoring:** CloudWatch with custom metrics
- **Security:** IAM roles, VPC, security groups
- **SSL/TLS:** ACM certificates for HTTPS

## Development Environment

### Prerequisites
- **Node.js:** Version 20.19.3 LTS (updated from Node 22 for compatibility)
- **Python:** Version 3.11 or higher
- **Docker:** Version 24.0+ with Docker Compose
- **Git:** Version 2.30+

### Local Development Setup
```bash
# Frontend (Next.js)
cd apps/web-frontend
npm install
npm run dev  # Runs on http://localhost:3000

# Backend (FastAPI)
cd apps/api-gateway
poetry install
poetry run uvicorn app.main:app --reload  # Runs on http://localhost:8000

# Database & Redis
docker-compose up -d postgres redis
```

### Key Configuration Files
- **Frontend:** `apps/web-frontend/next.config.js`, `tsconfig.json`, `tailwind.config.js`
- **Backend:** `apps/api-gateway/pyproject.toml`, `alembic.ini`
- **Database:** `scripts/init-db.sql`, `scripts/init-extensions.sql`
- **Docker:** `docker-compose.yml`, `Dockerfile.dev` files

## Architecture Patterns

### Frontend Architecture
- **App Directory:** Next.js 13+ app directory structure
- **Component Library:** Reusable UI components with TypeScript
- **State Management:** Client state with Zustand, server state with React Query
- **Styling:** Utility-first CSS with Tailwind, component variants with CVA
- **Type Safety:** Full TypeScript integration with strict mode

### Backend Architecture
- **API Gateway:** FastAPI with dependency injection
- **Service Layer:** Business logic separation with async operations
- **Data Access:** SQLAlchemy with async support
- **Caching:** Redis for session and query caching
- **Background Jobs:** Celery for long-running tasks

### Data Architecture
- **Primary Database:** PostgreSQL with pgvector for embeddings
- **Caching Layer:** Redis for sessions and temporary data
- **File Storage:** S3-compatible storage for documents
- **Search:** Full-text search with semantic capabilities

## Performance & Scalability

### Frontend Optimization
- **Next.js Features:** Automatic code splitting, image optimization
- **Bundle Analysis:** Webpack bundle analyzer for size optimization
- **Caching:** Static generation and incremental static regeneration
- **Performance Monitoring:** Core Web Vitals tracking

### Backend Optimization
- **Async Operations:** Full async/await support for I/O operations
- **Database Optimization:** Connection pooling, query optimization
- **Caching Strategy:** Multi-level caching with Redis
- **Background Processing:** Celery for non-blocking operations

### Scalability Considerations
- **Horizontal Scaling:** Stateless API design for easy scaling
- **Database Scaling:** Read replicas and connection pooling
- **Caching Strategy:** Distributed caching with Redis
- **Load Balancing:** Application-level load balancing

## Security Considerations

### Frontend Security
- **Content Security Policy:** Strict CSP headers
- **Input Validation:** Client-side validation with Zod schemas
- **Authentication:** Secure token storage and refresh mechanisms
- **HTTPS:** Enforced HTTPS in production

### Backend Security
- **Authentication:** JWT with secure token handling
- **Authorization:** Role-based access control (RBAC)
- **Input Validation:** Pydantic models for request validation
- **SQL Injection:** Parameterized queries with SQLAlchemy
- **Rate Limiting:** API rate limiting and abuse prevention

### Infrastructure Security
- **Network Security:** VPC with security groups
- **Secrets Management:** Environment-based configuration
- **SSL/TLS:** End-to-end encryption
- **Monitoring:** Security event logging and alerting

## Testing Strategy

### Frontend Testing
- **Unit Tests:** Component testing with React Testing Library
- **Integration Tests:** API integration testing
- **E2E Tests:** Playwright for end-to-end testing
- **Type Checking:** TypeScript strict mode validation

### Backend Testing
- **Unit Tests:** Pytest for function and class testing
- **Integration Tests:** Database and API integration testing
- **Performance Tests:** Load testing with async operations
- **Security Tests:** Authentication and authorization testing

## Deployment Strategy

### Development Environment
- **Local Development:** Docker Compose for full stack
- **Hot Reloading:** Next.js and FastAPI development servers
- **Database:** Local PostgreSQL with pgvector
- **Caching:** Local Redis instance

### Production Environment
- **Container Orchestration:** AWS ECS with Fargate
- **Database:** AWS RDS with PostgreSQL
- **Caching:** AWS ElastiCache with Redis
- **Storage:** AWS S3 for file storage
- **CDN:** CloudFront for static assets
- **Monitoring:** CloudWatch with custom dashboards

## Migration Notes

### Recent Changes (July 2024)
- **Frontend Migration:** Successfully migrated from Vite to Next.js 14
- **Build System:** Resolved critical "can't detect preamble" error
- **Node.js Version:** Updated to Node.js 20 LTS for better compatibility
- **Routing:** Migrated from React Router to Next.js App Router
- **Configuration:** Updated PostCSS and TypeScript configs for Next.js

### Benefits of Next.js Migration
- **Better React Integration:** Native React support without plugin conflicts
- **Improved Performance:** Built-in optimizations and code splitting
- **Enhanced Developer Experience:** Better TypeScript support and debugging
- **Production Ready:** Optimized build process and deployment
- **File-based Routing:** Simpler and more intuitive routing system

---
*Technology choices are documented in docs/technical-decisions.md and should be reviewed quarterly for optimization opportunities.* 