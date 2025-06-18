# UI Design Specifications

## Design Philosophy

### Core Design Principles
1. **Simplicity** - Clean, uncluttered interfaces that focus on job application workflow
2. **Efficiency** - Streamlined interactions that minimize time to complete tasks
3. **Transparency** - Clear visibility into automation processes and application status
4. **Trust** - Professional appearance that builds confidence in automated processes
5. **Accessibility** - WCAG 2.1 AA compliance for inclusive job searching

### User Experience Goals
- **Intuitive Navigation:** Users can navigate job discovery and application management without training
- **Fast Performance:** All interactions feel instant and responsive (<100ms UI feedback)
- **Clear Progress:** Users always understand where they are in the application process
- **Accessibility:** Screen reader compatible and keyboard navigable throughout

---

## Visual Identity

### Color Palette
```css
/* Primary Colors */
--primary-50: #eff6ff;    /* Light blue backgrounds */
--primary-100: #dbeafe;
--primary-500: #3b82f6;   /* Primary brand blue */
--primary-600: #2563eb;
--primary-700: #1d4ed8;
--primary-900: #1e3a8a;   /* Dark blue text */

/* Secondary Colors */
--secondary-50: #f8fafc;
--secondary-500: #64748b;
--secondary-900: #0f172a;

/* Neutral Colors */
--neutral-50: #f9fafb;          /* Light backgrounds */
--neutral-100: #f3f4f6;
--neutral-500: #6b7280;        /* Secondary text */
--neutral-700: #374151;        /* Primary text */
--neutral-900: #111827;        /* Headings */

/* Semantic Colors */
--success-color: #10b981;       /* Applied status */
--warning-color: #f59e0b;       /* Pending status */
--error-color: #ef4444;         /* Rejected status */
--info-color: #3b82f6;          /* Information states */
```

### Typography
```css
/* Font Families */
--font-sans: 'Inter', system-ui, sans-serif;       /* Primary text font */
--font-mono: 'JetBrains Mono', monospace;          /* Code/data font */

/* Font Sizes */
--text-xs: 0.75rem;              /* 12px - Small labels */
--text-sm: 0.875rem;             /* 14px - Body text */
--text-base: 1rem;               /* 16px - Default size */
--text-lg: 1.125rem;             /* 18px - Large text */
--text-xl: 1.25rem;              /* 20px - Small headings */
--text-2xl: 1.5rem;              /* 24px - Medium headings */
--text-3xl: 1.875rem;            /* 30px - Large headings */

/* Font Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;

/* Line Heights */
--leading-tight: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.75;
```

### Spacing System
```css
/* Spacing Scale (4px base unit) */
--space-1: 0.25rem;           /* 4px */
--space-2: 0.5rem;            /* 8px */
--space-3: 0.75rem;           /* 12px */
--space-4: 1rem;              /* 16px - Base unit */
--space-6: 1.5rem;            /* 24px */
--space-8: 2rem;              /* 32px */
--space-12: 3rem;             /* 48px */
--space-16: 4rem;             /* 64px */
```

---

## Component Library

### Basic Components

#### Button
```typescript
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'outline' | 'ghost' | 'destructive';
  size: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  icon?: React.ReactNode;
  children: React.ReactNode;
  onClick?: () => void;
}

// Usage Examples:
<Button variant="primary" size="md">Apply Now</Button>
<Button variant="outline" size="sm" icon={<Heart />}>Save Job</Button>
<Button variant="destructive" loading>Submitting...</Button>
```

#### Input Field
```typescript
interface InputProps {
  type: 'text' | 'email' | 'password' | 'search' | 'url';
  label: string;
  placeholder?: string;
  error?: string;
  required?: boolean;
  disabled?: boolean;
  value: string;
  onChange: (value: string) => void;
  icon?: React.ReactNode;
}

// Usage:
<Input 
  type="search" 
  label="Job Title" 
  placeholder="e.g., Software Engineer"
  icon={<Search />}
  required 
/>
```

#### Job Card
```typescript
interface JobCardProps {
  job: Job;
  similarity?: number;
  onApply: (jobId: string) => void;
  onSave: (jobId: string) => void;
  isApplying?: boolean;
  isSaved?: boolean;
}

// Key Features:
// - Similarity score badge
// - Company logo placeholder
// - Job details (title, company, location, salary)
// - Action buttons (Apply, Save)
// - Loading states
```

