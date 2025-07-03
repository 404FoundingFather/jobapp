# Architectural Decision Records (ADRs)

## AI Population Instructions
When working with this template:
- Replace the example ADRs with actual decisions made for your project
- Adapt the decision contexts and rationales to your specific technology choices
- Maintain the ADR structure while updating specific technology references
- Document all significant architectural and technical decisions following this format

## Overview
This file documents all significant architectural and technical decisions made during the Job Application Automation System project. Each decision record follows the ADR format to capture the context, decision, and consequences for future reference.

## Decision Record Template
```
## ADR-[NUMBER]: [Title]
**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Deprecated | Superseded
**Deciders:** [List of people involved in decision]

### Context
[Describe the situation and problem that prompted this decision]

### Decision
[Describe the decision made and why]

### Consequences
**Positive:**
- [List positive outcomes]

**Negative:**
- [List negative outcomes or trade-offs]

**Neutral:**
- [List other effects]

### Implementation Notes
[Any specific implementation details or guidelines]
```

---

## ADR-001: Python FastAPI Backend with React TypeScript Frontend
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** Project Lead, Tech Lead

### Context
Building a job application automation system requires a technology stack that supports:
- Complex ML/NLP operations for resume processing and job matching
- Real-time browser automation for application submission
- Scalable web application for user interaction
- Integration with multiple external APIs (OpenAI, job platforms)
- High-performance database operations with vector search

### Decision
Selected technology stack:
- **Backend:** Python 3.11+ with FastAPI for async API server
- **Frontend:** React 18+ with TypeScript 5.0+ for type safety
- **Build Tools:** Vite for fast frontend development, Poetry for Python dependency management
- **Styling:** Tailwind CSS with shadcn/ui component library
- **State Management:** Zustand for global state, React Query for server state

### Consequences
**Positive:**
- Python ecosystem provides excellent ML/NLP libraries (spaCy, sentence-transformers, scikit-learn)
- FastAPI offers automatic API documentation and excellent async support
- TypeScript provides type safety for complex API integrations
- Strong community support and extensive documentation
- Excellent tooling and IDE support for both stacks

**Negative:**
- Need to maintain two different language stacks (Python + TypeScript)
- Python GIL limitations for CPU-intensive tasks (mitigated by async I/O focus)
- Initial setup complexity with separate frontend/backend

**Neutral:**
- Team needs to maintain expertise in both Python and TypeScript ecosystems
- Requires establishing coding standards for both languages

### Implementation Notes
- Use Pydantic for request/response validation and automatic OpenAPI schema generation
- Implement CORS middleware for frontend-backend communication
- Set up comprehensive type definitions shared between frontend and backend
- Use async/await patterns throughout for optimal I/O performance

---

## ADR-002: Migration from Vite to Next.js Frontend Framework
**Date:** 2024-07-XX  
**Status:** Accepted  
**Deciders:** Project Lead, Frontend Developer

### Context
The project initially used Vite with React for the frontend, but encountered critical build issues:
- "can't detect preamble" error preventing frontend from rendering
- React version conflicts between React 18 and React 19 (from Radix UI dependencies)
- Vite plugin conflicts between @vitejs/plugin-react and @vitejs/plugin-react-swc
- Dependency resolution issues that were difficult to resolve without major changes

### Decision
Migrated from Vite to Next.js 14 for the frontend framework:
- **Framework:** Next.js 14.2.30 with App Router
- **Build System:** Next.js built-in build system replacing Vite
- **Routing:** File-based routing replacing React Router
- **Development:** Next.js dev server replacing Vite dev server
- **Configuration:** next.config.js replacing vite.config.ts

### Consequences
**Positive:**
- Resolved critical "can't detect preamble" build error
- Eliminated React version conflicts and dependency issues
- Better React integration with native Next.js support
- Improved performance with built-in optimizations and code splitting
- Enhanced developer experience with better TypeScript support
- Production-ready build process with optimized deployment
- File-based routing system is more intuitive and maintainable

