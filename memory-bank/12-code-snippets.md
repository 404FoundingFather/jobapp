# Code Snippets & Patterns

## Purpose & Instructions for AI

This file serves as a repository of reusable code patterns, templates, and examples that should be used consistently across the project. As an AI assistant, you should maintain this file by adding project-specific patterns as they emerge during development.

## How to Manage This File

### When to Add Snippets
- **Recurring Patterns:** When you notice the same code structure being implemented multiple times
- **Project Standards:** When establishing consistent patterns for the project
- **Complex Implementations:** When creating reusable solutions for common challenges
- **Team Requests:** When developers ask for standardized approaches

### What to Include

#### Frontend Patterns
Add snippets for:
- Component templates following project conventions
- Custom hooks with consistent structure
- Form handling patterns
- State management approaches
- API integration patterns
- Error handling implementations

#### Backend Patterns
Add snippets for:
- API route handlers with validation
- Service class templates
- Database repository patterns
- Middleware implementations
- Error handling utilities
- Authentication/authorization patterns

#### Testing Patterns
Add snippets for:
- Component test templates
- API endpoint test structures
- Mock implementations
- Test data factories
- Integration test patterns

#### Utility Patterns
Add snippets for:
- Common helper functions
- Configuration patterns
- Validation schemas
- Type definitions
- Constants and enums

### Organization Structure

Use this structure to organize code snippets:

```markdown
## [Category Name] (e.g., Frontend Components, Backend Services)

### [Pattern Name]
[Brief description of when to use this pattern]

```[language]
[Code snippet with clear placeholder markers]
```

#### Usage Example
[Show how to use the pattern]

#### Implementation Notes
- [Important considerations]
- [Common pitfalls to avoid]
- [Variations or alternatives]
```

### Quality Guidelines

#### Snippet Requirements
- **Complete and Functional:** Snippets should be ready-to-use with minimal modification
- **Well-Commented:** Include comments explaining key parts
- **Placeholder Markers:** Use clear placeholders like `[ComponentName]`, `[fieldName]`, etc.
- **Consistent Style:** Follow the project's coding standards
- **Error Handling:** Include appropriate error handling patterns

#### Documentation Standards
- **Clear Descriptions:** Explain when and why to use each pattern
- **Usage Examples:** Show practical implementation
- **Prerequisites:** Note any dependencies or setup required
- **Variations:** Document different approaches for different scenarios

### Maintenance Instructions

#### Regular Updates
- **After Major Features:** Add patterns that emerged during development
- **Code Review Findings:** Incorporate improvements from code reviews
- **Refactoring Sessions:** Update patterns when architecture changes
- **Team Feedback:** Add patterns requested by team members

#### Quality Checks
- **Validate Examples:** Ensure all code snippets compile and work
- **Remove Outdated:** Delete patterns that are no longer recommended
- **Consolidate Similar:** Merge similar patterns into comprehensive examples
- **Update Dependencies:** Ensure compatibility with current project versions

## Content Organization Template

Use this template structure for organizing content:

### Frontend Patterns
```markdown
## Frontend Components

### [Pattern Name]
[Description]

### Custom Hooks
[Pattern templates]

### Form Handling
[Validation and submission patterns]

### State Management
[Global and local state patterns]
```

### Backend Patterns
```markdown
## Backend Services

### API Routes
[Route handler patterns]

### Business Logic
[Service layer patterns]

### Data Access
[Repository and database patterns]

### Middleware
[Authentication, validation, error handling]
```

### Testing Patterns
```markdown
## Testing Utilities

### Component Tests
[React component testing patterns]

### API Tests
[Backend endpoint testing]

### Integration Tests
[Full-stack testing patterns]

### Test Data
[Mock data and factory patterns]
```

### Utility Patterns
```markdown
## Utility Functions

### Validation
[Input validation patterns]

### Error Handling
[Consistent error handling]

### Configuration
[Environment and config patterns]

### Type Definitions
[Common TypeScript patterns]
```

## Best Practices for AI Maintenance

### Pattern Recognition
- **Identify Repetition:** Look for code that's written similarly across different files
- **Extract Common Logic:** Create reusable patterns from frequently used code
- **Standardize Approaches:** Establish consistent ways to handle common tasks

### Documentation Quality
- **Be Specific:** Provide concrete examples rather than abstract descriptions
- **Include Context:** Explain why a pattern is recommended
- **Show Alternatives:** Document different approaches for different scenarios
- **Update Examples:** Keep examples current with latest project practices

### Collaboration Guidelines
- **Reference in Code Reviews:** Point to established patterns during reviews
- **Suggest Improvements:** Recommend pattern usage when appropriate
- **Update Based on Feedback:** Incorporate suggestions from team members
- **Maintain Consistency:** Ensure new patterns align with existing conventions

## Integration with Development Workflow

### During Development
- **Reference Existing Patterns:** Check this file before implementing new features
- **Follow Established Conventions:** Use patterns that align with project standards
- **Suggest Pattern Usage:** Recommend appropriate patterns to developers

