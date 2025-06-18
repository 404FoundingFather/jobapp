-- =============================================================================
-- PostgreSQL Extensions Setup for Job Application System
-- =============================================================================
-- This script installs all necessary PostgreSQL extensions

-- Connect to the development database
\c jobapp_dev

-- Install pgvector extension for semantic similarity search
CREATE EXTENSION IF NOT EXISTS vector;

-- Install uuid-ossp for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Install pg_trgm for fuzzy text matching
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Install unaccent for removing accents from text
CREATE EXTENSION IF NOT EXISTS unaccent;

-- Install btree_gin for better indexing options
CREATE EXTENSION IF NOT EXISTS btree_gin;

-- Verify extensions are installed
SELECT 
    extname AS "Extension Name",
    extversion AS "Version"
FROM pg_extension 
WHERE extname IN ('vector', 'uuid-ossp', 'pg_trgm', 'unaccent', 'btree_gin')
ORDER BY extname;

-- Configure pgvector settings for optimal performance
-- Set default vector index parameters
ALTER DATABASE jobapp_dev SET ivfflat.probes = 10;

-- Log successful extension installation
SELECT 
    'Extensions installed successfully: ' || 
    string_agg(extname, ', ' ORDER BY extname) AS status
FROM pg_extension 
WHERE extname IN ('vector', 'uuid-ossp', 'pg_trgm', 'unaccent', 'btree_gin');

-- Switch to test database and install same extensions
\c jobapp_test

-- Install same extensions for test database
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;
CREATE EXTENSION IF NOT EXISTS btree_gin;

-- Configure test database settings
ALTER DATABASE jobapp_test SET ivfflat.probes = 10;

SELECT 'Test database extensions installed successfully' AS status; 