**Negative:**
- Required migration effort and code changes
- Different configuration patterns and development workflow
- Learning curve for team members familiar with Vite
- Slightly different deployment process

**Neutral:**
- Both frameworks are well-supported and mature
- Migration was completed successfully with minimal disruption
- Future development will follow Next.js patterns and conventions

### Implementation Notes
- Updated all components to use Next.js Link component instead of React Router
- Migrated from useLocation to usePathname for navigation state
- Updated environment variables from VITE_ prefix to NEXT_PUBLIC_ prefix
- Configured PostCSS for Next.js compatibility
- Updated TypeScript configuration for Next.js requirements
- All pages now use Next.js app directory structure

---

## ADR-003: PostgreSQL with pgvector for Semantic Job Matching
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** Backend Lead, Database Administrator

### Context
The job discovery service requires semantic similarity matching between user profiles and job postings. Traditional SQL databases cannot efficiently handle vector similarity searches, while pure vector databases lack ACID guarantees needed for user data management.

### Decision
Adopted PostgreSQL 15+ with pgvector extension:
- **Primary Database:** PostgreSQL for all structured data (users, jobs, applications)
- **Vector Search:** pgvector extension for embedding storage and similarity search
- **Embedding Model:** sentence-transformers 'all-MiniLM-L6-v2' (384 dimensions)
- **Indexing Strategy:** IVFFlat indexes for vector similarity with cosine distance

### Consequences
**Positive:**
- Single database solution reduces infrastructure complexity
- ACID guarantees for critical user and financial data
- Native vector operations with acceptable performance (<2s for similarity search)
- Familiar SQL interface for complex queries combining structured and vector data
- Excellent backup, replication, and monitoring tools available

**Negative:**
- Vector search performance not as optimal as specialized vector databases
- Limited to 2000 dimensions per vector (sufficient for current needs)
- Requires PostgreSQL 15+ with extension installation

**Neutral:**
- Need to optimize vector index parameters for dataset size
- Regular index maintenance and performance tuning required
- May need to evaluate specialized vector databases at scale

### Implementation Notes
- Use cosine distance for similarity calculations: `ORDER BY embedding <=> query_vector`
- Set `ivfflat.probes = 10` for balance between speed and accuracy
- Create separate indexes for different types of embeddings (job, user profile, skills)
- Monitor query performance and adjust index lists parameter based on data volume

---

## ADR-004: Microservices Architecture with Event-Driven Orchestration
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** Tech Lead, System Architect

### Context
The job application automation system has distinct domains (job discovery, resume processing, content generation, browser automation) with different scaling requirements and technology needs. A monolithic approach would couple these disparate concerns.

### Decision
Implemented microservices architecture with event-driven communication:
- **API Gateway:** FastAPI gateway for unified frontend interface
- **Core Services:** Job Discovery, Resume Processor, Cover Letter Generator, Application Automation
- **Communication:** Redis pub/sub for event-driven workflows
- **Orchestration:** Celery for background task processing
- **Data Isolation:** Each service owns its domain data

### Consequences
**Positive:**
- Independent scaling based on service load patterns
- Technology flexibility per service (ML libraries for NLP services)
- Clear separation of concerns and domain boundaries
- Fault isolation prevents cascade failures
- Parallel development of different services

**Negative:**
- Increased operational complexity with multiple services
- Network latency for inter-service communication
- Distributed system challenges (eventual consistency, coordination)
- More complex testing and debugging

**Neutral:**
- Need to establish service communication patterns and error handling
- Requires comprehensive monitoring and observability
- Team coordination needed for API contracts

### Implementation Notes
- Use domain events for loose coupling: `job.discovered`, `resume.tailored`, `application.submitted`
- Implement circuit breaker pattern for service resilience
- Each service maintains its own database schema within shared PostgreSQL instance
- Use correlation IDs for request tracing across services

---