### During Code Review
- **Validate Pattern Usage:** Ensure code follows established patterns
- **Identify New Patterns:** Recognize opportunities to create new reusable patterns
- **Update Documentation:** Add new patterns discovered during review

### During Refactoring
- **Update Patterns:** Modify patterns when architecture changes
- **Consolidate Similar Code:** Extract common patterns from similar implementations
- **Remove Deprecated:** Clean up patterns that are no longer recommended

---

## Getting Started

### Initial Setup
1. **Review Project Code:** Identify existing patterns in the codebase
2. **Extract Common Patterns:** Create initial snippets from frequently used code
3. **Establish Categories:** Organize patterns into logical sections
4. **Document Usage:** Add clear examples and implementation notes

### Ongoing Maintenance
1. **Regular Reviews:** Periodically assess pattern usage and effectiveness
2. **Team Input:** Incorporate feedback and requests from developers
3. **Quality Updates:** Improve patterns based on evolving best practices
4. **Consistency Checks:** Ensure patterns align with current project standards

*This file should evolve with the project, capturing the team's accumulated knowledge and established conventions in reusable, well-documented patterns.* 

## Frontend Components

### Layout Component (Implemented)
Main layout component with navigation and routing support

```typescript
import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Button } from '../components/ui/button';

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
      <header className="border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
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
                <Link 
                  to="/jobs" 
                  className={`text-sm font-medium transition-colors hover:text-primary ${
                    isActive('/jobs') ? 'text-primary' : 'text-muted-foreground'
                  }`}
                >
                  Jobs
                </Link>
                <Link 
                  to="/applications" 
                  className={`text-sm font-medium transition-colors hover:text-primary ${
                    isActive('/applications') ? 'text-primary' : 'text-muted-foreground'
                  }`}
                >
                  Applications
                </Link>
                <Link 
                  to="/profile" 
                  className={`text-sm font-medium transition-colors hover:text-primary ${
                    isActive('/profile') ? 'text-primary' : 'text-muted-foreground'
                  }`}
                >
                  Profile
                </Link>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Button variant="outline" size="sm">
                Help
              </Button>
              <Button size="sm">
                Account
              </Button>
            </div>
          </nav>
        </div>
      </header>
      <main>
        {children}
      </main>
    </div>
  );
}
```

### shadcn/ui Button Component (Implemented)
Reusable button component with variants and sizes

```typescript
import * as React from 'react';
import { Slot } from '@radix-ui/react-slot';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '../../lib/utils';

const buttonVariants = cva(
  'inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive:
          'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline:
          'border border-input bg-background hover:bg-accent hover:text-accent-foreground',
        secondary:
          'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'text-primary underline-offset-4 hover:underline',
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
Button.displayName = 'Button';

export { Button, buttonVariants };
```

### Card Component (Implemented)
Flexible card component for content containers

```typescript
import * as React from 'react';
import { cn } from '../../lib/utils';

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      'rounded-lg border bg-card text-card-foreground shadow-sm',
      className
    )}
    {...props}
  />
));
Card.displayName = 'Card';

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn('flex flex-col space-y-1.5 p-6', className)}
    {...props}
  />
));
CardHeader.displayName = 'CardHeader';

const CardTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h3
    ref={ref}
    className={cn(
      'text-2xl font-semibold leading-none tracking-tight',
      className
    )}
    {...props}
  />
));
CardTitle.displayName = 'CardTitle';

const CardDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <p
    ref={ref}
    className={cn('text-sm text-muted-foreground', className)}
    {...props}
  />
));
CardDescription.displayName = 'CardDescription';

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn('p-6 pt-0', className)} {...props} />
));
CardContent.displayName = 'CardContent';

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn('flex items-center p-6 pt-0', className)}
    {...props}
  />
));
CardFooter.displayName = 'CardFooter';

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent };
```

### Dashboard Page Component (Implemented)
Main dashboard page with feature overview cards

