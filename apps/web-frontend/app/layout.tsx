import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import '../src/index.css'
import Layout from '../src/components/Layout'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Job Application Automation',
  description: 'AI-powered job application assistance system',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Layout>
          {children}
        </Layout>
      </body>
    </html>
  )
} 