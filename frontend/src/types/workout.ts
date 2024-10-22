export interface IReviewCreate {
  id: string;
  name: string;
  text: string;
  rating: number;
}

export interface IUser {
  id: string;
  username: string;
  email: string;
}

export interface IReview {
  id: number;
  trainer: string;
  text: string;
  rating: number;
  user: IUser;
  created_at: string;
  date_age?: string;
}

export interface ITrainer {
  id: string | undefined;
  first_name: string;
  last_name: string;
  position: string;
  phone: string;
  email: string;
  bio: string;
  avatar: string;
  trainer_reviews: [];
  count_reviews?: number;
  total_rating?: number;
}

export interface ITrainerList {
  id: number | string;
  avatar: string;
}

export interface iRate {
  id: string;
  title: string;
  count_minutes: number;
  price: number;
  description: string;
}