```typescript
import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { Button } from '../components/ui/button';

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
                Intelligent job search with semantic matching and multi-platform aggregation.
              </p>
              <Button className="w-full">Search Jobs</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Resume Processing</CardTitle>
              <CardDescription>
                Tailor your resume for each application
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground mb-4">
                Dynamic resume optimization based on job requirements.
              </p>
              <Button variant="outline" className="w-full">Upload Resume</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Cover Letters</CardTitle>
              <CardDescription>
                AI-generated personalized cover letters
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground mb-4">
                Personalized content with company research integration.
              </p>
              <Button variant="secondary" className="w-full">Generate Letter</Button>
            </CardContent>
          </Card>
        </div>

        <div className="mt-12">
          <Card>
            <CardHeader>
              <CardTitle>Quick Start</CardTitle>
              <CardDescription>
                Get started with your job application automation
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="flex items-center space-x-4">
                  <div className="w-8 h-8 bg-primary text-primary-foreground rounded-full flex items-center justify-center text-sm font-semibold">
                    1
                  </div>
                  <div>
                    <h3 className="font-semibold">Set up your profile</h3>
                    <p className="text-sm text-muted-foreground">
                      Upload your resume and set job preferences
                    </p>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <div className="w-8 h-8 bg-primary text-primary-foreground rounded-full flex items-center justify-center text-sm font-semibold">
                    2
                  </div>
                  <div>
                    <h3 className="font-semibold">Discover relevant jobs</h3>
                    <p className="text-sm text-muted-foreground">
                      AI-powered job matching across multiple platforms
                    </p>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <div className="w-8 h-8 bg-primary text-primary-foreground rounded-full flex items-center justify-center text-sm font-semibold">
                    3
                  </div>
                  <div>
                    <h3 className="font-semibold">Generate application materials</h3>
                    <p className="text-sm text-muted-foreground">
                      Tailored resumes and personalized cover letters
                    </p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
```

### Job Card Component
Component for displaying job postings in search results and saved jobs

```typescript
interface JobCardProps {
  job: Job;
  onApply: (jobId: string) => void;
  onSave: (jobId: string) => void;
  isApplying?: boolean;
  similarity?: number;
}

export const JobCard: React.FC<JobCardProps> = ({ 
  job, 
  onApply, 
  onSave, 
  isApplying = false,
  similarity 
}) => {
  return (
    <Card className="job-card hover:shadow-lg transition-shadow">
      <CardHeader>
        <div className="flex justify-between items-start">
          <div>
            <h3 className="text-lg font-semibold">{job.title}</h3>
            <p className="text-gray-600">{job.company.name}</p>
          </div>
          {similarity && (
            <Badge variant="secondary">{Math.round(similarity * 100)}% match</Badge>
          )}
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-2">
          <div className="flex gap-2 flex-wrap">
            <Badge variant="outline">{job.experienceLevel}</Badge>
            <Badge variant="outline">{job.workArrangement}</Badge>
          </div>
          <p className="text-sm text-gray-600">{job.location}</p>
          {job.salaryRange && (
            <p className="text-sm font-medium">{job.salaryRange}</p>
          )}
        </div>
      </CardContent>
      <CardFooter className="flex gap-2">
        <Button 
          onClick={() => onApply(job.id)} 
          disabled={isApplying}
          className="flex-1"
        >
          {isApplying ? <Spinner className="mr-2" /> : null}
          Apply Now
        </Button>
        <Button variant="outline" onClick={() => onSave(job.id)}>
          <Heart className="w-4 h-4" />
        </Button>
      </CardFooter>
    </Card>
  );
};
```

### Application Status Component
Component for tracking application progress

```typescript
interface ApplicationStatusProps {
  application: Application;
  onUpdateStatus: (applicationId: string, status: ApplicationStatus) => void;
}

export const ApplicationStatus: React.FC<ApplicationStatusProps> = ({
  application,
  onUpdateStatus
}) => {
  const getStatusColor = (status: ApplicationStatus): string => {
    const colors = {
      pending: 'bg-yellow-100 text-yellow-800',
      submitted: 'bg-blue-100 text-blue-800',
      reviewing: 'bg-purple-100 text-purple-800',
      interviewed: 'bg-green-100 text-green-800',
      rejected: 'bg-red-100 text-red-800',
      offered: 'bg-emerald-100 text-emerald-800',
    };
    return colors[status] || 'bg-gray-100 text-gray-800';
  };

  return (
    <div className="application-status p-4 border rounded-lg">
      <div className="flex justify-between items-center mb-3">
        <h4 className="font-medium">{application.jobTitle}</h4>
        <Badge className={getStatusColor(application.status)}>
          {application.status}
        </Badge>
      </div>
      
      <div className="text-sm text-gray-600 space-y-1">
        <p>{application.companyName}</p>
        <p>Applied: {formatDate(application.submittedAt)}</p>
        {application.lastStatusUpdate && (
          <p>Updated: {formatDate(application.lastStatusUpdate)}</p>
        )}
      </div>

      <Select 
        value={application.status} 
        onValueChange={(status) => onUpdateStatus(application.id, status as ApplicationStatus)}
      >
        <SelectTrigger className="mt-3">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="pending">Pending</SelectItem>
          <SelectItem value="submitted">Submitted</SelectItem>
          <SelectItem value="reviewing">Under Review</SelectItem>
          <SelectItem value="interviewed">Interviewed</SelectItem>
          <SelectItem value="rejected">Rejected</SelectItem>
          <SelectItem value="offered">Offered</SelectItem>
        </SelectContent>
      </Select>
    </div>
  );
};
```

### Custom Hooks

#### useJobSearch Hook
Hook for managing job search state and API calls

