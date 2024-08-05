import { defineStore } from "pinia";
import { reactive } from "vue";
import axios from "axios";


type TokenType = {
  access: string;
  refresh: string;
};

interface IAuth {
  access: string | null;
  refresh: string | null;
  isAuthenticated: boolean;
  id: string | null;
  username: string | null;
  email: string | null;
}

interface IUserRegister {
  id: string | null;
  username: string | null;
  email: string | null;
  token: TokenType;
}



export const useUserStore = defineStore("user", () => {
  const user: IAuth = reactive({
    isAuthenticated: false,
    id: null,
    username: null,
    email: null,
    access: null,
    refresh: null,
  });


  function initStore() {
    console.log("initStore", localStorage.getItem("user.access"));

    if (localStorage.getItem("user.access")) {
      console.log("User has access!");

      user.access = localStorage.getItem("user.access");
      user.refresh = localStorage.getItem("user.refresh");
      user.id = localStorage.getItem("user.id");
      user.username = localStorage.getItem("user.name");
      user.email = localStorage.getItem("user.email");
      user.isAuthenticated = true;

      refreshToken();

      console.log("Initialized user:", user);
    }
  }


  const auth = async (type: string, data: object) => {
    const url: string = (type === "login") ? "/api/auth/login/" : "/api/auth/register/";
    try {
      const res = await axios.post(url, data);
      setToken(res.data);
    } catch (error) {
      console.log(error);
    }
  }


  // {
  //   "username": "serj2626",
  //   "email": "serj2656@mail.ru",
  //   "token": {
  //     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODQzMDQ5NSwiaWF0IjoxNzIyODc4NDk1LCJqdGkiOiI5MzExNTNjOWMxYWU0ZTIxOTUzMTU5MzU0YjNiNzc4OCIsInVzZXJfaWQiOjV9.OCWObH_zCZjVbuHmG0otvrbPQOz_Ggh0mn5qXrjNpGU",
  //     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDcwNDk1LCJpYXQiOjE3MjI4Nzg0OTUsImp0aSI6IjVmMzhmZDgwZmUyMTRlNGNhZTIxMzJiNmJiZWYzOTNmIiwidXNlcl9pZCI6NX0.gQJflI6LGoqkVWXNliBy2lfozkxeIcuWtdGredcUTxU"
  //   }
  // }


  // {
  //   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODQzMDYxMCwiaWF0IjoxNzIyODc4NjEwLCJqdGkiOiJjOTRhNWQwM2JmYzE0MGExOTAzYWI5N2Q5Nzg0NDEzYSIsInVzZXJfaWQiOjV9.xun0J82tU8TcepIMXf6kA3aZKGeNF0cU4Ob_t3-xb6M",
  //   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDcwNjEwLCJpYXQiOjE3MjI4Nzg2MTAsImp0aSI6ImY2ZmNlYWFmYTI0ZjRmN2RhNWVlNjc5ZGVmMWViNWJhIiwidXNlcl9pZCI6NX0.t6Sz6ZQiYr31uu0C_zsV1J4yYHbW80ZhnF6e0YL_52o"
  // }

  function setToken(data: TokenType) {
    console.log("setToken", data);

    user.access = data.access;
    user.refresh = data.refresh;
    user.isAuthenticated = true;

    localStorage.setItem("user-fitness", JSON.stringify(data));
  }

  function removeToken() {
    console.log("removeToken");

    user.refresh = null;
    user.access = null;
    user.isAuthenticated = false;
    user.id = null;
    user.username = null;
    user.email = null;

    localStorage.setItem("user-fitness", "");
  }

  function setUserInfo(data: IUserRegister) {
    console.log("setUserInfo", data);

    user.id = data.id;
    user.username = data.username;
    user.email = data.email;
    user.isAuthenticated = true;
    user.access = data.token.access;
    user.refresh = data.token.refresh;

    localStorage.setItem("user-fitness", JSON.stringify(data));


    console.log("User", user);
  }

  // const refresh = async () => {
  //   try {
  //     const res = await axios.post("/api/refresh/");
  //     user.access = res.data.access;
  //     localStorage.setItem("user.access", res.data.access);
  //     axios.defaults.headers.common["Authorization"] =
  //       "Bearer " + res.data.access;
  //   } catch (error) {
  //     console.log(error);
  //     removeToken();
  //   }
  // };

  function refreshToken() {
    axios
      .post("/api/auth/refresh/", {
        refresh: user.refresh,
      })
      .then((response) => {
        user.access = response.data.access;

        localStorage.setItem("user.access", response.data.access);

        axios.defaults.headers.common["Authorization"] =
          "Bearer " + response.data.access;
      })
      .catch((error) => {
        console.log(error);

        removeToken();
      });
  }

  return { user, initStore, setToken, removeToken, setUserInfo, refreshToken, auth };
});