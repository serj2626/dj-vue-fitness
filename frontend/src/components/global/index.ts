import Alert from "./Alert.vue";
import type { App } from "vue";
import ArrowUpButton from "./ArrowUpButton.vue";
import AuthCard from "./AuthCard.vue";
import DeleteModal from "./DeleteModal.vue";
import UButton from "./UButton.vue";
import UModal from "./UModal.vue";
import URating from "./URating.vue";

const components = [
  { name: "ArrowUpButton", component: ArrowUpButton },
  { name: "URating", component: URating },
  { name: "UButton", component: UButton },
  { name: "AuthCard", component: AuthCard },
  { name: "UModal", component: UModal },
  { name: "DeleteModal", component: DeleteModal },
  { name: "Alert", component: Alert },
];

export default {
  install(app: App) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
