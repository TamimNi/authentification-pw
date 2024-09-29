'use client';

import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { useState, useEffect } from 'react';

const Navbar: React.FC = () => {
  const pathname = usePathname();
  const router = useRouter();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Check if the token is in localStorage on component mount
  useEffect(() => {
    const token = localStorage.getItem('token');
    setIsLoggedIn(!!token); // Set login state based on token presence
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token'); // Clear token on logout
    setIsLoggedIn(false); // Update state
    router.push('/'); // Redirect to home page
  };

  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Secret', path: '/pages/secret' },
  ];

  return (
    <nav className="bg-blue-600 p-4">
      <ul className="flex space-x-4">
        {navLinks.map((link) => (
          <li key={link.name}>
            <Link href={link.path}>
              <span
                className={`text-white cursor-pointer ${
                  pathname === link.path
                    ? 'underline font-bold'
                    : 'hover:underline'
                }`}
              >
                {link.name}
              </span>
            </Link>
          </li>
        ))}

        {!isLoggedIn ? (
          <li>
            <Link href="/pages/login">
              <span
                className={`text-white cursor-pointer ${
                  pathname === '/login'
                    ? 'underline font-bold'
                    : 'hover:underline'
                }`}
              >
                Login
              </span>
            </Link>
          </li>
        ) : (
          <li>
            <button
              onClick={handleLogout}
              className="text-white hover:underline focus:outline-none"
            >
              Logout
            </button>
          </li>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
