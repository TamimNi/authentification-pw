import fs from 'fs';
import path from 'path';

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Any other Next.js config options go here

  // Custom Webpack Dev Middleware to configure HTTPS
  webpackDevMiddleware: (config) => {
    return config;
  },
};

export default nextConfig;
