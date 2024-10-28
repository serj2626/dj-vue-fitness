
type UserType = {
    username: string;
    email: string;
    password: string;
};

interface IPost {
    id: string;
    category: string;
}

interface IFormReview {
    message: string;
    rating: number | null;
  }
  

export type { UserType, IPost, IFormReview };