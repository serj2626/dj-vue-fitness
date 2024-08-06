export interface IToken {
    access: string;
    refresh: string;
  }
  
  export interface IAuth {
    access: string | null;
    refresh: string | null;
    isAuthenticated: boolean;
    id: string | null;
    username: string | null;
    email: string | null;
  }
  
  export interface IUserRegister {
    username: string
    email: string
    password: string
  }

  export interface IUserRegisterData {
    id: string;
    username: string;
    email: string;
    token: IToken
  }
  
  export interface ILogin {
    username: string;
    password: string;
  }
  