```typescript
export const useJobSearch = (initialParams?: JobSearchParams) => {
  const [searchParams, setSearchParams] = useState<JobSearchParams>(
    initialParams || {
      query: '',
      location: '',
      experienceLevel: '',
      workArrangement: '',
    }
  );

  const { 
    data: jobs, 
    isLoading, 
    error,
    refetch 
  } = useQuery({
    queryKey: ['jobs', 'search', searchParams],
    queryFn: () => jobApi.searchJobs(searchParams),
    enabled: Boolean(searchParams.query),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  const updateSearch = useCallback((params: Partial<JobSearchParams>) => {
    setSearchParams(prev => ({ ...prev, ...params }));
  }, []);

  const clearSearch = useCallback(() => {
    setSearchParams({
      query: '',
      location: '',
      experienceLevel: '',
      workArrangement: '',
    });
  }, []);

  return {
    jobs: jobs?.data || [],
    searchParams,
    updateSearch,
    clearSearch,
    isLoading,
    error,
    refetch,
  };
};
```

#### useApplication Hook
Hook for managing application submission and tracking

```typescript
export const useApplication = () => {
  const queryClient = useQueryClient();

  const applyToJob = useMutation({
    mutationFn: async (params: {
      jobId: string;
      resumeId?: string;
      coverLetterContent?: string;
      customData?: Record<string, any>;
    }) => {
      return jobApi.applyToJob(params);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['applications'] });
      toast.success('Application submitted successfully!');
    },
    onError: (error) => {
      toast.error('Failed to submit application');
      console.error('Application submission error:', error);
    },
  });

  const updateApplicationStatus = useMutation({
    mutationFn: async (params: {
      applicationId: string;
      status: ApplicationStatus;
      notes?: string;
    }) => {
      return jobApi.updateApplicationStatus(params);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['applications'] });
    },
  });

  return {
    applyToJob: applyToJob.mutate,
    updateStatus: updateApplicationStatus.mutate,
    isApplying: applyToJob.isPending,
    isUpdating: updateApplicationStatus.isPending,
  };
};
```

## Backend Services

### FastAPI Route Handler Pattern
Standard pattern for API endpoints with validation and error handling

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.job import JobSearchRequest, JobResponse
from app.services.job_discovery import JobDiscoveryService

router = APIRouter(prefix="/api/v1/jobs", tags=["jobs"])

@router.post("/search", response_model=List[JobResponse])
async def search_jobs(
    request: JobSearchRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
    job_service: JobDiscoveryService = Depends(get_job_service)
):
    """
    Search for relevant jobs based on user preferences and query.
    """
    try:
        jobs = await job_service.discover_relevant_jobs(
            user_id=current_user.id,
            search_criteria=request
        )
        return jobs
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Job search failed for user {current_user.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred"
        )
```

### Health Check Implementation Pattern
Comprehensive health check system for monitoring all service dependencies

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import asyncio
from datetime import datetime

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    environment: str
    services: Dict[str, Any]

class ServiceHealth(BaseModel):
    status: str
    response_time_ms: float
    details: Dict[str, Any] = {}

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Comprehensive health check for all system components"""
    start_time = asyncio.get_event_loop().time()
    
    services = {}
    overall_status = "healthy"
    
    # Check Database
    try:
        db_start = asyncio.get_event_loop().time()
        db_healthy = await check_database_health()
        db_time = (asyncio.get_event_loop().time() - db_start) * 1000
        
        services["database"] = ServiceHealth(
            status="healthy" if db_healthy else "unhealthy",
            response_time_ms=round(db_time, 2),
            details={"url": settings.DATABASE_URL.split("@")[1] if "@" in settings.DATABASE_URL else "hidden"}
        )
        
        if not db_healthy:
            overall_status = "degraded"
            
    except Exception as e:
        services["database"] = ServiceHealth(
            status="unhealthy",
            response_time_ms=0,
            details={"error": str(e)}
        )
        overall_status = "unhealthy"
    
    return HealthResponse(
        status=overall_status,
        timestamp=datetime.utcnow(),
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
        services=services
    )

@router.get("/health/ready")
async def readiness_check():
    """Kubernetes-style readiness check"""
    db_healthy = await check_database_health()
    redis_healthy = await redis_client.check_health()
    
    if db_healthy and redis_healthy:
        return {"status": "ready"}
    else:
        raise HTTPException(status_code=503, detail="Service not ready")

@router.get("/health/live")
async def liveness_check():
    """Kubernetes-style liveness check"""
    return {"status": "alive", "timestamp": datetime.utcnow()}
```

### Async Database Configuration Pattern
SQLAlchemy async setup with session management and health checks

```python
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create async engine for database operations
engine = create_async_engine(
    settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"),
    echo=settings.DEBUG,
    future=True
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for SQLAlchemy models
Base = declarative_base()

# Dependency to get database session
async def get_database_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Database health check
async def check_database_health() -> bool:
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(text("SELECT 1"))
            return result.fetchone() is not None
    except Exception as e:
        print(f"Database health check failed: {e}")
        return False
```

