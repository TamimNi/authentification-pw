'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const LoginRegister: React.FC = () => {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
  
    const loginData = {
      email: email,
      password: password,
    };
  
    try {
      const response = await fetch('https://localhost:5443/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData),
      });
  
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.token); // Store the token
        toast.success(data.message); // Show success message
        await new Promise(resolve => setTimeout(resolve, 1000));
        router.push('/'); // Redirect to the home page
      } else {
        const errorData = await response.json();
        toast.error(errorData.message); // Show error message
      }
    } catch (error) {
      console.error('Error during login:', error);
      toast.error('An error occurred. Please try again later.');
    }
  };
  

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (email && password) {
      const registerData = {
        email: email,
        password: password,
      };
  
      try {
        const response = await fetch('https://localhost:5443/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(registerData),
        });
  
        const data = await response.json();
        
        if (response.ok) {
          toast.success(data.message); // Show success message
        } else {
          toast.error(data.message); // Show error message
        }
      } catch (error) {
        console.error('Error during registration:', error);
        toast.error('An error occurred. Please try again later.');
      }
    } else {
      toast.error('Please fill in all fields');
    }
  };
  

  return (
    <main className="flex flex-col items-center justify-center h-screen  p-4">
    <div className="bg-gray-500 bg-opacity-90 p-5 border border-blue-400 rounded -mt-32">
      <h1 className="text-3xl text-white font-bold mb-6">
        {isRegistering ? 'Register' : 'Login'}
      </h1>
      <form onSubmit={isRegistering ? handleRegister : handleLogin} className="w-full max-w-md">
        <div className="mb-4">
          <label className="block text-gray-300">Email</label>
          <input
            type="email"
            className="w-full px-4 py-3 border border-gray-400 rounded bg-gray-800 text-white"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-300">Password</label>
          <input
            type="password"
            className="w-full px-4 py-3 border border-gray-400 rounded bg-gray-800 text-white"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {isRegistering ? 'Register' : 'Login'}
        </button>
      </form>
      <div className="mt-4">
        <button
          className="text-blue-400 underline"
          onClick={() => setIsRegistering(!isRegistering)}
        >
          {isRegistering
            ? 'Already have an account? Login here'
            : "Don't have an account? Register here"}
        </button>
      </div>
      </div>
      {/* Add ToastContainer to render the toast notifications */}
      <ToastContainer />
    </main>
  );
};

export default LoginRegister;