## ADR-005: OpenAI GPT-4 for Content Generation with Local Fallbacks
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** AI/ML Lead, Product Lead

### Context
Cover letter generation and resume optimization require high-quality, personalized content. Options include local open-source models, cloud AI services, or hybrid approaches. Quality requirements favor advanced models, but cost and latency are important considerations.

### Decision
Hybrid approach with OpenAI GPT-4 as primary and local models as backup:
- **Primary:** OpenAI GPT-4 for cover letter generation and content optimization
- **Backup:** Local Llama 2 or similar for cost-sensitive operations
- **Optimization:** Aggressive caching, prompt optimization, and usage monitoring
- **Cost Control:** Usage limits, quality scoring, and user tier restrictions

### Consequences
**Positive:**
- Excellent content quality comparable to human-written cover letters
- Reliable API with good uptime and support
- Comprehensive prompt engineering capabilities
- Strong content safety and filtering

**Negative:**
- High operational costs ($0.03 per 1k tokens for GPT-4)
- External dependency with potential rate limiting
- Data privacy considerations with third-party processing
- Potential latency issues for real-time generation

**Neutral:**
- Need to implement cost monitoring and budget controls
- Requires prompt engineering expertise and optimization
- May need to evaluate alternative models as they improve

### Implementation Notes
- Implement token counting and cost tracking for all requests
- Use structured prompts with clear templates and variables
- Cache generated content aggressively (1 hour+ for similar job/user combinations)
- Implement quality scoring to validate generated content
- Set up usage alerts and circuit breakers for cost protection

---

## ADR-006: Playwright for Browser Automation with Anti-Detection
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** Automation Lead, Tech Lead

### Context
Automated job application submission requires reliable browser automation that can handle modern web applications while avoiding detection by anti-bot systems. Traditional tools like Selenium have limited anti-detection capabilities.

### Decision
Selected Playwright with comprehensive anti-detection measures:
- **Framework:** Playwright with Chromium for consistent behavior
- **Anti-Detection:** User agent rotation, JavaScript injection, behavioral simulation
- **Stealth Measures:** Request timing randomization, mouse movement simulation
- **Session Management:** Persistent browser sessions with cookie management

### Consequences
**Positive:**
- Modern web app support with better performance than Selenium
- Built-in anti-detection capabilities and stealth mode
- Excellent debugging tools and screenshot capabilities
- Reliable handling of dynamic content and SPAs
- Good documentation and community support

**Negative:**
- Still susceptible to advanced bot detection systems
- Requires ongoing maintenance for platform-specific adaptations
- Resource intensive with multiple browser instances
- Potential legal and ethical considerations with automation

**Neutral:**
- Need to implement respectful rate limiting and user agent rotation
- Requires monitoring for detection events and adaptation
- Must maintain compliance with platform terms of service

### Implementation Notes
- Implement human-like timing patterns: random delays between 500ms-2s
- Rotate user agents and browser fingerprints for each session
- Use residential proxies for additional anonymity when necessary
- Implement graceful degradation when automation fails
- Monitor success rates and adapt strategies based on platform changes

---

## ADR-007: JWT Authentication with Redis Session Management
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** Security Lead, Backend Lead

### Context
The application requires secure authentication that supports both web and potential mobile clients. Need to balance security, scalability, and user experience while supporting features like session management and token revocation.

### Decision
Implemented JWT tokens with Redis-backed session management:
- **Authentication:** JWT access tokens with 30-minute expiration
- **Refresh Strategy:** Long-lived refresh tokens stored in Redis
- **Session Management:** Redis for active session tracking and revocation
- **Security:** HttpOnly cookies for web clients, Authorization header for API clients

### Consequences
**Positive:**
- Stateless authentication scales well across multiple service instances
- Fine-grained session control with immediate revocation capability
- Good performance with Redis caching layer
- Supports both web and API clients effectively

**Negative:**
- Requires Redis infrastructure for session management
- Token size larger than simple session IDs
- Complexity in handling token refresh logic

