import { OhVueIcon, addIcons } from "oh-vue-icons";
import { OiNumber, OiQuestion, OiTypography } from "oh-vue-icons/icons";
import DefaultTheme from "vitepress/theme-without-fonts";
import button from "./components/button.vue";
import schemaEntry from "./components/schema-entry.vue";

addIcons(OiNumber, OiTypography, OiQuestion);

export default {
  extends: DefaultTheme,
  enhanceApp(ctx) {
    ctx.app.component("Button", button);
    ctx.app.component("SchemaEntry", schemaEntry);
    ctx.app.component("v-icon", OhVueIcon);
  },
};
