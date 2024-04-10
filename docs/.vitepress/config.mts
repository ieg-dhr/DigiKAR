import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "DigiKAR · Dokumentation",
  lang: "en-US",
  description: "Documentation on data and workflows of the DigiKAR project.",
  locales: {
    root: {
      label: "English",
      lang: "en",
      title: "DigiKAR · Documentation",
    },
    fr: {
      label: "Français",
      lang: "fr",
      title: "DigiKAR · Documentation",
    },
    de: {
      label: "Deutsch",
      lang: "de",
    },
  },
  lastUpdated: true,
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "Examples", link: "/markdown-examples" },
    ],
    sidebar: [
      {
        text: "General",
        items: [
          {
            text: "About the project",
            link: "/project",
          },
          {
            text: "Links",
            link: "/links",
          },
          {
            text: "Data queries",
            link: "/data-queries",
          },
          {
            text: "Managing time",
            link: "/managing-time",
          },
          {
            text: "Managing space",
            link: "/managing-space",
          },
          {
            text: "Visualisations",
            link: "/visualisations",
          },
          {
            text: "Scripts",
            link: "/scripts",
          },
          {
            text: "Data Structure",
            link: "/data-structure",
          },
          {
            text: "Tools",
            link: "/tools",
          },
          {
            text: "Data Services",
            link: "/data-services",
          },
        ],
      },
      {
        text: "Mobility data",
        collapsed: false,
        items: [
          {
            text: "Workflow",
            items: [
              {
                text: "Data Categorisation Mainz",
                link: "/data-categorisation-mainz",
              },
              {
                text: "Person Identification Mainz",
                link: "/persons-mainz",
              },
              { text: "Temporary IDs" },
              { text: "Geocoding" },
              { text: "CSV", link: "/csv-excel" },
            ],
          },
        ],
      },
      {
        text: "Soverein rights data",
        link: "rights-holders-saxony",
        collapsed: true,
        items: [
          {
            text: "Workflow",
            items: [{ text: "QGIS to Postgres" }, { text: "Normalization" }],
          },
          {
            text: "Data structure",
            items: [{ text: "Places" }, { text: "Sovereign Rights" }],
          },
          {
            text: "Data access",
            items: [{ text: "Postgres" }, { text: "PostgREST" }],
          },
        ],
      },
    ],
    outline: {
      level: [2, 3],
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/ieg-dhr/DigiKAR" },
    ],
    search: {
      provider: "local",
    },
  },
});
