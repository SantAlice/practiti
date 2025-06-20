import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/layout/Layout';
import Home from './pages/Home';
import Clients from './pages/Clients';
import Bookings from './pages/Bookings';
import Profile from './pages/Profile';

const App: React.FC = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="clients" element={<Clients />} />
        <Route path="bookings" element={<Bookings />} />
        <Route path="profile" element={<Profile />} />
      </Route>
    </Routes>
  </BrowserRouter>
);

export default App; 