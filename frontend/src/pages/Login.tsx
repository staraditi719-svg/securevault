import { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const API = 'http://127.0.0.1:8000'

export default function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [role, setRole] = useState('viewer')
  const [isRegister, setIsRegister] = useState(false)
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async () => {
    setMessage('')
    setError('')
    try {
      if (isRegister) {
        await axios.post(`${API}/register`, { username, password, role })
        setMessage('Registered successfully! Please login now.')
        setIsRegister(false)
      } else {
        const res = await axios.post(`${API}/login`, { username, password })
        localStorage.setItem('token', res.data.access_token)
        localStorage.setItem('username', username)
        navigate('/dashboard')
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Something went wrong')
    }
  }

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>🔐 SecureVault</h1>
        <p style={styles.subtitle}>
          {isRegister ? 'Create your account' : 'Sign in to your account'}
        </p>

        <input
          style={styles.input}
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        <input
          style={styles.input}
          placeholder="Password"
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />

        {isRegister && (
          <select
            style={styles.input}
            value={role}
            onChange={e => setRole(e.target.value)}
          >
            <option value="viewer">Viewer</option>
            <option value="editor">Editor</option>
            <option value="admin">Admin</option>
          </select>
        )}

        {message && <p style={styles.success}>{message}</p>}
        {error && <p style={styles.error}>{error}</p>}

        <button style={styles.button} onClick={handleSubmit}>
          {isRegister ? 'Register' : 'Login'}
        </button>

        <p
          style={styles.toggle}
          onClick={() => { setIsRegister(!isRegister); setMessage(''); setError('') }}
        >
          {isRegister ? 'Already have an account? Login' : "Don't have an account? Register"}
        </p>
      </div>
    </div>
  )
}

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#0f172a',
  },
  card: {
    backgroundColor: '#1e293b',
    padding: '40px',
    borderRadius: '16px',
    width: '380px',
    display: 'flex',
    flexDirection: 'column',
    gap: '12px',
    boxShadow: '0 4px 30px rgba(0,0,0,0.4)',
  },
  title: { color: '#f1f5f9', textAlign: 'center', margin: 0 },
  subtitle: { color: '#94a3b8', textAlign: 'center', margin: 0, fontSize: '14px' },
  input: {
    padding: '12px',
    borderRadius: '8px',
    border: '1px solid #334155',
    backgroundColor: '#0f172a',
    color: '#f1f5f9',
    fontSize: '14px',
    outline: 'none',
  },
  button: {
    padding: '12px',
    borderRadius: '8px',
    border: 'none',
    backgroundColor: '#6366f1',
    color: 'white',
    fontSize: '16px',
    cursor: 'pointer',
    fontWeight: 'bold',
  },
  toggle: {
    color: '#6366f1',
    textAlign: 'center',
    cursor: 'pointer',
    fontSize: '13px',
  },
  success: { color: '#4ade80', fontSize: '13px', textAlign: 'center' },
  error: { color: '#f87171', fontSize: '13px', textAlign: 'center' },
}
