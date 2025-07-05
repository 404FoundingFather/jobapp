import Applications from '../../src/pages/Applications'
import ProtectedRoute from '../../src/components/auth/ProtectedRoute'

export default function ApplicationsPage() {
  return (
    <ProtectedRoute>
      <Applications />
    </ProtectedRoute>
  )
} 