import Profile from '../../src/pages/Profile'
import ProtectedRoute from '../../src/components/auth/ProtectedRoute'

export default function ProfilePage() {
  return (
    <ProtectedRoute>
      <Profile />
    </ProtectedRoute>
  )
} 