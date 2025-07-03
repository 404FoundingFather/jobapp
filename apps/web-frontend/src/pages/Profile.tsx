
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card'
import { Button } from '../components/ui/button'

export default function Profile() {
  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-foreground mb-2">
            Profile & Settings
          </h1>
          <p className="text-lg text-muted-foreground">
            Manage your profile, resume, and job preferences
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Personal Information</CardTitle>
                <CardDescription>
                  Update your personal details and contact information
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium mb-2">First Name</label>
                    <input 
                      type="text" 
                      placeholder="John"
                      className="w-full px-3 py-2 border border-input rounded-md bg-background"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">Last Name</label>
                    <input 
                      type="text" 
                      placeholder="Doe"
                      className="w-full px-3 py-2 border border-input rounded-md bg-background"
                    />
                  </div>
                  <div className="md:col-span-2">
                    <label className="block text-sm font-medium mb-2">Email</label>
                    <input 
                      type="email" 
                      placeholder="john.doe@example.com"
                      className="w-full px-3 py-2 border border-input rounded-md bg-background"
                    />
                  </div>
                </div>
                <div className="mt-4">
                  <Button>Save Changes</Button>
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Resume Management</CardTitle>
                <CardDescription>
                  Upload and manage your resume
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="border-2 border-dashed border-border rounded-lg p-8 text-center">
                  <div className="w-12 h-12 bg-muted rounded-lg mx-auto mb-4 flex items-center justify-center">
                    <svg className="w-6 h-6 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                  </div>
                  <h3 className="text-lg font-semibold mb-2">Upload your resume</h3>
                  <p className="text-muted-foreground mb-4">
                    Drag and drop your resume file or click to browse
                  </p>
                  <Button>Choose File</Button>
                </div>
              </CardContent>
            </Card>
          </div>

          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Job Preferences</CardTitle>
                <CardDescription>
                  Set your job search preferences
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium mb-2">Preferred Job Title</label>
                    <input 
                      type="text" 
                      placeholder="Software Engineer"
                      className="w-full px-3 py-2 border border-input rounded-md bg-background"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">Location</label>
                    <input 
                      type="text" 
                      placeholder="Remote, San Francisco"
                      className="w-full px-3 py-2 border border-input rounded-md bg-background"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">Salary Range</label>
                    <select className="w-full px-3 py-2 border border-input rounded-md bg-background">
                      <option>Not specified</option>
                      <option>$50k - $75k</option>
                      <option>$75k - $100k</option>
                      <option>$100k - $150k</option>
                      <option>$150k+</option>
                    </select>
                  </div>
                </div>
                <div className="mt-4">
                  <Button className="w-full">Save Preferences</Button>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
} 