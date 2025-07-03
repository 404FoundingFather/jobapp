-- Initial Database Schema Migration
-- Job Application Assistance System
-- Version: 1.0.0
-- Created: 2024-01-XX

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgvector";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Create custom types
CREATE TYPE subscription_tier AS ENUM ('free', 'basic', 'premium', 'enterprise');
CREATE TYPE skill_category AS ENUM ('technical', 'soft', 'language', 'certification');
CREATE TYPE proficiency_level AS ENUM ('beginner', 'intermediate', 'advanced', 'expert');
CREATE TYPE company_size AS ENUM ('startup', 'small', 'medium', 'large', 'enterprise');
CREATE TYPE experience_level AS ENUM ('entry', 'mid', 'senior', 'lead', 'executive');
CREATE TYPE employment_type AS ENUM ('full-time', 'part-time', 'contract', 'internship');
CREATE TYPE work_arrangement AS ENUM ('remote', 'hybrid', 'onsite');
CREATE TYPE application_status AS ENUM ('pending', 'submitted', 'reviewing', 'interviewed', 'rejected', 'offered', 'withdrawn');
CREATE TYPE application_method AS ENUM ('automated', 'manual', 'referral');
CREATE TYPE task_status AS ENUM ('pending', 'running', 'completed', 'failed', 'cancelled');
CREATE TYPE content_type AS ENUM ('resume', 'cover_letter', 'follow_up_email');

-- ============================================================================
-- USER MANAGEMENT DOMAIN
-- ============================================================================

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    subscription_tier subscription_tier DEFAULT 'free',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login_at TIMESTAMP WITH TIME ZONE
);

-- User profiles table
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
    preferred_work_type work_arrangement,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    CONSTRAINT unique_user_profile UNIQUE (user_id)
);

-- User skills table
CREATE TABLE user_skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    skill_name VARCHAR(100) NOT NULL,
    skill_category skill_category,
    proficiency_level proficiency_level,
    years_experience DECIMAL(3,1),
    is_primary BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User experiences table
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

-- ============================================================================
-- JOB DISCOVERY DOMAIN
-- ============================================================================

