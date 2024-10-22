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
      path: "/coach-list",
      name: "coachList",
      component: () => import("../views/CoachListView.vue"),
    },
    {
      path: "/coach/:id",
      name: "coach",
      component: () => import("../views/CoachDetailView.vue"),
    },
    {
      path: "/coach/:id/reviews",
      name: "coachReviews",
      component: () => import("../views/CoachReviews.vue"),
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
      path: "/my-abonements/:id/pay",
      name: "payAbonement",
      component: () => import("../views/AbonementPaymentView.vue"),
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
    {
      path: "/my-trainings/:id/pay",
      name: "payTraining",
      component: () => import("../views/TrainingPaymentView.vue"),
    },
    {
      path: "/my-settings/",
      name: "mySettings",
      component: () => import("../views/MySettingsView.vue"),
    },
    {
      path: "/reviews/:id/update",
      name: "reviewUpdate",
      component: () => import("../views/ReviewUpdateView.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "notFound",
      component: () => import("../views/NotFoundView.vue"),
    },
    {
      path: "/other",
      name: "other",
      component: () => import("../views/Other.vue"),
    },
  ],
});

router.beforeEach((to, from, next) => {
  // if (to.path === "/login" || to.path === "/register") {
  //   next();
  // } else {
  //   next("/login");
  console.log("to", to);
  console.log("from", from);
  next();
  // }
});

export default router;
