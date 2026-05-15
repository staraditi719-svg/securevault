import { useEffect, useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const API = 'https://securevault-qci0.onrender.com'

export default function Dashboard() {
  const [data, setData] = useState<any>(null)
  const [error, setError] = useState('')
  const navigate = useNavigate()
  const token = localStorage.getItem('token')

  useEffect(() => {
    axios.get(`${API}/dashboard`, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(res => setData(res.data))
      .catch(() => setError('Session expired. Please login again.'))
  }, [])

  const logout = () => {
    localStorage.clear()
    navigate('/login')
  }

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.header}>
          <h2 style={styles.title}>🔐 SecureVault</h2>
          <button style={styles.logout} onClick={logout}>Logout</button>
        </div>

        {error && <p style={styles.error}>{error}</p>}

        {data && (
          <>
            <p style={styles.welcome}>{data.message}</p>
            <div style={styles.roleBadge}>{data.role.toUpperCase()}</div>

            <h3 style={styles.sectionTitle}>Your Resources</h3>
            <div style={styles.resources}>
              {data.resources.map((r: string) => (
                <div key={r} style={styles.resource}>
                  📁 {r}
                </div>
              ))}
            </div>

            {data.role === 'admin' && (
              <button
                style={styles.adminBtn}
                onClick={() => navigate('/admin')}
              >
                Go to Admin Panel
              </button>
            )}
          </>
        )}
      </div>
    </div>
  )
}

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    minHeight: '100vh',
    backgroundColor: '#0f172a',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  card: {
    backgroundColor: '#1e293b',
    padding: '40px',
    borderRadius: '16px',
    width: '480px',
    boxShadow: '0 4px 30px rgba(0,0,0,0.4)',
  },
  header: { display: 'flex', justifyContent: 'space-between', alignItems: 'center' },
  title: { color: '#f1f5f9', margin: 0 },
  logout: {
    padding: '8px 16px',
    borderRadius: '8px',
    border: 'none',
    backgroundColor: '#ef4444',
    color: 'white',
    cursor: 'pointer',
  },
  welcome: { color: '#94a3b8', fontSize: '16px' },
  roleBadge: {
    display: 'inline-block',
    padding: '4px 16px',
    borderRadius: '999px',
    backgroundColor: '#6366f1',
    color: 'white',
    fontWeight: 'bold',
    fontSize: '13px',
  },
  sectionTitle: { color: '#f1f5f9', marginTop: '24px' },
  resources: { display: 'flex', flexDirection: 'column', gap: '10px' },
  resource: {
    padding: '12px',
    backgroundColor: '#0f172a',
    borderRadius: '8px',
    color: '#94a3b8',
    fontSize: '14px',
  },
  adminBtn: {
    marginTop: '20px',
    padding: '12px',
    width: '100%',
    borderRadius: '8px',
    border: 'none',
    backgroundColor: '#6366f1',
    color: 'white',
    cursor: 'pointer',
    fontWeight: 'bold',
  },
  error: { color: '#f87171' },
}