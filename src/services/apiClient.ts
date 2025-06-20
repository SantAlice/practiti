import axios from 'axios';
import { Client, ClientCreateData } from '../types/client';
import { Subscription, SubscriptionCreateData, SubscriptionUpdateData } from '../types/subscription';
import { Booking, BookingCreateData } from '../types/booking';

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
});

export interface GetClientsParams {
  page?: number;
  pageSize?: number;
  search?: string;
  status?: string;
}

// Клиенты
export const getClients = async (params: GetClientsParams = {}): Promise<{ data: Client[]; total: number }> => {
  const { data } = await api.get<{ data: Client[]; total: number }>('/api/clients', { params });
  return data;
};

export const getClientById = async (id: string): Promise<Client> => {
  const { data } = await api.get<Client>(`/api/clients/${id}`);
  return data;
};

export const createClient = async (client: ClientCreateData): Promise<Client> => {
  const { data } = await api.post<Client>('/api/clients', client);
  return data;
};

// Абонементы
export const getSubscriptions = async (): Promise<Subscription[]> => {
  const { data } = await api.get<Subscription[]>('/api/subscriptions');
  return data;
};

export const getSubscriptionsByClientId = async (clientId: string): Promise<Subscription[]> => {
  const { data } = await api.get<Subscription[]>(`/api/clients/${clientId}/subscriptions`);
  return data;
};

export const createSubscription = async (sub: SubscriptionCreateData): Promise<Subscription> => {
  const { data } = await api.post<Subscription>('/api/subscriptions', sub);
  return data;
};

export const updateSubscription = async (id: string, data: SubscriptionUpdateData): Promise<Subscription> => {
  const res = await api.put<Subscription>(`/api/subscriptions/${id}`, data);
  return res.data;
};

export const giftClassToSubscription = async (id: string): Promise<Subscription> => {
  const res = await api.post<Subscription>(`/api/subscriptions/${id}/gift-class`);
  return res.data;
};

export const deleteSubscription = async (id: string): Promise<void> => {
  await api.delete(`/api/subscriptions/${id}`);
};

// Занятия
export const getBookings = async (): Promise<Booking[]> => {
  const { data } = await api.get<Booking[]>('/api/bookings');
  return data;
};

export const createBooking = async (booking: BookingCreateData): Promise<Booking> => {
  const { data } = await api.post<Booking>('/api/bookings', booking);
  return data;
};

export interface DashboardMetrics {
  totalClients: number;
  activeClients: number;
  totalSubscriptions: number;
  activeSubscriptions: number;
  totalBookings: number;
  bookingsThisMonth: number;
}

export const getDashboardMetrics = async (): Promise<DashboardMetrics> => {
  const { data } = await api.get<DashboardMetrics>('/api/dashboard/metrics');
  return data;
}; 