'use client';

import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { useState, useEffect } from 'react';

const Navbar: React.FC = () => {
  const pathname = usePathname();
  const router = useRouter();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Dummy authentication check
  useEffect(() => {
    // Replace this with real authentication logic
    const token = localStorage.getItem('token');
    setIsLoggedIn(!!token);
  }, []);

  const handleLogout = () => {
    // Replace this with real logout logic
    localStorage.removeItem('token');
    setIsLoggedIn(false);
    router.push('/');
  };

  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Uploads', path: '/pages/uploads' },
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