import { Icon } from "@iconify/vue";
import DefaultTheme from "vitepress/theme-without-fonts";
import button from "./components/button.vue";
import schemaEntry from "./components/schema-entry.vue";
import Layout from "./Layout.vue";

export default {
  extends: DefaultTheme,
  Layout: Layout,
  enhanceApp(ctx) {
    ctx.app.component("Button", button);
    ctx.app.component("SchemaEntry", schemaEntry);
    ctx.app.component("icon", Icon);
  },
};
