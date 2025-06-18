# System Patterns & Implementation Standards

## System Architecture Patterns

### Microservices Architecture
**Event-Driven Service Communication**
```python
# Service Event Publisher Pattern
from dataclasses import dataclass
from typing import Any, Dict
import redis
import json

@dataclass
class DomainEvent:
    event_type: str
    aggregate_id: str
    data: Dict[str, Any]
    timestamp: str
    version: int = 1

class EventPublisher:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    async def publish(self, event: DomainEvent):
        channel = f"events.{event.event_type}"
        message = json.dumps(event.__dict__)
        await self.redis.publish(channel, message)

# Usage in services
# job_discovered_event = DomainEvent(
#     event_type="job.discovered",
#     aggregate_id=job_id,
#     data={"job_title": title, "company": company}
# )
# await event_publisher.publish(job_discovered_event)
```

**Service Boundary Pattern**
```python
# Domain Service Interface
from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

class JobDiscoveryService(ABC):
    @abstractmethod
    async def discover_jobs(self, user_preferences: dict) -> List[dict]:
        pass
    
    @abstractmethod
    async def get_job_details(self, job_id: UUID) -> Optional[dict]:
        pass

# Concrete Implementation
class LinkedInJobDiscoveryService(JobDiscoveryService):
    async def discover_jobs(self, user_preferences: dict) -> List[dict]:
        # LinkedIn-specific job discovery logic
        pass
```

### Frontend Architecture Patterns

**React Application Structure (Implemented)**
```typescript
// Current project structure - Page-based organization
// apps/web-frontend/src/
//   ├── components/
//   │   ├── Layout.tsx              // Main layout with navigation
//   │   └── ui/                     // Reusable UI components
//   │       ├── button.tsx          // shadcn/ui Button component
//   │       └── card.tsx            // shadcn/ui Card component
//   ├── pages/                      // Route-based pages
//   │   ├── Dashboard.tsx           // Main dashboard page
//   │   ├── Jobs.tsx                // Job discovery page
//   │   ├── Applications.tsx        // Application management
//   │   └── Profile.tsx             // User profile page
//   ├── lib/
//   │   └── utils.ts                // Utility functions (cn, etc.)
//   ├── App.tsx                     // Main app with routing
//   ├── main.tsx                    // React entry point
//   └── index.css                   // Tailwind CSS styles

// Layout Component Pattern (Implemented)
interface LayoutProps {
  children: React.ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  const location = useLocation();

  const isActive = (path: string) => {
    return location.pathname === path;
  };

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b border-border bg-background/95 backdrop-blur">
        <div className="container mx-auto px-4">
          <nav className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-8">
              <Link to="/" className="text-xl font-bold text-foreground">
                JobApp
              </Link>
              <div className="hidden md:flex items-center space-x-6">
                <Link 
                  to="/" 
                  className={`text-sm font-medium transition-colors hover:text-primary ${
                    isActive('/') ? 'text-primary' : 'text-muted-foreground'
                  }`}
                >
                  Dashboard
                </Link>
                {/* More navigation links */}
              </div>
            </div>
          </nav>
        </div>
      </header>
      <main>{children}</main>
    </div>
  );
}

// shadcn/ui Component Pattern (Implemented)
import { cn } from '../../lib/utils';
import { cva, type VariantProps } from 'class-variance-authority';

const buttonVariants = cva(
  'inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        outline: 'border border-input bg-background hover:bg-accent',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : 'button';
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);

// Page Component Pattern (Implemented)
export default function Dashboard() {
  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-foreground mb-2">
            Job Application Automation
          </h1>
          <p className="text-lg text-muted-foreground">
            AI-powered job discovery and application assistance
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Job Discovery</CardTitle>
              <CardDescription>
                Find relevant jobs across multiple platforms
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground mb-4">
                Intelligent job search with semantic matching.
              </p>
              <Button className="w-full">Search Jobs</Button>
            </CardContent>
          </Card>
          {/* More cards */}
        </div>
      </div>
    </div>
  );
}
```

