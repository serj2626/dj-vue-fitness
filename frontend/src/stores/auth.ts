import { defineStore } from "pinia";
import { reactive } from "vue";
import axios from "axios";
import type { IAuth, ILogin, IUserRegister } from "@/utils/auth";

export const useUserStore = defineStore("user", () => {
  const user = reactive<IAuth>({
    access: null,
    refresh: null,
    isAuthenticated: false,
    id: null,
    username: null,
    email: null,
  });

  const register = async (userData: IUserRegister) => {
    try {
      const { data } = await axios.post("/api/auth/register/", userData);
      user.id = data.id;
      user.username = data.username;
      user.email = data.email;
      user.isAuthenticated = true;
      user.access = data.token.access;
      user.refresh = data.token.refresh;

      localStorage.setItem("fitness.id", data.id);
      localStorage.setItem("fitness.username", data.username);
      localStorage.setItem("fitness.email", data.email);
      localStorage.setItem("fitness.access", data.token.access);
      localStorage.setItem("fitness.refresh", data.token.refresh);
    } catch (error) {
      throw new Error();
    }
  };

  const login = async (userData: ILogin) => {
    try {
      const { data } = await axios.post("/api/auth/login/", userData);
      user.isAuthenticated = true;
      user.access = data.access;
      user.refresh = data.refresh;
      localStorage.setItem("fitness.access", data.access);
      localStorage.setItem("fitness.refresh", data.refresh);
      axios.defaults.headers.common["Authorization"] = "Bearer " + user.access;
      await setUserInfo();
    } catch (error) {
      throw new Error();
    }
  };

  const removeToken = () => {
    user.refresh = null;
    user.access = null;
    user.isAuthenticated = false;
    user.id = null;
    user.username = null;
    user.email = null;

    localStorage.removeItem("fitness.access");
    localStorage.removeItem("fitness.refresh");
  };

  const refreshToken = async () => {
    try {
      const { data } = await axios.post("/api/auth/refresh/");
      user.access = data.access;
      localStorage.setItem("fitness.access", data.access);
      axios.defaults.headers.common["Authorization"] = "Bearer " + data.access;
    } catch (error) {
      console.log(error);
      removeToken();
    }
  };

  const initStore = () => {
    console.log("initStore", localStorage.getItem("fitness.access"));

    if (localStorage.getItem("fitness.access")) {
      console.log("Вы авторизовались!");

    //   user.access = localStorage.getItem("fitness.access");
    //   user.refresh = localStorage.getItem("fitness.refresh");
      user.id = localStorage.getItem("fitness.id");
      user.username = localStorage.getItem("fitness.username");
      user.email = localStorage.getItem("fitness.email");
      user.isAuthenticated = true;

      // refreshToken();

      // console.log("Initialized user:", user);
    } else {
      ("asd");
    }
  };

  const setUserInfo = async () => {
    try {
      const { data } = await axios.post("/api/auth/me/");
      console.log(data);
    //   user.id = data.id;
    //   user.username = data.username;
    //   user.email = data.email;
    //   user.isAuthenticated = true;
    } catch (error) {
      throw new Error();
    }
  };

  return {
    user,
    register,
    login,
    removeToken,
    initStore,
    setUserInfo,
    refreshToken,
  };
});
