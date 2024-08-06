interface IAuth {
    access: string | null;
    refresh: string | null;
    isAuthenticated: boolean;
    id: number | null;
    username: string | null;
    email: string | null;
}

interface ILogin {
    username: string;
    password: string;
}

interface IReview {
    id: number | string;
    name: string;
    text: string;
    rating: number;
}

interface ITrainer {
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


export type { IAuth, ILogin, ITrainer, IReview } 