#### Application Status Badge
```typescript
interface StatusBadgeProps {
  status: ApplicationStatus;
  size?: 'sm' | 'md';
}

// Status Colors:
// - pending: yellow
// - submitted: blue  
// - reviewing: purple
// - interviewed: green
// - rejected: red
// - offered: emerald
```

### Form Components

#### Search Filters
```typescript
interface SearchFiltersProps {
  filters: JobSearchFilters;
  onFiltersChange: (filters: Partial<JobSearchFilters>) => void;
  isLoading?: boolean;
}

// Includes:
// - Location autocomplete
// - Experience level select
// - Work arrangement chips
// - Salary range slider
// - Date posted filter
```

#### Resume Upload
```typescript
interface ResumeUploadProps {
  onUpload: (file: File) => void;
  currentResume?: string;
  isUploading?: boolean;
  error?: string;
}

// Features:
// - Drag & drop zone
// - File type validation
// - Upload progress
// - Preview capability
```

---

## Layout Patterns

### Main Application Layout
```typescript
// Layout Structure
<div className="min-h-screen bg-gray-50">
  {/* Navigation Header */}
  <header className="bg-white border-b border-gray-200">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between items-center py-4">
        <Logo />
        <NavigationMenu />
        <UserMenu />
      </div>
    </div>
  </header>
  
  {/* Main Content Area */}
  <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
      {/* Sidebar */}
      <aside className="lg:col-span-3">
        <NavigationSidebar />
      </aside>
      
      {/* Page Content */}
      <div className="lg:col-span-9">
        <PageContent />
      </div>
    </div>
  </main>
</div>
```

### Job Discovery Layout
```typescript
// Job Search Results Layout
<div className="space-y-6">
  {/* Search Header */}
  <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
    <div>
      <h1 className="text-2xl font-bold text-gray-900">Job Discovery</h1>
      <p className="text-gray-600">
        {jobCount} jobs found matching your criteria
      </p>
    </div>
    <div className="flex gap-3">
      <SortDropdown />
      <FilterToggle />
    </div>
  </div>

  <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
    {/* Filters Sidebar */}
    <div className="lg:col-span-1">
      <SearchFilters />
    </div>
    
    {/* Job Results */}
    <div className="lg:col-span-3">
      <div className="grid gap-4">
        {jobs.map(job => (
          <JobCard key={job.id} job={job} />
        ))}
      </div>
      <Pagination />
    </div>
  </div>
</div>
```

### Application Dashboard Layout
```typescript
// Applications Management Layout
<div className="space-y-6">
  {/* Dashboard Header */}
  <div className="bg-white rounded-lg border border-gray-200 p-6">
    <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Applications</h1>
        <ApplicationStats />
      </div>
      <QuickActions />
    </div>
  </div>

  {/* Applications List/Grid */}
  <div className="grid gap-6">
    <ApplicationFilters />
    <ApplicationsList />
  </div>
</div>
```

---

## Responsive Design

### Breakpoints
```css
/* Mobile First Approach */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
@media (min-width: 1536px) { /* 2xl */ }
```

### Mobile Adaptations
- **Navigation:** Collapsible hamburger menu with slide-out sidebar
- **Job Cards:** Single column layout with compact information display
- **Filters:** Modal overlay instead of sidebar
- **Tables:** Horizontal scroll with sticky columns for application data
- **Forms:** Full-width inputs with larger touch targets (44px minimum)

### Touch Interactions
- **Swipe Actions:** Swipe job cards to save/apply
- **Pull to Refresh:** Refresh job listings and application status
- **Touch Feedback:** Visual feedback for all interactive elements
- **Gesture Navigation:** Pinch to zoom on document previews

---

## Interaction Design

### Loading States
```typescript
// Component Loading Patterns
<Button loading>
  <Spinner className="mr-2" />
  Applying...
</Button>

<JobCard skeleton /> // Skeleton loading for job cards

<div className="animate-pulse">
  <div className="h-4 bg-gray-200 rounded w-3/4 mb-2" />
  <div className="h-4 bg-gray-200 rounded w-1/2" />
</div>
```

### Error States
```typescript
// Error Handling Patterns
<ErrorBoundary fallback={<ErrorFallback />}>
  <JobSearchResults />
</ErrorBoundary>

<Toast variant="error">
  Failed to apply to job. Please try again.
</Toast>

<EmptyState
  icon={<Briefcase />}
  title="No jobs found"
  description="Try adjusting your search criteria"
  action={<Button>Clear Filters</Button>}
/>
```