**React Router Pattern (Implemented)**
```typescript
// App.tsx - Main routing setup
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/jobs" element={<Jobs />} />
          <Route path="/applications" element={<Applications />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Layout>
    </Router>
  );
}

// Navigation with active state management
const isActive = (path: string) => {
  return location.pathname === path;
};

<Link 
  to="/jobs" 
  className={`text-sm font-medium transition-colors hover:text-primary ${
    isActive('/jobs') ? 'text-primary' : 'text-muted-foreground'
  }`}
>
  Jobs
</Link>
```

**Tailwind CSS + shadcn/ui Design System (Implemented)**
```css
/* index.css - CSS Variables for theming */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96%;
    --secondary-foreground: 222.2 84% 4.9%;
    --muted: 210 40% 96%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%;
    --radius: 0.5rem;
  }
}

/* Utility function for conditional classes */
// lib/utils.ts
import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

**React Query Setup (Implemented)**
```typescript
// main.tsx - QueryClient configuration
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5, // 5 minutes
      retry: 1,
    },
  },
});

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>,
);

// Future usage pattern for API calls
export const useJobSearch = (searchParams: JobSearchParams) => {
  return useQuery({
    queryKey: ['jobs', 'search', searchParams],
    queryFn: () => jobApi.searchJobs(searchParams),
    staleTime: 5 * 60 * 1000, // 5 minutes
    enabled: !!searchParams.query
  });
};
```

**State Management Pattern (Ready for Implementation)**
```typescript
// Zustand Store Pattern for Global State
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

interface UserState {
  user: User | null;
  preferences: JobPreferences;
  isAuthenticated: boolean;
  
  // Actions
  setUser: (user: User) => void;
  updatePreferences: (prefs: Partial<JobPreferences>) => void;
  logout: () => void;
}

export const useUserStore = create<UserState>()(
  devtools(
    persist(
      (set, get) => ({
        user: null,
        preferences: {},
        isAuthenticated: false,
        
        setUser: (user) => set({ user, isAuthenticated: true }),
        updatePreferences: (prefs) => set((state) => ({
          preferences: { ...state.preferences, ...prefs }
        })),
        logout: () => set({ user: null, isAuthenticated: false })
      }),
      { name: 'user-store' }
    )
  )
);
```

## Backend Service Patterns

### FastAPI Service Structure
```python
# Service Layer Pattern
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
import asyncio

# Pydantic Models for Request/Response
class JobSearchRequest(BaseModel):
    query: str
    location: Optional[str] = None
    experience_level: Optional[str] = None
    work_arrangement: Optional[str] = None
    
class JobResponse(BaseModel):
    id: UUID
    title: str
    company: str
    location: str
    description: str
    requirements: List[str]
    similarity_score: Optional[float] = None

# Repository Pattern
class JobRepository:
    def __init__(self, db_session):
        self.db = db_session
    
    async def search_jobs(self, criteria: JobSearchRequest, user_vector: List[float]) -> List[JobResponse]:
        # Vector similarity search with filters
        query = """
        SELECT jp.*, c.name as company_name,
               (jp.embedding <=> %s::vector) as similarity_score
        FROM job_postings jp
        JOIN companies c ON jp.company_id = c.id
        WHERE jp.is_active = true
          AND (%s::text IS NULL OR jp.location_city ILIKE %s)
          AND (%s::text IS NULL OR jp.experience_level = %s)
        ORDER BY jp.embedding <=> %s::vector
        LIMIT 50
        """
        # Execute query and return results
        pass

