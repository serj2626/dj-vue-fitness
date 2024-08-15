import { createApp } from "vue";
import { createPinia } from "pinia";

import PrimeVue from "primevue/config";
import Aura from "@primevue/themes/aura";



import axios from "axios";
import App from "./App.vue";
import router from "./router";
import globalComponents from "./components/global";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import "./assets/main.css";


axios.defaults.baseURL = import.meta.env.VITE_API_URL;

const app = createApp(App);
app
  .use(axios)
  .use(PrimeVue, {
    theme: {
      preset: Aura,
    },
    ripple: true,
  })
  .use(globalComponents)
  .use(Toast, {
    transition: "Vue-Toastification__fade",
    maxToasts: 20,
    newestOnTop: true,
    position: "top-right",
    timeout: 1500,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: "button",
    icon: true,
    rtl: false,
  })
  .use(createPinia())
  .use(router)
  .mount("#app");
