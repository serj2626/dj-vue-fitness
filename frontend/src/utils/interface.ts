export interface IAuth {
    access: string | null;
    refresh: string | null;
    isAuthenticated: boolean;
    id: number | null;
    username: string | null;
    email: string | null;
}

export interface ILogin {
    username: string;
    password: string;
}

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
    user : string;
    created_at: string;
}

export interface ITrainer {
    id: number | string;
    first_name: string;
    last_name: string;
    position: string;
    phone: string;
    email: string;
    bio: string;
    avatar: string;
    trainer_reviews: [];
}

export interface IAbonement {
    id: number;
    title: string;
    description: string;
    price: number;
    number_of_months: number;
}