# Service Layer
class JobDiscoveryService:
    def __init__(self, job_repo: JobRepository, nlp_service: NLPService):
        self.job_repo = job_repo
        self.nlp_service = nlp_service
    
    async def discover_relevant_jobs(
        self, 
        user_id: UUID, 
        search_criteria: JobSearchRequest
    ) -> List[JobResponse]:
        # Get user profile vector
        user_profile = await self.get_user_profile(user_id)
        user_vector = await self.nlp_service.generate_embedding(user_profile.skills_text)
        
        # Search with semantic similarity
        jobs = await self.job_repo.search_jobs(search_criteria, user_vector)
        
        # Apply business logic filtering
        filtered_jobs = await self.apply_user_preferences(jobs, user_id)
        
        return filtered_jobs

# FastAPI Route Handler
@app.post("/api/v1/jobs/search", response_model=List[JobResponse])
async def search_jobs(
    request: JobSearchRequest,
    current_user: User = Depends(get_current_user),
    job_service: JobDiscoveryService = Depends(get_job_service)
):
    try:
        jobs = await job_service.discover_relevant_jobs(current_user.id, request)
        return jobs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### Async Task Processing Pattern
```python
# Celery Task Pattern for Background Processing
from celery import Celery
from typing import Dict, Any
import asyncio

app = Celery('job_automation')

@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3})
def process_job_application(self, application_data: Dict[str, Any]):
    """Background task for processing job applications"""
    try:
        # 1. Generate tailored resume
        resume_task = generate_tailored_resume.delay(
            application_data['user_id'], 
            application_data['job_id']
        )
        
        # 2. Generate cover letter
        cover_letter_task = generate_cover_letter.delay(
            application_data['user_id'],
            application_data['job_id']
        )
        
        # 3. Wait for content generation
        resume_result = resume_task.get(timeout=60)
        cover_letter_result = cover_letter_task.get(timeout=60)
        
        # 4. Submit application
        submit_application.delay(
            application_data['application_id'],
            resume_result['file_url'],
            cover_letter_result['file_url']
        )
        
        return {"status": "success", "application_id": application_data['application_id']}
        
    except Exception as exc:
        # Log error and retry
        logger.error(f"Application processing failed: {str(exc)}")
        raise self.retry(countdown=60)
```

## Data Access Patterns

### Database Repository Pattern
```python
# SQLAlchemy Repository Pattern
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_
from sqlalchemy.orm import selectinload
from typing import List, Optional
from uuid import UUID

class BaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_by_id(self, model_class, id: UUID):
        result = await self.session.execute(
            select(model_class).where(model_class.id == id)
        )
        return result.scalar_one_or_none()
    
    async def create(self, entity):
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

class ApplicationRepository(BaseRepository):
    async def get_user_applications(
        self, 
        user_id: UUID, 
        status: Optional[str] = None
    ) -> List[Application]:
        query = select(Application).where(Application.user_id == user_id)
        
        if status:
            query = query.where(Application.status == status)
            
        query = query.options(
            selectinload(Application.job_posting),
            selectinload(Application.generated_content)
        ).order_by(Application.created_at.desc())
        
        result = await self.session.execute(query)
        return result.scalars().all()
```

### Caching Pattern
```python
# Redis Caching Decorator
import redis.asyncio as redis
import json
from functools import wraps
from typing import Any, Callable

class CacheService:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    def cache(self, key_prefix: str, ttl: int = 3600):
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs):
                # Generate cache key
                cache_key = f"{key_prefix}:{hash(str(args) + str(kwargs))}"
                
                # Try to get from cache
                cached_result = await self.redis.get(cache_key)
                if cached_result:
                    return json.loads(cached_result)
                
                # Execute function and cache result
                result = await func(*args, **kwargs)
                await self.redis.setex(
                    cache_key, 
                    ttl, 
                    json.dumps(result, default=str)
                )
                return result
            return wrapper
        return decorator

# Usage
cache_service = CacheService(redis_client)

@cache_service.cache("job_recommendations", ttl=1800)
async def get_job_recommendations(user_id: UUID) -> List[Dict]:
    # Expensive operation to get job recommendations
    pass
```

## AI/ML Integration Patterns