### Success Feedback
```typescript
// Success Confirmation Patterns
<Toast variant="success">
  Application submitted successfully!
</Toast>

<SuccessModal
  title="Application Sent"
  description="Your application has been submitted to TechCorp"
  action={<Button>View Application</Button>}
/>
```

---

## Accessibility Guidelines

### Keyboard Navigation
- **Tab Order:** Logical tab sequence through all interactive elements
- **Focus Indicators:** Clear visual focus indicators with 3:1 contrast ratio
- **Shortcuts:** Keyboard shortcuts for common actions (Ctrl+K for search)
- **Escape Key:** Closes modals and dropdowns consistently

### Screen Reader Support
```typescript
// Accessibility Attributes
<button 
  aria-label="Apply to Software Engineer position at TechCorp"
  aria-describedby="job-description"
>
  Apply Now
</button>

<div role="status" aria-live="polite">
  {applicationCount} applications submitted
</div>

<nav aria-label="Job search pagination">
  <PaginationControls />
</nav>
```

### Color Accessibility
- **Contrast Ratios:** Minimum 4.5:1 for normal text, 3:1 for large text
- **Color Independence:** Information never conveyed by color alone
- **Focus Indicators:** 3:1 contrast ratio against adjacent colors

### Motion & Animation
- **Reduced Motion:** Respect `prefers-reduced-motion` media query
- **Duration:** Animations under 500ms for UI feedback
- **Purpose:** Animations enhance understanding, not decoration

---

## Animation & Transitions

### Micro-Interactions
```css
/* Button Hover Effects */
.button {
  transition: all 0.2s ease-in-out;
}

.button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Card Hover Effects */
.job-card {
  transition: box-shadow 0.3s ease;
}

.job-card:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}
```

### Page Transitions
```typescript
// React Router with Framer Motion
<AnimatePresence mode="wait">
  <motion.div
    key={location.pathname}
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -20 }}
    transition={{ duration: 0.3 }}
  >
    <Outlet />
  </motion.div>
</AnimatePresence>
```

### Progress Indicators
```typescript
// Application Progress Animation
<motion.div
  className="bg-primary-500 h-2 rounded-full"
  initial={{ width: 0 }}
  animate={{ width: `${progress}%` }}
  transition={{ duration: 0.5, ease: "easeOut" }}
/>
```

---

## Component States

### Interactive States
- **Default:** Base appearance
- **Hover:** Subtle elevation and color changes
- **Active:** Pressed state with slight scale down
- **Focus:** Clear focus ring for keyboard navigation
- **Disabled:** Reduced opacity and no pointer events
- **Loading:** Spinner or skeleton loading state

### Data States
- **Empty:** Helpful empty states with clear actions
- **Error:** Error messages with retry options
- **Loading:** Progressive loading with skeleton screens
- **Success:** Confirmation messages and next steps

---

## Design Tokens

### Shadows
```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
```

### Border Radius
```css
--radius-sm: 0.125rem;   /* 2px */
--radius-md: 0.375rem;   /* 6px */
--radius-lg: 0.5rem;     /* 8px */
--radius-xl: 0.75rem;    /* 12px */
```

### Z-Index Scale
```css
--z-dropdown: 1000;
--z-sticky: 1020;
--z-fixed: 1030;
--z-modal: 1040;
--z-popover: 1050;
--z-tooltip: 1060;
```

---

## Implementation Guidelines

### Component Development
- Use TypeScript for all components with proper prop interfaces
- Implement compound components for complex UI patterns
- Follow atomic design principles (atoms, molecules, organisms)
- Use Tailwind CSS utility classes with custom CSS for complex animations
- Implement proper error boundaries for robust user experience

### Performance Considerations
- Lazy load components that are not immediately visible
- Optimize images with proper sizing and WebP format
- Use React.memo for expensive re-renders
- Implement virtual scrolling for large job lists
- Bundle split routes for faster initial load times

### Testing Strategy
- Unit tests for individual components with React Testing Library
- Integration tests for complete user workflows
- Visual regression testing with Chromatic or Percy
- Accessibility testing with axe-core
- Performance testing with Lighthouse CI

---
*This UI design specification should be updated as the design system evolves and new patterns emerge during development. Maintain consistency with these guidelines while adapting to user feedback and usability insights.* 