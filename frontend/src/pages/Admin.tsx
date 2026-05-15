import { useEffect, useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

 const API = 'https://securevault-aditi.duckdns.org'

export default function Admin() {
  const [data, setData] = useState<any>(null)
  const [error, setError] = useState('')
  const navigate = useNavigate()
  const token = localStorage.getItem('token')

  useEffect(() => {
    axios.get(`${API}/admin`, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(res => setData(res.data))
      .catch(() => setError('Access denied or session expired.'))
  }, [])

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.header}>
          <h2 style={styles.title}>⚙️ Admin Panel</h2>
          <button style={styles.back} onClick={() => navigate('/dashboard')}>
            ← Back
          </button>
        </div>

        {error && <p style={styles.error}>{error}</p>}

        {data && (
          <>
            <p style={styles.message}>{data.message}</p>
            <div style={styles.accessBadge}>Access: {data.access}</div>

            <h3 style={styles.sectionTitle}>Admin Controls</h3>
            <div style={styles.controls}>
              <div style={styles.control}>👥 Manage Users</div>
              <div style={styles.control}>📊 View Analytics</div>
              <div style={styles.control}>⚙️ System Settings</div>
              <div style={styles.control}>🔒 Security Logs</div>
            </div>
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
  back: {
    padding: '8px 16px',
    borderRadius: '8px',
    border: 'none',
    backgroundColor: '#334155',
    color: 'white',
    cursor: 'pointer',
  },
  message: { color: '#94a3b8' },
  accessBadge: {
    display: 'inline-block',
    padding: '4px 16px',
    borderRadius: '999px',
    backgroundColor: '#4ade80',
    color: '#0f172a',
    fontWeight: 'bold',
    fontSize: '13px',
  },
  sectionTitle: { color: '#f1f5f9', marginTop: '24px' },
  controls: { display: 'flex', flexDirection: 'column', gap: '10px' },
  control: {
    padding: '14px',
    backgroundColor: '#0f172a',
    borderRadius: '8px',
    color: '#94a3b8',
    fontSize: '14px',
    cursor: 'pointer',
  },
  error: { color: '#f87171' },
}