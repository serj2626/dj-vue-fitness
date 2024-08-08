import ArrowUpButton from "./ArrowUpButton.vue";
import ProfileButton from "./ProfileButton.vue";

const components = [
  { name: "ArrowUpButton", component: ArrowUpButton },
  { name: "ProfileButton", component: ProfileButton },
];

export default {
  install(app) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
