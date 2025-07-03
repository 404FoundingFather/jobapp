# UI Design & Frontend Architecture

## Frontend Technology Stack

### Core Framework
- **Next.js 14.2.30** - React framework with app directory structure
- **TypeScript 5.0+** - Type-safe development with strict mode
- **Tailwind CSS 3.3+** - Utility-first CSS framework
- **shadcn/ui** - High-quality component library built on Radix UI

### State Management & Data
- **Zustand 4.4+** - Lightweight state management for client-side state
- **TanStack React Query 5.0+** - Server state management and caching
- **React Hook Form 7.48+** - Performant forms with validation
- **Zod 3.22+** - TypeScript-first schema validation

### UI Components & Styling
- **Radix UI** - Unstyled, accessible component primitives
- **Lucide React** - Beautiful, customizable icons
- **Class Variance Authority (CVA)** - Type-safe component variants
- **Tailwind Merge** - Intelligent class merging utility

### Development Tools
- **ESLint** - Code linting and quality enforcement
- **Prettier** - Code formatting
- **TypeScript** - Static type checking
- **Next.js App Router** - File-based routing system

## Project Structure

### Next.js App Directory Structure
```
apps/web-frontend/
├── app/                          # Next.js 13+ app directory
│   ├── layout.tsx               # Root layout with metadata
│   ├── page.tsx                 # Home page (Dashboard)
│   ├── jobs/
│   │   └── page.tsx            # Jobs page
│   ├── applications/
│   │   └── page.tsx            # Applications page
│   └── profile/
│       └── page.tsx            # Profile page
├── src/
│   ├── components/              # Reusable UI components
│   │   ├── ui/                 # shadcn/ui components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   └── avatar.tsx
│   │   ├── Layout.tsx          # Main layout component
│   │   └── user/
│   │       └── UserAvatar.tsx
│   ├── pages/                   # Page components (legacy structure)
│   │   ├── Dashboard.tsx
│   │   ├── Jobs.tsx
│   │   ├── Applications.tsx
│   │   └── Profile.tsx
│   ├── hooks/                   # Custom React hooks
│   ├── stores/                  # Zustand state stores
│   ├── services/                # API client services
│   ├── types/                   # TypeScript type definitions
│   ├── lib/                     # Utility functions
│   │   └── utils.ts            # Common utilities (cn function)
│   └── index.css               # Global styles
├── public/                      # Static assets
├── next.config.js              # Next.js configuration
├── tailwind.config.js          # Tailwind CSS configuration
├── tsconfig.json               # TypeScript configuration
└── package.json                # Dependencies and scripts
```

## Component Architecture

### Design System Principles
1. **Accessibility First** - All components built on Radix UI primitives
2. **Type Safety** - Full TypeScript integration with strict mode
3. **Consistency** - Unified design tokens and spacing system
4. **Reusability** - Modular components with clear interfaces
5. **Performance** - Optimized rendering and bundle splitting

### Component Categories

#### 1. UI Primitives (shadcn/ui)
- **Button** - Primary, secondary, outline, ghost variants
- **Card** - Content containers with consistent spacing
- **Avatar** - User profile images with fallbacks
- **Dialog** - Modal dialogs and overlays
- **Dropdown Menu** - Context menus and navigation
- **Select** - Form select components
- **Toast** - Notification system

#### 2. Layout Components
- **Layout** - Main application layout with navigation
- **Navigation** - Header navigation with active states
- **Sidebar** - Collapsible sidebar navigation
- **Footer** - Application footer

#### 3. Page Components
- **Dashboard** - Main application dashboard
- **Jobs** - Job listing and management
- **Applications** - Application tracking
- **Profile** - User profile management

#### 4. Form Components
- **Form Fields** - Input, textarea, select components
- **Form Validation** - Error states and validation messages
- **Form Layout** - Consistent form spacing and alignment

## Styling System

### Tailwind CSS Configuration
```javascript
// tailwind.config.js
module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
```

### CSS Variables (Design Tokens)
```css
/* src/index.css */
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --card: 0 0% 100%;
  --card-foreground: 222.2 84% 4.9%;
  --popover: 0 0% 100%;
  --popover-foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96%;
  --secondary-foreground: 222.2 84% 4.9%;
  --muted: 210 40% 96%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --accent: 210 40% 96%;
  --accent-foreground: 222.2 84% 4.9%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;
  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;
  --radius: 0.5rem;
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --card: 222.2 84% 4.9%;
  --card-foreground: 210 40% 98%;
  --popover: 222.2 84% 4.9%;
  --popover-foreground: 210 40% 98%;
  --primary: 210 40% 98%;
  --primary-foreground: 222.2 47.4% 11.2%;
  --secondary: 217.2 32.6% 17.5%;
  --secondary-foreground: 210 40% 98%;
  --muted: 217.2 32.6% 17.5%;
  --muted-foreground: 215 20.2% 65.1%;
  --accent: 217.2 32.6% 17.5%;
  --accent-foreground: 210 40% 98%;
  --destructive: 0 62.8% 30.6%;
  --destructive-foreground: 210 40% 98%;
  --border: 217.2 32.6% 17.5%;
  --input: 217.2 32.6% 17.5%;
  --ring: 212.7 26.8% 83.9%;
}
```

## Component Examples

### Button Component
```typescript
// src/components/ui/button.tsx
import React from 'react'
import { cn } from '../../lib/utils'

const Button = React.forwardRef<HTMLButtonElement, React.ButtonHTMLAttributes<HTMLButtonElement>>(
  (props, ref) => {
    return (
      <button
        className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        ref={ref}
        {...props}
      />
    )
  }
)

Button.displayName = 'Button'

export { Button }
```