### OpenAI Integration Pattern
```python
# AI Service Pattern for Content Generation
from openai import AsyncOpenAI
from typing import Dict, Any
import asyncio

class CoverLetterGenerator:
    def __init__(self, openai_client: AsyncOpenAI):
        self.client = openai_client
    
    async def generate_cover_letter(
        self, 
        user_profile: Dict[str, Any],
        job_posting: Dict[str, Any],
        company_info: Dict[str, Any]
    ) -> str:
        prompt = self._build_prompt(user_profile, job_posting, company_info)
        
        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self._get_system_prompt()},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        return response.choices[0].message.content
    
    def _build_prompt(self, user_profile, job_posting, company_info) -> str:
        return f"""
        Generate a personalized cover letter for:
        
        Job: {job_posting['title']} at {company_info['name']}
        Company: {company_info['description']}
        Requirements: {job_posting['requirements']}
        
        Candidate Profile:
        Experience: {user_profile['experience']}
        Skills: {user_profile['skills']}
        Achievements: {user_profile['achievements']}
        """
    
    def _get_system_prompt(self) -> str:
        return """You are an expert career counselor. Generate professional, 
        personalized cover letters that highlight relevant experience and 
        demonstrate genuine interest in the company."""

# Vector Embedding Pattern
class SemanticMatchingService:
    def __init__(self, embedding_model):
        self.model = embedding_model
    
    async def calculate_job_similarity(
        self, 
        user_skills: List[str], 
        job_requirements: List[str]
    ) -> float:
        # Generate embeddings
        user_embedding = await self._get_embedding(" ".join(user_skills))
        job_embedding = await self._get_embedding(" ".join(job_requirements))
        
        # Calculate cosine similarity
        similarity = self._cosine_similarity(user_embedding, job_embedding)
        return similarity
    
    async def _get_embedding(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()
```

## Browser Automation Patterns

### Playwright Automation Pattern
```python
# Anti-Detection Browser Automation
from playwright.async_api import async_playwright, Page
import random
import asyncio

class BrowserAutomationService:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        ]
    
    async def create_stealth_browser(self):
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ]
        )
        
        context = await browser.new_context(
            user_agent=random.choice(self.user_agents),
            viewport={'width': 1920, 'height': 1080},
            java_script_enabled=True
        )
        
        # Inject anti-detection scripts
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });
        """)
        
        return await context.new_page()
    
    async def human_like_typing(self, page: Page, selector: str, text: str):
        await page.click(selector)
        await page.fill(selector, "")  # Clear field
        
        for char in text:
            await page.type(selector, char, delay=random.randint(50, 150))
            
    async def human_like_scroll(self, page: Page):
        # Random scroll pattern
        for _ in range(random.randint(2, 5)):
            await page.mouse.wheel(0, random.randint(200, 400))
            await asyncio.sleep(random.uniform(0.5, 1.5))

class LinkedInApplicationBot:
    def __init__(self, browser_service: BrowserAutomationService):
        self.browser_service = browser_service
    
    async def apply_to_job(self, job_url: str, application_data: Dict):
        page = await self.browser_service.create_stealth_browser()
        
        try:
            # Navigate to job posting
            await page.goto(job_url, wait_until='networkidle')
            
            # Click apply button
            apply_button = page.locator('button:has-text("Apply")')
            await apply_button.click()
            
            # Fill application form
            await self._fill_application_form(page, application_data)
            
            # Submit application
            await self._submit_application(page)
            
            return {"status": "success", "job_url": job_url}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
        finally:
            await page.close()
```

## Error Handling & Monitoring

