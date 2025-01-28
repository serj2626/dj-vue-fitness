import { createRouter, createWebHistory } from "vue-router";

import { AppRoutes } from "@/utils/router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: AppRoutes.home,
      component: () => import("../pages/Home.vue"),
    },
    {
      path: "/login",
      name: AppRoutes.login,
      component: () => import("../pages/Login.vue"),
    },
    {
      path: "/register",
      name: AppRoutes.register,
      component: () => import("../pages/Register.vue"),
    },
    {
      path: "/coach-list",
      name: AppRoutes.coachList,
      component: () => import("../pages/CoachList.vue"),
    },
    {
      path: "/coach/:id",
      name: AppRoutes.coach,
      component: () => import("../pages/CoachDetail.vue"),
    },
    {
      path: "/coach/:id/reviews",
      name: AppRoutes.coachReviews,
      component: () => import("../pages/CoachReviews.vue"),
    },
    {
      path: "/posts/:category",
      name: AppRoutes.post,
      component: () => import("../pages/Post.vue"),
    },
    {
      path: "/abonements/",
      name: AppRoutes.abonements,
      component: () => import("../pages/AbonementsLIst.vue"),
    },
    {
      path: "/my-abonements/:id/pay",
      name: AppRoutes.payAbonement,
      component: () => import("../pages/AbonementPayment.vue"),
    },
    {
      path: "/my-abonements/",
      name: AppRoutes.myAbonements,
      component: () => import("../pages/MyAbonements.vue"),
    },
    {
      path: "/my-trainings/",
      name: AppRoutes.myTrainings,
      component: () => import("../pages/MyTrainings.vue"),
    },
    {
      path: "/my-trainings/:id/pay",
      name: AppRoutes.payTraining,
      component: () => import("../pages/TrainingPayment.vue"),
    },
    {
      path: "/my-settings/",
      name: AppRoutes.mySettings,
      component: () => import("../pages/MySettings.vue"),
    },
    {
      path: "/repages/:id/update",
      name: AppRoutes.reviewUpdate,
      component: () => import("../pages/ReviewUpdate.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: AppRoutes.notFound,
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
