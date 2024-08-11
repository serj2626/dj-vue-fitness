
type UserType = {
    username: string;
    email: string;
    password: string;
};

interface IPost {
    id: string;
    category: string;
}

export type { UserType, IPost }