**Neutral:**
- Need to implement secure token storage on client side
- Regular monitoring of Redis memory usage and session cleanup
- Token rotation strategy for enhanced security

### Implementation Notes
- Use RS256 algorithm with key rotation every 90 days
- Implement automatic token refresh 5 minutes before expiration
- Store minimal user claims in JWT, fetch additional data from database
- Set up Redis TTL matching token expiration times
- Implement comprehensive logout that clears both tokens and Redis sessions

---

## ADR-008: Celery with Redis for Background Task Processing
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** Backend Lead, Infrastructure Lead

### Context
Job application processing involves multiple time-consuming operations (resume generation, cover letter creation, application submission) that should not block user interactions. Need reliable background processing with retry capabilities and monitoring.

### Decision
Implemented Celery task queue with Redis as both broker and result backend:
- **Task Queue:** Celery for async job processing and workflow orchestration
- **Broker:** Redis for task message passing and result storage
- **Workers:** Separate worker processes for different task types
- **Monitoring:** Flower for task monitoring and management

### Consequences
**Positive:**
- Reliable task execution with automatic retry and error handling
- Horizontal scaling through additional worker processes
- Good monitoring and debugging capabilities
- Mature ecosystem with excellent documentation

**Negative:**
- Additional infrastructure complexity with worker management
- Redis memory usage for task storage and results
- Potential task serialization/deserialization overhead

**Neutral:**
- Need to implement task routing and priority management
- Regular monitoring of queue lengths and worker health
- Backup strategy for task persistence

### Implementation Notes
- Use different queues for different priority levels: `high`, `normal`, `low`
- Implement exponential backoff for failed tasks with max 3 retries
- Set up task result expiration to manage Redis memory usage
- Use task routing to direct CPU-intensive tasks to dedicated workers
- Implement comprehensive logging and alerting for failed tasks

---

## ADR-009: React Query for Server State Management
**Date:** 2024-01-XX  
**Status:** Accepted  
**Deciders:** Frontend Lead, UX Lead

### Context
The job application dashboard requires efficient management of server state (jobs, applications, user data) with features like caching, background updates, and optimistic updates. Traditional state management solutions don't handle server state well.

### Decision
Adopted React Query (TanStack Query) for server state management:
- **Server State:** React Query for API data caching and synchronization
- **Global State:** Zustand for application state (UI state, user preferences)
- **Form State:** React Hook Form for form handling and validation
- **Caching Strategy:** Stale-while-revalidate with intelligent background updates

### Consequences
**Positive:**
- Excellent developer experience with automatic caching and synchronization
- Reduced API calls through intelligent caching strategies
- Built-in loading states, error handling, and retry logic
- Optimistic updates improve perceived performance

**Negative:**
- Additional learning curve for React Query concepts
- Memory usage for cached data (manageable with proper configuration)
- Need to design cache invalidation strategies

**Neutral:**
- Requires thoughtful query key design for effective caching
- Need to balance cache duration with data freshness requirements
- Integration with error handling and user feedback systems

### Implementation Notes
- Use hierarchical query keys: `['jobs', 'search', searchParams]`
- Set stale time to 5 minutes for job data, 1 hour for static data
- Implement optimistic updates for user actions (save job, update application status)
- Use query invalidation for related data updates
- Set up global error handling for API failures

---

## ADR-010: FastAPI Gateway Implementation with Comprehensive Health Monitoring
**Date:** 2024-06-18  
**Status:** Accepted  
**Deciders:** Backend Lead, DevOps Lead

### Context
During Sprint 0 implementation of the FastAPI gateway, several technical decisions were required around database connectivity, health monitoring, middleware architecture, and development environment setup. The goal was to create a production-ready API foundation with comprehensive observability.

