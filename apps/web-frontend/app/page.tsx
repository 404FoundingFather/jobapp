import Dashboard from '../src/pages/Dashboard'
import ProtectedRoute from '../src/components/auth/ProtectedRoute'

export default function HomePage() {
  return (
    <ProtectedRoute>
      <Dashboard />
    </ProtectedRoute>
  )
} 