'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

const Secrets: React.FC = () => {
  const [secret, setSecret] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    const fetchSecret = async () => {
      try {
        const token = localStorage.getItem('token'); // Get token from localStorage

        const response = await fetch('https://localhost:6443/secret', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ token }), // Send token in the request body
        });

        if (response.ok) {
          const data = await response.json();

          // Check if a new token is provided in the response
          if (data.token) {
            localStorage.setItem('token', data.token); // Set the new token in localStorage
          }

          setSecret(data.secret); // Assuming the response contains a "secret" field
          setError(null); // Clear any previous errors
        } else {
          setError('Unauthorized');
          setSecret(null); // Clear any previous secret
        }
      } catch (error) {
        console.error('Error fetching secret:', error);
        setError('An error occurred. Please try again later.');
        setSecret(null); // Clear any previous secret
      }
    };

    fetchSecret();
  }, []);

  return (
    <div className="flex items-center justify-center h-screen ">   
      <div className="bg-black bg-opacity-80 p-5 border border-red-400 rounded -mt-40"> 
        {secret ? (
          <h1 className="text-4xl text-white">{secret}</h1>
        ) : (
          <h1 className="text-4xl text-red-500">{error || 'Loading...'}</h1>
        )}
      </div>
    </div>
  );
};

export default Secrets;
