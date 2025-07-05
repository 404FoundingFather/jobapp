import Jobs from '../../src/pages/Jobs'
import ProtectedRoute from '../../src/components/auth/ProtectedRoute'

export default function JobsPage() {
  return (
    <ProtectedRoute>
      <Jobs />
    </ProtectedRoute>
  )
} 