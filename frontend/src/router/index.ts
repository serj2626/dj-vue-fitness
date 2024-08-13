import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../views/RegisterView.vue"),
    },
    {
      path: "/coach/:id",
      name: "coach",
      component: () => import("../views/CoachDetailView.vue"),
    },
    {
      path: "/posts/:category",
      name: "post",
      component: () => import("../views/PostView.vue"),
    },
    {
      path: "/abonements/",
      name: "abonements",
      component: () => import("../views/AbonementsLIstView.vue"),
    },
    {
      path: "/my-abonements/",
      name: "myAbonements",
      component: () => import("../views/MyAbonementsView.vue"),
    },
    {
      path: "/my-trainings/",
      name: "myTrainings",
      component: () => import("../views/MyTrainingsView.vue"),
    },
  ],
});

// router.beforeEach((to, from, next) => {
//   if (to.path === "/login" || to.path === "/register") {
//     next();
//   } else {
//     next("/login");
//   }
// });

export default router;