### Decision
Implemented FastAPI gateway with the following technical choices:
- **Async Database Pattern:** SQLAlchemy async with AsyncSession and connection pooling
- **Health Check Strategy:** Multi-service health monitoring with Kubernetes-style endpoints
- **Middleware Stack:** Custom logging middleware with request timing and error handling
- **Database Health Check:** Docker exec workaround for authentication issues during development
- **Configuration Management:** Pydantic Settings with environment variable support
- **Redis Integration:** Async Redis client with connection pooling and health monitoring

### Consequences
**Positive:**
- Production-ready async FastAPI application with excellent performance characteristics
- Comprehensive health monitoring enables effective system observability
- Request/response logging provides valuable debugging and performance insights
- Kubernetes-style endpoints (/ready, /live) support container orchestration
- Database and Redis health checks enable proactive issue detection
- Modular middleware design allows easy addition of features like rate limiting

**Negative:**
- Database authentication workaround using Docker exec is not production-suitable
- Additional complexity in async database session management
- Redis connection pooling requires careful memory management
- Multiple health check endpoints increase API surface area

**Neutral:**
- Need to resolve database authentication for production deployment
- Requires monitoring setup to leverage health check endpoints effectively
- Middleware ordering becomes important for request processing pipeline

### Implementation Notes
- Database health check uses `docker exec jobapp_postgres psql -U postgres -d jobapp_dev -c 'SELECT 1'` as temporary workaround
- Health check endpoints return structured JSON with service status and response times
- Logging middleware adds X-Process-Time header for client-side performance monitoring
- Redis client implements connection pooling with 20 max connections
- All async operations use proper session management with try/finally blocks
- CORS configuration supports both localhost:3000 and 127.0.0.1:3000 for development

### Production Readiness Checklist
- [ ] Resolve database authentication issue for direct async connections
- [ ] Replace Docker exec health check with proper async database connection
- [ ] Add rate limiting middleware for API protection
- [ ] Implement structured logging with correlation IDs
- [ ] Set up monitoring dashboards for health check endpoints
- [ ] Configure alerts for service degradation

---

## Decision Impact Assessment

### High Impact Decisions
- **Technology Stack (ADR-001):** Fundamental choice affecting all development
- **Database Architecture (ADR-003):** Core data strategy with performance implications
- **Microservices Design (ADR-004):** System architecture affecting scalability and development

### Medium Impact Decisions
- **AI Integration (ADR-005):** Feature quality and operational costs
- **Browser Automation (ADR-006):** Core functionality success and legal compliance
- **Authentication Strategy (ADR-007):** Security and user experience

### Lower Impact Decisions
- **Background Processing (ADR-008):** Performance and system reliability
- **State Management (ADR-009):** Frontend development efficiency and UX

## Decision Review Schedule

### Quarterly Reviews
- Evaluate technology stack performance and ecosystem changes
- Assess AI model alternatives and cost optimization opportunities
- Review browser automation effectiveness and platform adaptations

### Semi-Annual Reviews
- Database performance analysis and potential migration considerations
- Security framework assessment and compliance updates
- Infrastructure scaling decisions and cloud optimization

### Annual Reviews
- Complete architecture assessment for scalability and maintainability
- Technology stack evaluation for major version upgrades
- Cost analysis and optimization across all service decisions

## Lessons Learned

### What Worked Well
- Early decision to use Python for ML ecosystem integration proved valuable
- PostgreSQL with pgvector provides good balance of features and performance
- Microservices architecture enables independent team development
- React Query significantly improved frontend development experience

### Areas for Improvement
- Need better cost monitoring for OpenAI API usage from the start
- Browser automation detection avoidance requires ongoing research and adaptation
- Microservices coordination could benefit from better service mesh tooling
- Database vector search performance needs monitoring as data grows

### Future Considerations
- Evaluate serverless computing for cost optimization of variable workloads
- Consider GraphQL for more efficient API consumption patterns
- Investigate newer vector database solutions as they mature
- Plan for multi-region deployment and data residency requirements

---
*This document captures the reasoning behind all major technical decisions and should be consulted when making related choices or considering changes to the system architecture.* 