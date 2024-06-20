import { defineConfig } from "vitepress";
import { shared } from "./shared";
import { en } from "./en";
import { de } from "./de";
import { fr } from "./fr";

export default defineConfig({
  ...shared,
  locales: {
    root: { label: "English", ...en },
    de: { label: "Deutsch", ...de },
    fr: { label: "Français", ...fr },
  },
});
