import { createApp } from 'vue'
import { createPinia } from 'pinia'

import axios from 'axios'
import App from './App.vue'
import router from './router'
import globalComponents from "./components/global";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import './assets/main.css'




axios.defaults.baseURL = import.meta.env.VITE_API_URL


const app = createApp(App)
app.use(axios)
    .use(globalComponents)
    .use(Toast)
    .use(createPinia())
    .use(router)
    .mount('#app')
