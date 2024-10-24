import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../pages/HomeView.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../pages/LoginView.vue"),
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../pages/RegisterView.vue"),
    },
    {
      path: "/coach-list",
      name: "coachList",
      component: () => import("../pages/CoachListView.vue"),
    },
    {
      path: "/coach/:id",
      name: "coach",
      component: () => import("../pages/CoachDetailView.vue"),
    },
    // {
    //   path: "/coach/:id/repages",
    //   name: "coachRepages",
    //   component: () => import("../pages/CoachRepages.vue"),
    // },
    {
      path: "/posts/:category",
      name: "post",
      component: () => import("../pages/PostView.vue"),
    },
    {
      path: "/abonements/",
      name: "abonements",
      component: () => import("../pages/AbonementsLIstView.vue"),
    },
    {
      path: "/my-abonements/:id/pay",
      name: "payAbonement",
      component: () => import("../pages/AbonementPaymentView.vue"),
    },
    {
      path: "/my-abonements/",
      name: "myAbonements",
      component: () => import("../pages/MyAbonementsView.vue"),
    },
    {
      path: "/my-trainings/",
      name: "myTrainings",
      component: () => import("../pages/MyTrainingsView.vue"),
    },
    {
      path: "/my-trainings/:id/pay",
      name: "payTraining",
      component: () => import("../pages/TrainingPaymentView.vue"),
    },
    {
      path: "/my-settings/",
      name: "mySettings",
      component: () => import("../pages/MySettingsView.vue"),
    },
    {
      path: "/repages/:id/update",
      name: "reviewUpdate",
      component: () => import("../pages/ReviewUpdateView.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "notFound",
      component: () => import("../pages/NotFoundView.vue"),
    },
    {
      path: "/other",
      name: "other",
      component: () => import("../pages/Other.vue"),
    },
  ],
});

// router.beforeEach((to, from, next) => {
//   // if (to.path === "/login" || to.path === "/register") {
//   //   next();
//   // } else {
//   //   next("/login");
//   console.log("to", to);
//   console.log("from", from);
//   next();
//   // }
// });

export default router;