### Error Handling Pattern
```python
# Custom Exception Classes
class JobApplicationError(Exception):
    """Base exception for job application errors"""
    pass

class JobDiscoveryError(JobApplicationError):
    """Raised when job discovery fails"""
    pass

class ContentGenerationError(JobApplicationError):
    """Raised when AI content generation fails"""
    pass

class AutomationError(JobApplicationError):
    """Raised when browser automation fails"""
    pass

# Error Handler Middleware
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

async def error_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except JobApplicationError as e:
        logging.error(f"Application error: {str(e)}", exc_info=True)
        return JSONResponse(
            status_code=400,
            content={
                "error": {
                    "type": e.__class__.__name__,
                    "message": str(e),
                    "request_id": request.state.request_id
                }
            }
        )
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "type": "InternalServerError",
                    "message": "An unexpected error occurred",
                    "request_id": request.state.request_id
                }
            }
        )
```

## Security & Authentication

### JWT Authentication Pattern
```python
# JWT Token Management
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException

security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthenticationService:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm
    
    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            user_id = payload.get("sub")
            if user_id is None:
                raise HTTPException(status_code=401, detail="Invalid token")
            return user_id
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

# Authentication Dependency
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    auth_service: AuthenticationService = Depends()
):
    user_id = auth_service.verify_token(credentials.credentials)
    # Fetch user from database
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
```

## Configuration Management

### Environment Configuration Pattern
```python
# Pydantic Settings Pattern
from pydantic import BaseSettings, PostgresDsn, validator
from typing import Optional

class Settings(BaseSettings):
    # Database
    database_url: PostgresDsn
    redis_url: str
    
    # API Keys
    openai_api_key: str
    linkedin_api_key: Optional[str] = None
    indeed_api_key: Optional[str] = None
    
    # Security
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    
    # Application
    debug: bool = False
    log_level: str = "INFO"
    cors_origins: list = ["http://localhost:3000"]
    
    # External Services
    aws_region: str = "us-east-1"
    aws_s3_bucket: str
    
    @validator('cors_origins', pre=True)
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

## Testing Patterns

### FastAPI Testing Pattern
```python
# Test Configuration
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest.mock import AsyncMock

# Test database setup
SQLALCHEMY_DATABASE_URL = "postgresql://test:test@localhost/test_jobapp"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

# Test Example
def test_job_search(client, mock_auth_user):
    response = client.post(
        "/api/v1/jobs/search",
        json={
            "query": "Python Developer",
            "location": "San Francisco",
            "experience_level": "mid"
        },
        headers={"Authorization": f"Bearer {mock_auth_user.token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["title"]
    assert data[0]["company"]
```

## File Naming & Organization Standards

### Directory Structure
```
jobapp/
├── apps/
│   ├── web-frontend/           # React TypeScript app
│   │   ├── src/
│   │   │   ├── components/     # Reusable UI components
│   │   │   ├── features/       # Feature-specific code
│   │   │   ├── hooks/          # Custom React hooks
│   │   │   ├── services/       # API clients
│   │   │   ├── stores/         # Zustand stores
│   │   │   ├── types/          # TypeScript definitions
│   │   │   └── utils/          # Utility functions
│   └── api-gateway/            # FastAPI gateway
├── services/
│   ├── job-discovery/          # Job scraping service
│   ├── resume-processor/       # Resume processing service
│   ├── cover-letter-gen/       # Cover letter generation
│   └── automation-engine/      # Browser automation
└── packages/
    ├── shared-types/           # Shared TypeScript types
    ├── python-shared/          # Shared Python utilities
    └── ui-components/          # React component library
```

### Naming Conventions
- **React Components**: PascalCase (e.g., `JobSearchForm.tsx`)
- **React Hooks**: camelCase with `use` prefix (e.g., `useJobSearch.ts`)
- **Python Modules**: snake_case (e.g., `job_discovery_service.py`)
- **Python Classes**: PascalCase (e.g., `JobDiscoveryService`)
- **API Endpoints**: kebab-case (e.g., `/api/v1/job-search`)
- **Database Tables**: snake_case (e.g., `job_postings`)
- **Environment Variables**: UPPER_SNAKE_CASE (e.g., `OPENAI_API_KEY`)

---
*These patterns should be consistently applied across all services and components. Regular code reviews should ensure adherence to these standards.* 