### Redis Client Pattern
Async Redis client with connection pooling and health monitoring

```python
import redis.asyncio as redis
from app.core.config import settings
import json
from typing import Any, Optional

class RedisClient:
    def __init__(self):
        self.redis_pool = None
    
    async def connect(self):
        """Initialize Redis connection pool"""
        self.redis_pool = redis.ConnectionPool.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
            max_connections=20
        )
    
    async def get_client(self) -> redis.Redis:
        """Get Redis client instance"""
        if not self.redis_pool:
            await self.connect()
        return redis.Redis(connection_pool=self.redis_pool)
    
    async def set_cache(self, key: str, value: Any, expiry: int = 3600):
        """Set cache value with expiry"""
        client = await self.get_client()
        serialized_value = json.dumps(value, default=str)
        await client.setex(key, expiry, serialized_value)
    
    async def get_cache(self, key: str) -> Optional[Any]:
        """Get cache value"""
        client = await self.get_client()
        value = await client.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return None
    
    async def check_health(self) -> bool:
        """Check Redis connection health"""
        try:
            client = await self.get_client()
            response = await client.ping()
            return response is True
        except Exception:
            return False

# Global Redis client instance
redis_client = RedisClient()
```

### Request Logging Middleware Pattern
Middleware for comprehensive request/response logging with timing

```python
import time
import logging
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Log request
        logger.info(f"Request: {request.method} {request.url.path}")
        
        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            
            # Log response
            logger.info(
                f"Response: {response.status_code} - "
                f"{request.method} {request.url.path} - "
                f"Time: {process_time:.4f}s"
            )
            
            # Add timing header
            response.headers["X-Process-Time"] = str(process_time)
            return response
            
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(
                f"Error: {str(e)} - "
                f"{request.method} {request.url.path} - "
                f"Time: {process_time:.4f}s"
            )
            raise
```

### FastAPI Application Configuration Pattern
Complete FastAPI app setup with lifespan events and middleware

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.core.redis_client import redis_client
from app.middleware.logging import LoggingMiddleware
from app.routers.health import router as health_router

# Configure logging
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    logger.info("Starting Job Application Automation System API")
    
    # Initialize Redis connection
    try:
        await redis_client.connect()
        logger.info("Redis connection established")
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Job Application Automation System API")
    
    # Close Redis connection
    try:
        await redis_client.close()
        logger.info("Redis connection closed")
    except Exception as e:
        logger.error(f"Error closing Redis connection: {e}")

# Create FastAPI application with lifespan events
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Job Application Automation System API - AI-powered job discovery and application assistance",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Add custom middleware
app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(health_router, prefix="/api/v1", tags=["health"])
```

### Service Layer Pattern
Service class template for business logic

```python
from typing import List, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.job_repository import JobRepository
from app.services.nlp_service import NLPService
from app.schemas.job import JobSearchRequest, JobResponse

class JobDiscoveryService:
    def __init__(
        self, 
        job_repo: JobRepository, 
        nlp_service: NLPService,
        db: AsyncSession
    ):
        self.job_repo = job_repo
        self.nlp_service = nlp_service
        self.db = db

    async def discover_relevant_jobs(
        self, 
        user_id: UUID, 
        search_criteria: JobSearchRequest
    ) -> List[JobResponse]:
        """
        Discover and rank jobs based on user profile and semantic similarity.
        """
        # Get user profile and preferences
        user_profile = await self.get_user_profile(user_id)
        
        # Generate user skills embedding
        user_vector = await self.nlp_service.generate_embedding(
            user_profile.skills_text
        )
        
        # Search jobs with vector similarity
        jobs = await self.job_repo.search_jobs_with_similarity(
            criteria=search_criteria,
            user_vector=user_vector,
            limit=50
        )
        
        # Apply business logic filtering
        filtered_jobs = await self._apply_user_preferences(jobs, user_id)
        
        # Score and rank results
        ranked_jobs = await self._rank_job_relevance(filtered_jobs, user_profile)
        
        return ranked_jobs

    async def _apply_user_preferences(
        self, 
        jobs: List[JobResponse], 
        user_id: UUID
    ) -> List[JobResponse]:
        """Apply user-specific filtering preferences."""
        user_prefs = await self.job_repo.get_user_preferences(user_id)
        
        if not user_prefs:
            return jobs
            
        filtered = []
        for job in jobs:
            # Filter by salary requirements
            if user_prefs.min_salary and job.salary_min:
                if job.salary_min < user_prefs.min_salary:
                    continue
                    
            # Filter by work arrangement
            if user_prefs.work_arrangements:
                if job.work_arrangement not in user_prefs.work_arrangements:
                    continue
                    
            # Filter by location if not remote
            if job.work_arrangement != 'remote' and user_prefs.locations:
                job_location = f"{job.location_city}, {job.location_state}"
                if job_location not in user_prefs.locations:
                    continue
                    
            filtered.append(job)
            
        return filtered
