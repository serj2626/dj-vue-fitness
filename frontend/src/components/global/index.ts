import Alert from "./Alert.vue";
import type { App } from "vue";
import ArrowUpButton from "./ArrowUpButton.vue";
import AuthCard from "./AuthCard.vue";
import Confirm from "./Confirm.vue";
import Icon from "./Icon.vue";
import UButton from "./UButton.vue";
import UModal from "./UModal.vue";
import URating from "./URating.vue";

const components = [
  { name: "ArrowUpButton", component: ArrowUpButton },
  { name: "URating", component: URating },
  { name: "UButton", component: UButton },
  { name: "AuthCard", component: AuthCard },
  { name: "UModal", component: UModal },
  { name: "Confirm", component: Confirm },
  { name: "Alert", component: Alert },
  { name: "Icon", component: Icon },
];

export default {
  install(app: App) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