### Layout Component
```typescript
// src/components/Layout.tsx
'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { Button } from '../components/ui/button'
import { UserAvatar } from './user/UserAvatar'

interface LayoutProps {
  children: React.ReactNode
}

export default function Layout({ children }: LayoutProps) {
  const pathname = usePathname()

  const isActive = (path: string) => {
    return pathname === path
  }

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        {/* Navigation content */}
      </header>
      <main>
        {children}
      </main>
    </div>
  )
}
```

## Routing & Navigation

### Next.js App Router Structure
- **File-based Routing** - Automatic route generation based on file structure
- **Layout Nesting** - Shared layouts with nested routing
- **Dynamic Routes** - Parameter-based routing for dynamic content
- **Loading States** - Built-in loading UI for route transitions

### Navigation Patterns
- **Active States** - Visual feedback for current page
- **Breadcrumbs** - Hierarchical navigation context
- **Mobile Responsive** - Collapsible navigation for mobile devices
- **Accessibility** - Keyboard navigation and screen reader support

## State Management

### Client State (Zustand)
```typescript
// src/stores/userStore.ts
import { create } from 'zustand'

interface UserState {
  user: User | null
  setUser: (user: User | null) => void
  isAuthenticated: boolean
}

export const useUserStore = create<UserState>((set) => ({
  user: null,
  setUser: (user) => set({ user, isAuthenticated: !!user }),
  isAuthenticated: false,
}))
```

### Server State (React Query)
```typescript
// src/hooks/useJobs.ts
import { useQuery } from '@tanstack/react-query'
import { fetchJobs } from '../services/api'

export const useJobs = () => {
  return useQuery({
    queryKey: ['jobs'],
    queryFn: fetchJobs,
    staleTime: 5 * 60 * 1000, // 5 minutes
  })
}
```

## Form Handling

### React Hook Form with Zod
```typescript
// src/components/JobForm.tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'

const jobSchema = z.object({
  title: z.string().min(1, 'Title is required'),
  company: z.string().min(1, 'Company is required'),
  location: z.string().optional(),
})

type JobFormData = z.infer<typeof jobSchema>

export function JobForm() {
  const form = useForm<JobFormData>({
    resolver: zodResolver(jobSchema),
  })

  return (
    <form onSubmit={form.handleSubmit(onSubmit)}>
      {/* Form fields */}
    </form>
  )
}
```

## Performance Optimization

### Next.js Optimizations
- **Automatic Code Splitting** - Route-based code splitting
- **Image Optimization** - Next.js Image component with optimization
- **Static Generation** - Pre-rendered pages for better performance
- **Incremental Static Regeneration** - Dynamic content with static benefits

### Bundle Optimization
- **Tree Shaking** - Unused code elimination
- **Dynamic Imports** - Lazy loading of components
- **Bundle Analysis** - Webpack bundle analyzer for size monitoring

## Accessibility

### WCAG 2.1 Compliance
- **Keyboard Navigation** - Full keyboard accessibility
- **Screen Reader Support** - Proper ARIA labels and roles
- **Color Contrast** - WCAG AA contrast ratios
- **Focus Management** - Visible focus indicators

### Component Accessibility
- **Semantic HTML** - Proper HTML structure
- **ARIA Labels** - Descriptive labels for screen readers
- **Focus Traps** - Modal and dialog focus management
- **Skip Links** - Keyboard navigation shortcuts

## Responsive Design

### Breakpoint Strategy
- **Mobile First** - Design for mobile, enhance for desktop
- **Flexible Grid** - CSS Grid and Flexbox for responsive layouts
- **Touch Targets** - Minimum 44px touch targets for mobile
- **Viewport Meta** - Proper viewport configuration

### Responsive Patterns
- **Collapsible Navigation** - Mobile-friendly navigation
- **Flexible Typography** - Responsive font sizes
- **Adaptive Images** - Responsive image handling
- **Touch Interactions** - Mobile-optimized interactions

## Migration Notes

### Recent Changes (July 2024)
- **Framework Migration** - Successfully migrated from Vite to Next.js 14
- **Routing Update** - Migrated from React Router to Next.js App Router
- **Build System** - Resolved critical build issues with new framework
- **Component Updates** - Updated components to use Next.js patterns

### Benefits of Next.js Migration
- **Better React Integration** - Native React support without plugin conflicts
- **Improved Performance** - Built-in optimizations and code splitting
- **Enhanced Developer Experience** - Better TypeScript support and debugging
- **Production Ready** - Optimized build process and deployment
- **File-based Routing** - Simpler and more intuitive routing system

## Development Workflow

### Component Development
1. **Create Component** - Use shadcn/ui CLI or manual creation
2. **Add Types** - TypeScript interfaces and props
3. **Style Component** - Tailwind CSS with design tokens
4. **Test Component** - Unit tests and accessibility testing
5. **Document Component** - Storybook or component documentation

### Styling Guidelines
- **Utility Classes** - Prefer Tailwind utility classes
- **Component Variants** - Use CVA for component variants
- **Design Tokens** - Use CSS variables for consistent theming
- **Responsive Design** - Mobile-first responsive approach

### Code Quality
- **TypeScript Strict** - Enable strict TypeScript mode
- **ESLint Rules** - Consistent code style and quality
- **Prettier Formatting** - Automated code formatting
- **Component Testing** - Unit tests for all components

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