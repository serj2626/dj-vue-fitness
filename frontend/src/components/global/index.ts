import ArrowUpButton from "./ArrowUpButton.vue";


const components = [
  { name: "ArrowUpButton", component: ArrowUpButton },
];

export default {
  install(app) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
