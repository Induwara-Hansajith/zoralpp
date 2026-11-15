import './Login.css';

function Login() {
  return (
    <main className="login-container">
      <section className="login-card">
        <div className="login-logo">
          <h1>Sync-space</h1>
          <p>Your workspace, powered by Sync-space dev team.</p>
        </div>

        <div className="login-heading">
          <h2>Welcome Back!</h2>
          <p>Please enter your details to sign in.</p>
        </div>

        <form className="login-form" onSubmit={(e) => e.preventDefault()}>
          <label htmlFor="email">Email Address</label>
          <input id="email" type="email"
            placeholder="Enter your email" required />

          <label htmlFor="password">Password</label>
          <input id="password" type="password"
            placeholder="Enter your password" required />

          <div className="login-options">
            <label className="remember">
              <input type="checkbox" /> Remember me
            </label>
            <a href="#">Forgot password?</a>
          </div>

          <button type="submit">Sign In</button>
        </form>

        <p className="signup-text">
          Don't have an account? <a href="#">Sign up</a>
        </p>
      </section>
    </main>
  );
}

export default Login;