```

### Background Task Pattern
Celery task for asynchronous processing

```python
from celery import Celery
from typing import Dict, Any
import asyncio
from app.services.application_automation import ApplicationAutomationService
from app.services.resume_processor import ResumeProcessorService
from app.services.cover_letter_generator import CoverLetterGenerator

app = Celery('job_automation')

@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3})
def process_job_application(self, application_data: Dict[str, Any]):
    """
    Background task for processing complete job application workflow.
    """
    try:
        # Initialize services
        resume_service = ResumeProcessorService()
        cover_letter_service = CoverLetterGenerator()
        automation_service = ApplicationAutomationService()
        
        # Generate tailored resume
        resume_result = asyncio.run(
            resume_service.tailor_resume(
                user_id=application_data['user_id'],
                job_id=application_data['job_id']
            )
        )
        
        # Generate cover letter
        cover_letter_result = asyncio.run(
            cover_letter_service.generate_cover_letter(
                user_id=application_data['user_id'],
                job_id=application_data['job_id'],
                job_data=application_data['job_data']
            )
        )
        
        # Submit application if user approved
        if application_data.get('auto_submit', False):
            submission_result = asyncio.run(
                automation_service.submit_application(
                    application_id=application_data['application_id'],
                    resume_url=resume_result['file_url'],
                    cover_letter_content=cover_letter_result['content'],
                    job_url=application_data['job_url']
                )
            )
            
            return {
                'status': 'completed',
                'application_id': application_data['application_id'],
                'submitted': True,
                'submission_result': submission_result
            }
        
        return {
            'status': 'ready_for_review',
            'application_id': application_data['application_id'],
            'resume_url': resume_result['file_url'],
            'cover_letter_content': cover_letter_result['content']
        }
        
    except Exception as exc:
        logger.error(f"Application processing failed: {str(exc)}")
        raise self.retry(countdown=60)
```

## Data Access Patterns

### Repository Pattern
Database repository with async operations

```python
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_, func
from sqlalchemy.orm import selectinload
from typing import List, Optional
from uuid import UUID
from app.models.job import JobPosting, Company
from app.schemas.job import JobSearchRequest

class JobRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def search_jobs_with_similarity(
        self,
        criteria: JobSearchRequest,
        user_vector: List[float],
        limit: int = 50
    ) -> List[JobPosting]:
        """
        Search jobs using vector similarity and filters.
        """
        query = select(JobPosting).join(Company)
        
        # Apply filters
        filters = [JobPosting.is_active == True]
        
        if criteria.location:
            filters.append(
                or_(
                    JobPosting.location_city.ilike(f"%{criteria.location}%"),
                    JobPosting.work_arrangement == 'remote'
                )
            )
            
        if criteria.experience_level:
            filters.append(JobPosting.experience_level == criteria.experience_level)
            
        if criteria.work_arrangement:
            filters.append(JobPosting.work_arrangement == criteria.work_arrangement)
            
        query = query.where(and_(*filters))
        
        # Add vector similarity ordering
        query = query.order_by(
            JobPosting.embedding.cosine_distance(user_vector)
        ).limit(limit)
        
        # Include company data
        query = query.options(selectinload(JobPosting.company))
        
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_user_applications(
        self, 
        user_id: UUID,
        status: Optional[str] = None
    ) -> List[dict]:
        """Get user's job applications with status filtering."""
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

### Database Session Management
Async database session handling

```python
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from app.core.config import settings

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
    pool_recycle=300
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

@asynccontextmanager
async def get_db_session():
    """Context manager for database sessions."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

# Dependency for FastAPI
async def get_db():
    async with get_db_session() as session:
        yield session
```

## AI/ML Integration Patterns

### OpenAI Content Generation
Pattern for AI-powered content generation with error handling

