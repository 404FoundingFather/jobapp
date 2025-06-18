import React from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Button } from '../components/ui/button'

interface LayoutProps {
  children: React.ReactNode
}

export default function Layout({ children }: LayoutProps) {
  const location = useLocation()

  const isActive = (path: string) => {
    return location.pathname === path
  }

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
  )
} 