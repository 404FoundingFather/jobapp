# Memory Bank Index

## Overview
This Memory Bank serves as the persistent memory system for the Job Application Assistance System project. It maintains continuity across AI sessions by documenting all crucial project information, patterns, and decisions for this specific job application assistance platform.

## Purpose
The Memory Bank is designed to overcome the challenge of AI memory resets between sessions. Each file contains essential project knowledge that allows any AI to quickly understand and continue development work effectively on the Job Application Assistance System.

## File Structure and Reading Order

### Core Documentation (Read First)
1. **00-index.md** (This file) - Navigation hub and overview
2. **01-productVision.md** - Job application assistance product goals and user experience
3. **02-techContext.md** - Python/FastAPI backend, Next.js/TypeScript frontend technology stack
4. **03-systemArchitecture.md** - Microservices architecture with AI/ML integration
5. **04-systemPatterns.md** - Implementation patterns for job assistance features

### Current Status (Read Second)
6. **08-kanban.md** - Current sprint status and task tracking
7. **09-changelog.md** - Project history and development milestones
8. **07-developmentPlan.md** - 20-week simplified MVP development roadmap

### Technical References (Read as Needed)
9. **05-database.md** - PostgreSQL schema with pgvector for semantic search
10. **06-uidesign.md** - Next.js/TypeScript UI components and design system
11. **10-environment.md** - Docker development environment and AWS deployment
12. **12-code-snippets.md** - Reusable patterns for job assistance features
13. **13-decisions.md** - Technical and architectural decisions
14. **14-quick-reference.md** - Commands, endpoints, and troubleshooting

### Meta-Documentation
15. **11-ai-interaction-guidelines.md** - AI workflow and preferences
16. **15-dev-readiness.md** - Development readiness checklist and implementation guide

## Project Context

### Job Application Assistance System (MVP)
This Memory Bank supports the development of an AI-powered job application assistance platform that:
- Discovers relevant jobs across multiple platforms (LinkedIn, Indeed, Glassdoor)
- Provides multi-select interface for job selection
- Automatically tailors resumes based on selected job requirements
- Generates personalized cover letters using AI with company research
- Creates application packages with job URL, tailored resume, and custom cover letter
- Enables manual application submission with AI-generated materials
- Provides comprehensive tracking and analytics

### Technology Stack
- **Frontend:** Next.js 14+ with TypeScript, Tailwind CSS, shadcn/ui
- **Backend:** Python 3.11+ with FastAPI, async architecture
- **Database:** PostgreSQL 15+ with pgvector extension for semantic search
- **ML/AI:** OpenAI GPT-4, sentence-transformers, spaCy for NLP
- **Infrastructure:** AWS ECS/Fargate, RDS, ElastiCache, S3

## How to Use This Memory Bank

### For New AI Sessions
1. Always start by reading files 1-5 (Core Documentation)
2. Check files 6-8 (Current Status) to understand current development phase
3. Reference technical files (9-14) as needed for implementation
4. Follow the workflow described in `11-ai-interaction-guidelines.md`

### Current Development Phase
- **Phase:** Sprint 0 - Pre-Development Setup (Weeks 1-2) - ✅ **COMPLETE**
- **Status:** All infrastructure files created, documentation complete, frontend working with Next.js
- **Focus:** Foundation & Core Infrastructure (Weeks 3-8) - Ready to begin
- **Next Phase:** User Management & Authentication implementation

## 🚀 **READY TO START DEVELOPMENT**
**All prerequisites completed. Frontend successfully migrated to Next.js and working. Ready to begin Phase 1 implementation.**

## Memory Bank Maintenance

### Regular Updates Required
- **Daily:** Kanban board status updates during active development
- **Weekly:** Development plan progress and sprint planning updates
- **Per Feature:** Changelog entries for completed job assistance features
- **Per Decision:** Architectural decision records for technical choices
- **Per Pattern:** Code snippets for discovered assistance patterns

### Project-Specific Maintenance
- **Job Discovery Updates:** Changes to scraping logic or new platform integrations
- **AI Integration Updates:** OpenAI API changes, prompt engineering improvements
- **Content Generation Updates:** Resume tailoring and cover letter improvements
- **Security Updates:** Authentication, authorization, and compliance changes

## Integration Benefits

### For AI Assistance
- **Persistent Context:** AI understands job assistance domain across sessions
- **Technology Awareness:** AI works with Python/FastAPI backend and Next.js frontend
- **Pattern Recognition:** AI follows established job assistance patterns
- **Decision Context:** AI understands why specific choices were made

### For Development Team
- **Living Documentation:** Always current job assistance system documentation
- **Onboarding:** New team members get comprehensive assistance platform overview
- **Knowledge Sharing:** Team expertise in job assistance captured in reusable patterns
- **Decision Tracking:** Historical record of assistance-specific technical choices

## Quick Navigation

### By Development Phase
- **Sprint 0 (Complete):** 08-kanban.md, 10-environment.md, 02-techContext.md
- **Foundation Phase:** 05-database.md, 03-systemArchitecture.md, 04-systemPatterns.md
- **Feature Development:** 12-code-snippets.md, 13-decisions.md, 06-uidesign.md
- **Deployment:** 10-environment.md, 07-developmentPlan.md

### By Feature Area
- **Job Discovery:** 03-systemArchitecture.md, 04-systemPatterns.md, 12-code-snippets.md
- **Resume Processing:** 04-systemPatterns.md, 05-database.md, 12-code-snippets.md
- **AI Content Generation:** 02-techContext.md, 04-systemPatterns.md, 13-decisions.md
- **Application Packages:** 04-systemPatterns.md, 13-decisions.md, 14-quick-reference.md

### By Role
- **AI Assistant:** Start with 01-productVision.md, then 08-kanban.md for current status
- **Frontend Developer:** Focus on 06-uidesign.md, 04-systemPatterns.md, 12-code-snippets.md
- **Backend Developer:** Focus on 03-systemArchitecture.md, 05-database.md, 04-systemPatterns.md
- **DevOps/Infrastructure:** Focus on 10-environment.md, 07-developmentPlan.md, 02-techContext.md

---
*This Memory Bank is specifically designed for the Job Application Assistance System project and should be updated regularly to reflect the current state of development and technical decisions.* 