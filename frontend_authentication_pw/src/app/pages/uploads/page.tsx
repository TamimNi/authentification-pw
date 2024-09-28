'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

const Uploads: React.FC = () => {
  const router = useRouter();
  const [file, setFile] = useState<File | null>(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/');
    }
  }, [router]);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = () => {
    if (!file) {
      alert('Please select a file first.');
      return;
    }

    // Replace with real upload logic
    alert(`Uploading ${file.name}...`);
  };

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">Upload File</h1>
      <input type="file" onChange={handleFileChange} className="mb-4" />
      <button
        onClick={handleUpload}
        className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        Upload
      </button>
    </main>
  );
};

export default Uploads;