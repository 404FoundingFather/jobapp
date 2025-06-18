# Database Schema & Data Models

## Database Technology
**Primary Database:** PostgreSQL 15+ with pgvector extension  
**Caching Layer:** Redis 7.0+ for sessions and application cache  
**File Storage:** AWS S3 for documents (resumes, cover letters, generated files)

**Database Design Philosophy:** Domain-driven design with clear service boundaries, optimized for read-heavy workloads with intelligent caching strategies.

---

## Core Domain Models

### User Management Domain

#### users
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    subscription_tier VARCHAR(20) DEFAULT 'free',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_active ON users(is_active);
```

#### user_profiles
```sql
CREATE TABLE user_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    resume_file_url VARCHAR(500),
    resume_text TEXT,
    linkedin_url VARCHAR(255),
    github_url VARCHAR(255),
    portfolio_url VARCHAR(255),
    phone VARCHAR(20),
    location_city VARCHAR(100),
    location_state VARCHAR(50),
    location_country VARCHAR(50),
    willing_to_relocate BOOLEAN DEFAULT false,
    years_experience INTEGER,
    current_title VARCHAR(200),
    target_salary_min INTEGER,
    target_salary_max INTEGER,
    preferred_work_type VARCHAR(20), -- remote, hybrid, onsite
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_user_profiles_user_id ON user_profiles(user_id);
```

#### user_skills
```sql
CREATE TABLE user_skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    skill_name VARCHAR(100) NOT NULL,
    skill_category VARCHAR(50), -- technical, soft, language, certification
    proficiency_level VARCHAR(20), -- beginner, intermediate, advanced, expert
    years_experience DECIMAL(3,1),
    is_primary BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_user_skills_user_id ON user_skills(user_id);
CREATE INDEX idx_user_skills_category ON user_skills(skill_category);
CREATE INDEX idx_user_skills_name ON user_skills(skill_name);
```

#### user_experiences
```sql
CREATE TABLE user_experiences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    company_name VARCHAR(200) NOT NULL,
    job_title VARCHAR(200) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT false,
    description TEXT,
    achievements TEXT[],
    technologies_used TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_user_experiences_user_id ON user_experiences(user_id);