```python
from openai import AsyncOpenAI
from typing import Dict, Any, Optional
import asyncio
from app.core.config import settings

class CoverLetterGenerator:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4"

    async def generate_cover_letter(
        self,
        user_profile: Dict[str, Any],
        job_posting: Dict[str, Any],
        company_info: Dict[str, Any],
        tone: str = "professional"
    ) -> Dict[str, Any]:
        """
        Generate personalized cover letter using GPT-4.
        """
        try:
            prompt = self._build_prompt(user_profile, job_posting, company_info, tone)
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=800,
                presence_penalty=0.1,
                frequency_penalty=0.1
            )
            
            content = response.choices[0].message.content
            
            # Calculate quality score
            quality_score = await self._calculate_quality_score(content, job_posting)
            
            return {
                'content': content,
                'quality_score': quality_score,
                'model_used': self.model,
                'token_count': response.usage.total_tokens,
                'generation_metadata': {
                    'temperature': 0.7,
                    'tone': tone,
                    'prompt_version': '1.0'
                }
            }
            
        except Exception as e:
            logger.error(f"Cover letter generation failed: {str(e)}")
            raise ValueError(f"Failed to generate cover letter: {str(e)}")

    def _build_prompt(
        self, 
        user_profile: Dict[str, Any], 
        job_posting: Dict[str, Any],
        company_info: Dict[str, Any],
        tone: str
    ) -> str:
        """Build context-rich prompt for cover letter generation."""
        return f"""
        Generate a personalized cover letter for this job application:

        Job Details:
        - Title: {job_posting['title']}
        - Company: {company_info['name']}
        - Key Requirements: {', '.join(job_posting.get('required_skills', []))}
        - Description: {job_posting.get('description', '')[:500]}

        Company Information:
        - Industry: {company_info.get('industry', 'Unknown')}
        - Size: {company_info.get('size_category', 'Unknown')}
        - Description: {company_info.get('description', '')[:300]}

        Candidate Profile:
        - Name: {user_profile['first_name']} {user_profile['last_name']}
        - Current Title: {user_profile.get('current_title', '')}
        - Experience: {user_profile.get('years_experience', 0)} years
        - Key Skills: {', '.join(user_profile.get('top_skills', []))}
        - Recent Achievement: {user_profile.get('recent_achievements', [''])[0]}

        Tone: {tone}
        Length: 250-300 words
        Include: 2-3 specific connections between candidate skills and job requirements
        """

    async def _calculate_quality_score(
        self, 
        content: str, 
        job_posting: Dict[str, Any]
    ) -> float:
        """Calculate content quality score based on various factors."""
        score = 0.8  # Base score
        
        # Check for required skills mentions
        required_skills = job_posting.get('required_skills', [])
        if required_skills:
            mentions = sum(1 for skill in required_skills if skill.lower() in content.lower())
            score += (mentions / len(required_skills)) * 0.15
            
        # Check word count (target: 250-300 words)
        word_count = len(content.split())
        if 250 <= word_count <= 300:
            score += 0.05
            
        return min(score, 1.0)
```

### Vector Embedding Service
Service for generating and managing embeddings

```python
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any
import numpy as np
from app.core.config import settings

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = 384

    async def generate_job_embedding(self, job_data: Dict[str, Any]) -> List[float]:
        """Generate embedding for job posting."""
        # Combine relevant job text fields
        text_components = [
            job_data.get('title', ''),
            job_data.get('description', ''),
            ' '.join(job_data.get('required_skills', [])),
            ' '.join(job_data.get('preferred_skills', []))
        ]
        
        combined_text = ' '.join(filter(None, text_components))
        embedding = self.model.encode(combined_text)
        return embedding.tolist()

    async def generate_user_profile_embedding(self, user_profile: Dict[str, Any]) -> List[float]:
        """Generate embedding for user profile."""
        text_components = [
            user_profile.get('current_title', ''),
            ' '.join(user_profile.get('skills', [])),
            ' '.join(user_profile.get('experience_descriptions', [])),
            user_profile.get('summary', '')
        ]
        
        combined_text = ' '.join(filter(None, text_components))
        embedding = self.model.encode(combined_text)
        return embedding.tolist()

    def calculate_similarity(self, embedding1: List[float], embedding2: List[float]) -> float:
        """Calculate cosine similarity between two embeddings."""
        vec1 = np.array(embedding1)
        vec2 = np.array(embedding2)
        
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
            
        return float(dot_product / (norm1 * norm2))
```

## Browser Automation Patterns

### Playwright Anti-Detection Pattern
Browser automation with stealth capabilities

```python
from playwright.async_api import async_playwright, Page, Browser
import random
import asyncio
from typing import Dict, Any, Optional
from app.core.config import settings

class StealthBrowser:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]

    async def create_stealth_context(self):
        """Create browser context with anti-detection measures."""
        playwright = await async_playwright().start()
        
        browser = await playwright.chromium.launch(
            headless=settings.HEADLESS_MODE,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--disable-extensions',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-gpu',
                '--disable-background-timer-throttling',
                '--disable-backgrounding-occluded-windows',
                '--disable-renderer-backgrounding'
            ]
        )

        context = await browser.new_context(
            user_agent=random.choice(self.user_agents),
            viewport={'width': 1920, 'height': 1080},
            java_script_enabled=True,
            accept_downloads=True,
            ignore_https_errors=True
        )

        # Remove webdriver property
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });
            
            // Mock plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5],
            });
            
            // Mock languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en'],
            });
        """)

        return context, browser

    async def human_like_delay(self, min_ms: int = 500, max_ms: int = 2000):
        """Add human-like delays between actions."""
        delay = random.uniform(min_ms, max_ms) / 1000
        await asyncio.sleep(delay)

    async def type_like_human(self, page: Page, selector: str, text: str):
        """Type text with human-like delays."""
        await page.focus(selector)
        await self.human_like_delay(200, 500)
        
        for char in text:
            await page.keyboard.type(char)
            await asyncio.sleep(random.uniform(0.05, 0.15))

    async def click_with_movement(self, page: Page, selector: str):
        """Click with mouse movement simulation."""
        element = await page.wait_for_selector(selector)
        box = await element.bounding_box()
        
        if box:
            # Move to near the element first
            await page.mouse.move(
                box['x'] + box['width'] / 2 + random.uniform(-5, 5),
                box['y'] + box['height'] / 2 + random.uniform(-5, 5)
            )
            await self.human_like_delay(100, 300)
            
            # Click the element
            await element.click()
```

