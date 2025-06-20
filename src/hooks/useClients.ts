import { useQuery } from '@tanstack/react-query';
import { getClients, getClientById, getSubscriptionsByClientId, getDashboardMetrics, DashboardMetrics } from '../services/apiClient';
import { Client } from '../types/client';
import { Subscription } from '../types/subscription';
import { GetClientsParams } from '../services/apiClient';

export interface ClientFilters {
  search?: string;
  status?: string;
}

export const useClients = (page = 1, pageSize = 10, filters: ClientFilters = {}) => {
  return useQuery<{ data: Client[]; total: number }, Error>(
    ['clients', page, pageSize, filters],
    () => getClients({ page, pageSize, ...filters })
  );
};

export const useClientDetail = (id: string) => {
  return useQuery<Client, Error>({
    queryKey: ['client', id],
    queryFn: () => getClientById(id),
    enabled: !!id,
  });
};

export const useClientSubscriptions = (clientId: string) => {
  return useQuery<Subscription[], Error>({
    queryKey: ['subscriptions', clientId],
    queryFn: () => getSubscriptionsByClientId(clientId),
    enabled: !!clientId,
  });
};

export const useDashboardMetrics = () => {
  return useQuery<DashboardMetrics, Error>(['dashboard-metrics'], getDashboardMetrics);
}; 