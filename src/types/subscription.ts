export type SubscriptionType =
  | 'trial'
  | 'single'
  | 'newbie4'
  | 'regular4'
  | 'regular8'
  | 'regular12'
  | 'unlimited';

export type SubscriptionStatus = 'active' | 'inactive' | 'expired';

export interface Subscription {
  id: string;
  client_id: string;
  type: SubscriptionType;
  total_classes: number;
  used_classes: number;
  remaining_classes: number;
  start_date: string; // ISO date
  end_date: string; // ISO date
  status: SubscriptionStatus;
}

export interface SubscriptionCreateData {
  client_id: string;
  type: SubscriptionType;
}

export interface SubscriptionUpdateData {
  type?: SubscriptionType;
  status?: SubscriptionStatus;
  end_date?: string;
} 