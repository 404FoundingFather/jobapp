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
        <div className="container mx-auto px-4">
          <nav className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-8">
              <Link href="/" className="text-xl font-bold text-foreground">
                JobApp
              </Link>
              <div className="hidden md:flex items-center space-x-6">
                <Link 
                  href="/" 
                  className={`text-sm font-medium transition-colors hover:text-primary ${
                    isActive('/') ? 'text-primary' : 'text-muted-foreground'
                  }`}
                >
                  Dashboard
                </Link>
                <Link 
                  href="/jobs" 
                  className={`text-sm font-medium transition-colors hover:text-primary ${
                    isActive('/jobs') ? 'text-primary' : 'text-muted-foreground'
                  }`}
                >
                  Jobs
                </Link>
                <Link 
                  href="/applications" 
                  className={`text-sm font-medium transition-colors hover:text-primary ${
                    isActive('/applications') ? 'text-primary' : 'text-muted-foreground'
                  }`}
                >
                  Applications
                </Link>
                <Link 
                  href="/profile" 
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
              <UserAvatar userName="John Doe" />
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