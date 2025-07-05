export interface User {
  id: string;
  email: string;
  first_name?: string;
  last_name?: string;
  phone?: string;
  is_active: boolean;
  email_verified: boolean;
  subscription_tier: string;
  last_login_at?: string;
  created_at: string;
  updated_at: string;
}

export interface UserProfile {
  id: string;
  user_id: string;
  resume_file_url?: string;
  resume_text?: string;
  linkedin_url?: string;
  github_url?: string;
  portfolio_url?: string;
  phone?: string;
  location_city?: string;
  location_state?: string;
  location_country?: string;
  willing_to_relocate: boolean;
  years_experience?: number;
  current_title?: string;
  target_salary_min?: number;
  target_salary_max?: number;
  preferred_work_type?: string;
  created_at: string;
  updated_at: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  password: string;
  first_name?: string;
  last_name?: string;
  phone?: string;
  is_active?: boolean;
  email_verified?: boolean;
  subscription_tier?: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface AuthError {
  detail: string;
  status_code?: number;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
}

export interface AuthActions {
  login: (email: string, password: string) => Promise<void>;
  register: (userData: RegisterRequest) => Promise<void>;
  logout: () => void;
  setUser: (user: User) => void;
  clearError: () => void;
  checkAuth: () => Promise<void>;
} 