export interface IReviewCreate {
  id: string;
  name: string;
  text: string;
  rating: number;
}

export interface IReview {
  id: number;
  trainer: string;
  text: string;
  rating: number;
  user: string;
  created_at: string;
}

export interface ITrainer {
  id: string | null;
  first_name: string;
  last_name: string;
  position: string;
  phone: string;
  email: string;
  bio: string;
  avatar: string;
  trainer_reviews: [];
}

export interface ITrainerList {
  id: number | string;
  avatar: string;
}

export interface iRate {
  id: string,
  title: string,
  count_minutes: number,
  price: number,
  description: string
}