## Error Handling Patterns

### API Error Handler
Standardized error handling for API responses

```python
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from app.core.logging import logger
import traceback

class APIError(Exception):
    def __init__(self, message: str, status_code: int = 500, details: dict = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}

async def api_error_handler(request: Request, exc: APIError):
    """Global API error handler."""
    logger.error(f"API Error: {exc.message}", extra={
        'status_code': exc.status_code,
        'details': exc.details,
        'path': request.url.path,
        'method': request.method
    })
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'success': False,
            'error': {
                'message': exc.message,
                'code': exc.status_code,
                'details': exc.details
            },
            'meta': {
                'timestamp': datetime.utcnow().isoformat(),
                'path': request.url.path
            }
        }
    )

async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {str(exc)}", extra={
        'traceback': traceback.format_exc(),
        'path': request.url.path,
        'method': request.method
    })
    
    return JSONResponse(
        status_code=500,
        content={
            'success': False,
            'error': {
                'message': 'Internal server error',
                'code': 500
            },
            'meta': {
                'timestamp': datetime.utcnow().isoformat(),
                'path': request.url.path
            }
        }
    )
```

## Testing Patterns

### Component Test Template
Testing pattern for React components

```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { vi } from 'vitest';
import { JobCard } from './JobCard';
import { mockJob } from '../../../test/fixtures/jobs';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
      mutations: { retry: false },
    },
  });

  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('JobCard', () => {
  const mockOnApply = vi.fn();
  const mockOnSave = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders job information correctly', () => {
    render(
      <JobCard 
        job={mockJob} 
        onApply={mockOnApply} 
        onSave={mockOnSave} 
      />,
      { wrapper: createWrapper() }
    );

    expect(screen.getByText(mockJob.title)).toBeInTheDocument();
    expect(screen.getByText(mockJob.company.name)).toBeInTheDocument();
    expect(screen.getByText(mockJob.location)).toBeInTheDocument();
  });

  it('calls onApply when apply button is clicked', async () => {
    render(
      <JobCard 
        job={mockJob} 
        onApply={mockOnApply} 
        onSave={mockOnSave} 
      />,
      { wrapper: createWrapper() }
    );

    const applyButton = screen.getByText('Apply Now');
    fireEvent.click(applyButton);

    expect(mockOnApply).toHaveBeenCalledWith(mockJob.id);
  });

  it('shows similarity score when provided', () => {
    render(
      <JobCard 
        job={mockJob} 
        onApply={mockOnApply} 
        onSave={mockOnSave} 
        similarity={0.85}
      />,
      { wrapper: createWrapper() }
    );

    expect(screen.getByText('85% match')).toBeInTheDocument();
  });
});
```

### API Test Pattern
Testing pattern for FastAPI endpoints

```python
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app
from app.models.user import User
from app.models.job import JobPosting
from tests.fixtures.auth import create_test_user
from tests.fixtures.jobs import create_test_job

@pytest.mark.asyncio
async def test_search_jobs_success(
    async_client: AsyncClient,
    db_session: AsyncSession,
    authenticated_user: User
):
    """Test successful job search."""
    # Create test jobs
    job1 = await create_test_job(db_session, title="Python Developer")
    job2 = await create_test_job(db_session, title="JavaScript Developer")
    
    # Search for Python jobs
    response = await async_client.post(
        "/api/v1/jobs/search",
        json={
            "query": "Python",
            "location": "San Francisco",
            "experience_level": "mid"
        },
        headers={"Authorization": f"Bearer {authenticated_user.token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert any(job["title"] == "Python Developer" for job in data)

@pytest.mark.asyncio
async def test_search_jobs_unauthorized(async_client: AsyncClient):
    """Test job search without authentication."""
    response = await async_client.post(
        "/api/v1/jobs/search",
        json={"query": "Python"}
    )
    
    assert response.status_code == 401
    assert "unauthorized" in response.json()["error"]["message"].lower()

@pytest.mark.asyncio 
async def test_search_jobs_validation_error(
    async_client: AsyncClient,
    authenticated_user: User
):
    """Test job search with invalid parameters."""
    response = await async_client.post(
        "/api/v1/jobs/search",
        json={"query": ""},  # Empty query should fail validation
        headers={"Authorization": f"Bearer {authenticated_user.token}"}
    )
    
    assert response.status_code == 400
    assert "validation" in response.json()["error"]["message"].lower()
```

---
*This code snippets file contains real, production-ready patterns for the Job Application Automation System. Update regularly as new patterns emerge during development.* 