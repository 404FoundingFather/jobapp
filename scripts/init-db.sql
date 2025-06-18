-- =============================================================================
-- Job Application Automation System - Database Initialization
-- =============================================================================
-- This script runs when PostgreSQL container starts up
-- It creates the necessary databases and basic configuration

-- Create main development database
SELECT 'CREATE DATABASE jobapp_dev'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'jobapp_dev')\gexec

-- Create test database
SELECT 'CREATE DATABASE jobapp_test'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'jobapp_test')\gexec

-- Connect to development database
\c jobapp_dev

-- Create application user (optional, for production)
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = 'jobapp_user') THEN
        CREATE USER jobapp_user WITH PASSWORD 'jobapp_password';
    END IF;
END
$$;

-- Grant privileges to application user
GRANT ALL PRIVILEGES ON DATABASE jobapp_dev TO jobapp_user;
GRANT ALL PRIVILEGES ON DATABASE jobapp_test TO jobapp_user;

-- Set up database configuration
ALTER DATABASE jobapp_dev SET timezone TO 'UTC';
ALTER DATABASE jobapp_test SET timezone TO 'UTC';

-- Log initialization completion
SELECT 'Database initialization completed successfully' AS status; 