CREATE INDEX idx_user_experiences_current ON user_experiences(is_current);
```

---

### Job Discovery Domain

#### companies
```sql
CREATE TABLE companies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255),
    industry VARCHAR(100),
    size_category VARCHAR(20), -- startup, small, medium, large, enterprise
    headquarters_city VARCHAR(100),
    headquarters_country VARCHAR(50),
    description TEXT,
    logo_url VARCHAR(500),
    career_page_url VARCHAR(500),
    glassdoor_rating DECIMAL(3,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_companies_name ON companies(name);
CREATE INDEX idx_companies_domain ON companies(domain);
CREATE INDEX idx_companies_industry ON companies(industry);
```

#### job_postings
```sql
CREATE TABLE job_postings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id VARCHAR(255), -- ID from the source platform
    company_id UUID REFERENCES companies(id),
    title VARCHAR(300) NOT NULL,
    description TEXT NOT NULL,
    requirements TEXT,
    benefits TEXT,
    salary_min INTEGER,
    salary_max INTEGER,
    salary_currency VARCHAR(3) DEFAULT 'USD',
    experience_level VARCHAR(20), -- entry, mid, senior, lead, executive
    employment_type VARCHAR(20), -- full-time, part-time, contract, internship
    work_arrangement VARCHAR(20), -- remote, hybrid, onsite
    location_city VARCHAR(100),
    location_state VARCHAR(50),
    location_country VARCHAR(50),
    source_platform VARCHAR(50) NOT NULL, -- linkedin, indeed, glassdoor
    source_url VARCHAR(1000) NOT NULL,
    posted_date DATE,
    expires_date DATE,
    is_active BOOLEAN DEFAULT true,
    required_skills TEXT[],
    preferred_skills TEXT[],
    embedding VECTOR(384), -- for semantic similarity search
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_job_postings_company_id ON job_postings(company_id);
CREATE INDEX idx_job_postings_active ON job_postings(is_active);
CREATE INDEX idx_job_postings_source ON job_postings(source_platform);
CREATE INDEX idx_job_postings_location ON job_postings(location_city, location_state);
CREATE INDEX idx_job_postings_experience ON job_postings(experience_level);
CREATE INDEX idx_job_postings_work_type ON job_postings(work_arrangement);
CREATE INDEX idx_job_postings_posted_date ON job_postings(posted_date);

-- Vector similarity index for semantic search
CREATE INDEX idx_job_postings_embedding ON job_postings USING ivfflat (embedding vector_cosine_ops);
```

#### job_search_preferences
```sql
CREATE TABLE job_search_preferences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    search_name VARCHAR(100) NOT NULL,
    target_titles TEXT[], -- array of job titles to search for
    excluded_titles TEXT[], -- titles to exclude
    target_companies TEXT[], -- preferred companies
    excluded_companies TEXT[], -- companies to avoid
    min_salary INTEGER,
    max_salary INTEGER,
    experience_levels TEXT[], -- array of acceptable experience levels
    work_arrangements TEXT[], -- remote, hybrid, onsite
    employment_types TEXT[], -- full-time, contract, etc.
    locations TEXT[], -- preferred locations
    keywords TEXT[], -- must-have keywords
    excluded_keywords TEXT[], -- keywords to avoid
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_job_search_prefs_user_id ON job_search_preferences(user_id);
CREATE INDEX idx_job_search_prefs_active ON job_search_preferences(is_active);
```

---

### Application Management Domain

#### applications
```sql
CREATE TABLE applications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    job_posting_id UUID REFERENCES job_postings(id),
    company_name VARCHAR(255) NOT NULL,
    job_title VARCHAR(300) NOT NULL,
    job_url VARCHAR(1000),
    status VARCHAR(50) DEFAULT 'pending', -- pending, submitted, reviewing, interviewed, rejected, offered
    application_method VARCHAR(50), -- automated, manual, referral
    submitted_at TIMESTAMP WITH TIME ZONE,
    last_status_update TIMESTAMP WITH TIME ZONE,
    tailored_resume_url VARCHAR(500),
    cover_letter_url VARCHAR(500),
    notes TEXT,
    follow_up_date DATE,
    interview_dates TIMESTAMP WITH TIME ZONE[],
    rejection_reason VARCHAR(500),
    offer_salary INTEGER,
    offer_details JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_applications_user_id ON applications(user_id);
CREATE INDEX idx_applications_status ON applications(status);
CREATE INDEX idx_applications_submitted_at ON applications(submitted_at);
CREATE INDEX idx_applications_job_posting_id ON applications(job_posting_id);
```

#### application_status_history
```sql
CREATE TABLE application_status_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    application_id UUID NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL,
    notes TEXT,
    changed_by VARCHAR(50), -- system, user, automatic
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_app_status_history_app_id ON application_status_history(application_id);
CREATE INDEX idx_app_status_history_created_at ON application_status_history(created_at);
```

#### generated_content
```sql
CREATE TABLE generated_content (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    application_id UUID NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
    content_type VARCHAR(50) NOT NULL, -- resume, cover_letter, follow_up_email
    content_text TEXT,
    file_url VARCHAR(500),
    generation_prompt TEXT,
    model_used VARCHAR(50),
    generation_metadata JSONB,
    user_approved BOOLEAN DEFAULT false,
    user_edited BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_generated_content_app_id ON generated_content(application_id);
CREATE INDEX idx_generated_content_type ON generated_content(content_type);
```

---

### Automation & Tasks Domain

#### automation_tasks
```sql
CREATE TABLE automation_tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    application_id UUID REFERENCES applications(id),
    task_type VARCHAR(50) NOT NULL, -- job_discovery, resume_generation, cover_letter_generation, application_submission
    status VARCHAR(50) DEFAULT 'pending', -- pending, running, completed, failed, cancelled
    priority INTEGER DEFAULT 5, -- 1-10, higher is more priority
    scheduled_at TIMESTAMP WITH TIME ZONE,
    started_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    retry_count INTEGER DEFAULT 0,
    max_retries INTEGER DEFAULT 3,
    error_message TEXT,
    task_config JSONB,
    result_data JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_automation_tasks_user_id ON automation_tasks(user_id);
CREATE INDEX idx_automation_tasks_status ON automation_tasks(status);
CREATE INDEX idx_automation_tasks_type ON automation_tasks(task_type);
CREATE INDEX idx_automation_tasks_scheduled_at ON automation_tasks(scheduled_at);
```

#### browser_sessions
```sql
CREATE TABLE browser_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    platform VARCHAR(50) NOT NULL, -- linkedin, indeed, workday, greenhouse
    session_data JSONB,
    cookies TEXT,
    user_agent VARCHAR(500),
    proxy_config JSONB,
    is_active BOOLEAN DEFAULT true,
    last_used_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_browser_sessions_user_id ON browser_sessions(user_id);
CREATE INDEX idx_browser_sessions_platform ON browser_sessions(platform);
CREATE INDEX idx_browser_sessions_active ON browser_sessions(is_active);
```

---

### Analytics & Metrics Domain

#### user_analytics
```sql
CREATE TABLE user_analytics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    metric_date DATE NOT NULL,
    applications_submitted INTEGER DEFAULT 0,
    jobs_discovered INTEGER DEFAULT 0,
    resumes_generated INTEGER DEFAULT 0,
    cover_letters_generated INTEGER DEFAULT 0,
    interviews_scheduled INTEGER DEFAULT 0,
    offers_received INTEGER DEFAULT 0,
    response_rate DECIMAL(5,4), -- percentage as decimal
    time_saved_minutes INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_user_analytics_user_id ON user_analytics(user_id);
CREATE INDEX idx_user_analytics_date ON user_analytics(metric_date);
```

#### platform_metrics
```sql
CREATE TABLE platform_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    platform_name VARCHAR(50) NOT NULL,
    metric_date DATE NOT NULL,
    total_jobs_scraped INTEGER DEFAULT 0,
    successful_scrapes INTEGER DEFAULT 0,
    failed_scrapes INTEGER DEFAULT 0,
    rate_limit_hits INTEGER DEFAULT 0,
    detection_events INTEGER DEFAULT 0,
    average_response_time_ms INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_platform_metrics_platform ON platform_metrics(platform_name);
CREATE INDEX idx_platform_metrics_date ON platform_metrics(metric_date);
```

---

## Data Relationships & Constraints

### Primary Relationships
```sql
-- One user can have multiple applications
-- One job posting can have multiple applications (from different users)
-- One application can have multiple generated content items
-- One user can have multiple automation tasks
-- One application can trigger multiple automation tasks

-- Ensure data integrity
ALTER TABLE user_profiles ADD CONSTRAINT unique_user_profile UNIQUE (user_id);
ALTER TABLE applications ADD CONSTRAINT valid_application_status 
    CHECK (status IN ('pending', 'submitted', 'reviewing', 'interviewed', 'rejected', 'offered', 'withdrawn'));
ALTER TABLE automation_tasks ADD CONSTRAINT valid_task_status 
    CHECK (status IN ('pending', 'running', 'completed', 'failed', 'cancelled'));
```

### Data Validation Rules
```sql
-- Email validation
ALTER TABLE users ADD CONSTRAINT valid_email 
    CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

-- Salary ranges
ALTER TABLE job_postings ADD CONSTRAINT valid_salary_range 
    CHECK (salary_min IS NULL OR salary_max IS NULL OR salary_min <= salary_max);

-- Experience validation
ALTER TABLE user_profiles ADD CONSTRAINT valid_experience 
    CHECK (years_experience >= 0 AND years_experience <= 70);

-- Date constraints
ALTER TABLE user_experiences ADD CONSTRAINT valid_date_range 
    CHECK (start_date <= COALESCE(end_date, CURRENT_DATE));
```

---

## Indexing Strategy

### Performance Indexes
```sql
-- Composite indexes for common query patterns
CREATE INDEX idx_jobs_location_experience ON job_postings(location_city, experience_level, is_active);
CREATE INDEX idx_apps_user_status_date ON applications(user_id, status, created_at);
CREATE INDEX idx_tasks_status_priority ON automation_tasks(status, priority, scheduled_at);

-- Full-text search indexes
CREATE INDEX idx_job_postings_fts ON job_postings USING gin(to_tsvector('english', title || ' ' || description));
CREATE INDEX idx_companies_fts ON companies USING gin(to_tsvector('english', name || ' ' || COALESCE(description, '')));

-- Partial indexes for active records
CREATE INDEX idx_active_job_postings ON job_postings(created_at) WHERE is_active = true;
CREATE INDEX idx_pending_tasks ON automation_tasks(created_at) WHERE status = 'pending';
```

### Vector Search Optimization
```sql
-- Optimize vector search performance
SET ivfflat.probes = 10;

-- Create specialized indexes for different similarity searches
CREATE INDEX idx_job_embeddings_cosine ON job_postings USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

---

## Data Access Patterns

### Common Query Patterns
```sql
-- Find relevant jobs for a user
SELECT jp.*, c.name as company_name,
       (jp.embedding <=> %s::vector) as similarity_score
FROM job_postings jp
JOIN companies c ON jp.company_id = c.id
WHERE jp.is_active = true
  AND jp.location_city = ANY(%s)
  AND jp.experience_level = ANY(%s)
ORDER BY jp.embedding <=> %s::vector
LIMIT 50;

-- Get user's application pipeline
SELECT a.*, jp.title, c.name as company_name
FROM applications a
LEFT JOIN job_postings jp ON a.job_posting_id = jp.id
LEFT JOIN companies c ON jp.company_id = c.id
WHERE a.user_id = %s
ORDER BY a.created_at DESC;

-- User analytics dashboard
SELECT 
    DATE_TRUNC('week', created_at) as week,
    COUNT(*) as applications_count,
    COUNT(*) FILTER (WHERE status IN ('interviewed', 'offered')) as positive_responses
FROM applications
WHERE user_id = %s
GROUP BY week
ORDER BY week DESC;
```

### Caching Strategy
```sql
-- Redis cache keys for frequent queries
-- user:profile:{user_id} - User profile data
-- jobs:recommendations:{user_id} - Recommended jobs for user
-- applications:status:{user_id} - Current application statuses
-- analytics:daily:{user_id}:{date} - Daily user analytics
```

---

## Data Migration & Versioning

### Migration Management
```sql
-- Version tracking table
CREATE TABLE schema_migrations (
    version VARCHAR(255) PRIMARY KEY,
    applied_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Example migration structure
-- migrations/001_initial_schema.sql
-- migrations/002_add_vector_search.sql
-- migrations/003_add_analytics_tables.sql
```

### Data Backup Strategy
- **Full Backups:** Daily automated backups with 30-day retention
- **Point-in-Time Recovery:** WAL archiving for precise recovery
- **Cross-Region Replication:** Disaster recovery with read replicas
- **Data Export:** User data portability in JSON/CSV formats

---

## Security & Privacy

### Data Encryption
```sql
-- Encrypt sensitive fields
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Example of field-level encryption for PII
ALTER TABLE user_profiles ADD COLUMN phone_encrypted BYTEA;
UPDATE user_profiles SET phone_encrypted = pgp_sym_encrypt(phone, %s) WHERE phone IS NOT NULL;
```

### Data Retention Policies
```sql
-- Automated cleanup of old data
CREATE OR REPLACE FUNCTION cleanup_old_data()
RETURNS void AS $$
BEGIN
    -- Delete job postings older than 1 year
    DELETE FROM job_postings WHERE created_at < NOW() - INTERVAL '1 year';
    
    -- Delete inactive browser sessions older than 30 days
    DELETE FROM browser_sessions WHERE is_active = false AND last_used_at < NOW() - INTERVAL '30 days';
    
    -- Archive completed automation tasks older than 6 months
    INSERT INTO automation_tasks_archive SELECT * FROM automation_tasks 
    WHERE status = 'completed' AND completed_at < NOW() - INTERVAL '6 months';
    DELETE FROM automation_tasks WHERE id IN (SELECT id FROM automation_tasks_archive);
END;
$$ LANGUAGE plpgsql;

-- Schedule cleanup job
SELECT cron.schedule('cleanup-old-data', '0 2 * * *', 'SELECT cleanup_old_data();');
```

### Privacy Compliance
```sql
-- GDPR right to be forgotten
CREATE OR REPLACE FUNCTION delete_user_data(target_user_id UUID)
RETURNS void AS $$
BEGIN
    -- Anonymize or delete user data while preserving analytics
    UPDATE applications SET user_id = NULL WHERE user_id = target_user_id;
    DELETE FROM user_experiences WHERE user_id = target_user_id;
    DELETE FROM user_skills WHERE user_id = target_user_id;
    DELETE FROM user_profiles WHERE user_id = target_user_id;
    DELETE FROM users WHERE id = target_user_id;
END;
$$ LANGUAGE plpgsql;
```

---

*Database schema is version-controlled and managed through Alembic migrations. All changes should be backward compatible and include appropriate rollback scripts.* 