-- Companies table
CREATE TABLE companies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255),
    industry VARCHAR(100),
    size_category company_size,
    headquarters_city VARCHAR(100),
    headquarters_country VARCHAR(50),
    description TEXT,
    logo_url VARCHAR(500),
    career_page_url VARCHAR(500),
    glassdoor_rating DECIMAL(3,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Job postings table
CREATE TABLE job_postings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id VARCHAR(255),
    company_id UUID REFERENCES companies(id),
    title VARCHAR(300) NOT NULL,
    description TEXT NOT NULL,
    requirements TEXT,
    benefits TEXT,
    salary_min INTEGER,
    salary_max INTEGER,
    salary_currency VARCHAR(3) DEFAULT 'USD',
    experience_level experience_level,
    employment_type employment_type,
    work_arrangement work_arrangement,
    location_city VARCHAR(100),
    location_state VARCHAR(50),
    location_country VARCHAR(50),
    source_platform VARCHAR(50) NOT NULL,
    source_url VARCHAR(1000) NOT NULL,
    posted_date DATE,
    expires_date DATE,
    is_active BOOLEAN DEFAULT true,
    required_skills TEXT[],
    preferred_skills TEXT[],
    embedding VECTOR(384),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Job search preferences table
CREATE TABLE job_search_preferences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    search_name VARCHAR(100) NOT NULL,
    target_titles TEXT[],
    excluded_titles TEXT[],
    target_companies TEXT[],
    excluded_companies TEXT[],
    min_salary INTEGER,
    max_salary INTEGER,
    experience_levels TEXT[],
    work_arrangements TEXT[],
    employment_types TEXT[],
    locations TEXT[],
    keywords TEXT[],
    excluded_keywords TEXT[],
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================================================
-- APPLICATION MANAGEMENT DOMAIN
-- ============================================================================

-- Applications table
CREATE TABLE applications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    job_posting_id UUID REFERENCES job_postings(id),
    company_name VARCHAR(255) NOT NULL,
    job_title VARCHAR(300) NOT NULL,
    job_url VARCHAR(1000),
    status application_status DEFAULT 'pending',
    application_method application_method,
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

-- Application status history table
CREATE TABLE application_status_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    application_id UUID NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
    status application_status NOT NULL,
    notes TEXT,
    changed_by VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Generated content table
CREATE TABLE generated_content (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    application_id UUID NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
    content_type content_type NOT NULL,
    content_text TEXT,
    file_url VARCHAR(500),
    generation_prompt TEXT,
    model_used VARCHAR(50),
    generation_metadata JSONB,
    user_approved BOOLEAN DEFAULT false,
    user_edited BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================================================
-- AUTOMATION & TASKS DOMAIN
-- ============================================================================

-- Automation tasks table
CREATE TABLE automation_tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    application_id UUID REFERENCES applications(id),
    task_type VARCHAR(50) NOT NULL,
    status task_status DEFAULT 'pending',
    priority INTEGER DEFAULT 5,
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

-- Browser sessions table
CREATE TABLE browser_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    platform VARCHAR(50) NOT NULL,
    session_data JSONB,
    cookies TEXT,
    user_agent VARCHAR(500),
    proxy_config JSONB,
    is_active BOOLEAN DEFAULT true,
    last_used_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================================================
-- ANALYTICS & METRICS DOMAIN
-- ============================================================================

-- User analytics table
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
    response_rate DECIMAL(5,4),
    time_saved_minutes INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Platform metrics table
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

-- ============================================================================
-- INDEXES
-- ============================================================================

-- User indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_active ON users(is_active);
CREATE INDEX idx_user_profiles_user_id ON user_profiles(user_id);
CREATE INDEX idx_user_skills_user_id ON user_skills(user_id);
CREATE INDEX idx_user_skills_category ON user_skills(skill_category);
CREATE INDEX idx_user_skills_name ON user_skills(skill_name);
CREATE INDEX idx_user_experiences_user_id ON user_experiences(user_id);
CREATE INDEX idx_user_experiences_current ON user_experiences(is_current);

-- Company and job indexes
CREATE INDEX idx_companies_name ON companies(name);
CREATE INDEX idx_companies_domain ON companies(domain);
CREATE INDEX idx_companies_industry ON companies(industry);
CREATE INDEX idx_job_postings_company_id ON job_postings(company_id);
CREATE INDEX idx_job_postings_active ON job_postings(is_active);
CREATE INDEX idx_job_postings_source ON job_postings(source_platform);
CREATE INDEX idx_job_postings_location ON job_postings(location_city, location_state);
CREATE INDEX idx_job_postings_experience ON job_postings(experience_level);
CREATE INDEX idx_job_postings_work_type ON job_postings(work_arrangement);
CREATE INDEX idx_job_postings_posted_date ON job_postings(posted_date);

-- Vector similarity index for semantic search
CREATE INDEX idx_job_postings_embedding ON job_postings USING ivfflat (embedding vector_cosine_ops);

-- Job search preferences indexes
CREATE INDEX idx_job_search_prefs_user_id ON job_search_preferences(user_id);
CREATE INDEX idx_job_search_prefs_active ON job_search_preferences(is_active);

-- Application indexes
CREATE INDEX idx_applications_user_id ON applications(user_id);
CREATE INDEX idx_applications_status ON applications(status);
CREATE INDEX idx_applications_submitted_at ON applications(submitted_at);
CREATE INDEX idx_applications_job_posting_id ON applications(job_posting_id);
CREATE INDEX idx_app_status_history_app_id ON application_status_history(application_id);
CREATE INDEX idx_app_status_history_created_at ON application_status_history(created_at);
CREATE INDEX idx_generated_content_app_id ON generated_content(application_id);
CREATE INDEX idx_generated_content_type ON generated_content(content_type);

-- Automation indexes
CREATE INDEX idx_automation_tasks_user_id ON automation_tasks(user_id);
CREATE INDEX idx_automation_tasks_status ON automation_tasks(status);
CREATE INDEX idx_automation_tasks_type ON automation_tasks(task_type);
CREATE INDEX idx_automation_tasks_scheduled_at ON automation_tasks(scheduled_at);
CREATE INDEX idx_browser_sessions_user_id ON browser_sessions(user_id);
CREATE INDEX idx_browser_sessions_platform ON browser_sessions(platform);
CREATE INDEX idx_browser_sessions_active ON browser_sessions(is_active);

-- Analytics indexes
CREATE INDEX idx_user_analytics_user_id ON user_analytics(user_id);
CREATE INDEX idx_user_analytics_date ON user_analytics(metric_date);
CREATE INDEX idx_platform_metrics_platform ON platform_metrics(platform_name);
CREATE INDEX idx_platform_metrics_date ON platform_metrics(metric_date);

-- ============================================================================
-- CONSTRAINTS
-- ============================================================================

-- Email validation
ALTER TABLE users ADD CONSTRAINT valid_email 
    CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

-- Salary ranges
ALTER TABLE job_postings ADD CONSTRAINT valid_salary_range 
    CHECK (salary_min IS NULL OR salary_max IS NULL OR salary_min <= salary_max);

-- Experience validation
ALTER TABLE user_profiles ADD CONSTRAINT valid_experience 
    CHECK (years_experience >= 0 AND years_experience <= 70);

-- Priority validation
ALTER TABLE automation_tasks ADD CONSTRAINT valid_priority 
    CHECK (priority >= 1 AND priority <= 10);

-- Response rate validation
ALTER TABLE user_analytics ADD CONSTRAINT valid_response_rate 
    CHECK (response_rate >= 0 AND response_rate <= 1);

-- ============================================================================
-- TRIGGERS FOR UPDATED_AT
-- ============================================================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for updated_at
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_user_profiles_updated_at BEFORE UPDATE ON user_profiles FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_user_experiences_updated_at BEFORE UPDATE ON user_experiences FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_companies_updated_at BEFORE UPDATE ON companies FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_job_postings_updated_at BEFORE UPDATE ON job_postings FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_job_search_preferences_updated_at BEFORE UPDATE ON job_search_preferences FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_applications_updated_at BEFORE UPDATE ON applications FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_automation_tasks_updated_at BEFORE UPDATE ON automation_tasks FOR EACH ROW EXECUTE FUNCTION update_updated_at_column(); 