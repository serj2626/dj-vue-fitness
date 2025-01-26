import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../pages/Home.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../pages/Login.vue"),
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../pages/Register.vue"),
    },
    {
      path: "/coach-list",
      name: "coachList",
      component: () => import("../pages/CoachList.vue"),
    },
    {
      path: "/coach/:id",
      name: "coach",
      component: () => import("../pages/CoachDetail.vue"),
    },
    {
      path: "/coach/:id/reviews",
      name: "coachReviews",
      component: () => import("../pages/CoachReviews.vue"),
    },
    {
      path: "/posts/:category",
      name: "post",
      component: () => import("../pages/Post.vue"),
    },
    {
      path: "/abonements/",
      name: "abonements",
      component: () => import("../pages/AbonementsLIst.vue"),
    },
    {
      path: "/my-abonements/:id/pay",
      name: "payAbonement",
      component: () => import("../pages/AbonementPayment.vue"),
    },
    {
      path: "/my-abonements/",
      name: "myAbonements",
      component: () => import("../pages/MyAbonements.vue"),
    },
    {
      path: "/my-trainings/",
      name: "myTrainings",
      component: () => import("../pages/MyTrainings.vue"),
    },
    {
      path: "/my-trainings/:id/pay",
      name: "payTraining",
      component: () => import("../pages/TrainingPayment.vue"),
    },
    {
      path: "/my-settings/",
      name: "mySettings",
      component: () => import("../pages/MySettings.vue"),
    },
    {
      path: "/repages/:id/update",
      name: "reviewUpdate",
      component: () => import("../pages/ReviewUpdate.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "notFound",
      component: () => import("../pages/NotFound.vue"),
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
