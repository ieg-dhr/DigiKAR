import { Icon } from "@iconify/vue";
import DefaultTheme from "vitepress/theme-without-fonts";
import button from "./components/button.vue";
import schemaEntry from "./components/schema-entry.vue";

export default {
  extends: DefaultTheme,
  enhanceApp(ctx) {
    ctx.app.component("Button", button);
    ctx.app.component("SchemaEntry", schemaEntry);
    ctx.app.component("icon", Icon);
  },
};
