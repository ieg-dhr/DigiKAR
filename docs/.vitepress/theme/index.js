import DefaultTheme from "vitepress/theme-without-fonts";
import button from "./components/button.vue";

export default {
  extends: DefaultTheme,
  enhanceApp(ctx) {
    ctx.app.component("Button", button);
  },
};
