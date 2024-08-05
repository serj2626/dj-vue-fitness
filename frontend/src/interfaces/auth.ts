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

export { IAuth, ILogin };
