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
  base: "/DigiKAR/",
  lastUpdated: true,
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "Links", link: "/links" },
      { text: "Mobility", link: "/mobility" },
      { text: "Sovereign rights", link: "/rights-holders-saxony" },
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
            text: "Data visualisation",
            link: "/data-visualisation",
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
      {
        text: "Visualisation principles",
        link: "/visualisations/",
        collapsed: true,
        items: [
          {
            text: "Experimental development",
            link: "/visualisations/experimental-approach",
          },
          { text: "Processes", link: "/visualisations/process-driven" },
          { text: "Technology", link: "visualisations/technology" },
        ],
      },
    ],
    outline: {
      level: [2, 3],
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/ieg-dhr/DigiKAR" },
      { icon: "x", link: "https://twitter.com/digi_KAR" },
      {
        icon: {
          svg: `
            <svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 10 10">
                <path fill="currentColor" d="M5,0C2.24,0,0,2.24,0,5s2.24,5,5,5,5-2.24,5-5S7.76,0,5,0ZM5.25,2.25v-1.22c.13,0,.26.02.39.04.26.25.49.67.68,1.19h-1.06ZM6.47,2.75c.15.57.25,1.24.27,2h-1.49v-2h1.22ZM4.75,1.03v1.22h-1.06c.19-.52.42-.93.68-1.19.13-.02.26-.03.39-.04ZM4.75,2.75v2h-1.49c.02-.76.12-1.43.27-2h1.22ZM2.76,4.75h-1.74c.05-.74.28-1.42.67-2h1.33c-.15.6-.24,1.27-.26,2ZM1.03,5.25h1.74c.02.73.11,1.4.26,2h-1.33c-.39-.58-.62-1.26-.67-2ZM3.26,5.25h1.49v2h-1.22c-.15-.57-.25-1.24-.27-2ZM4.75,7.75v1.22c-.13,0-.26-.02-.39-.04-.26-.25-.49-.67-.68-1.19h1.06ZM5.25,8.97v-1.22h1.06c-.19.52-.42.93-.68,1.19-.13.02-.26.03-.39.04ZM5.25,7.25v-2h1.49c-.02.76-.12,1.43-.27,2h-1.22ZM7.24,5.25h1.74c-.05.74-.28,1.42-.67,2h-1.33c.15-.6.24-1.27.26-2ZM7.24,4.75c-.02-.73-.11-1.4-.26-2h1.33c.39.58.62,1.26.67,2h-1.74ZM7.89,2.25h-1.05c-.13-.38-.28-.7-.45-.99.57.21,1.09.55,1.5.99ZM3.61,1.26c-.17.28-.33.61-.45.99h-1.05c.42-.44.93-.77,1.5-.99ZM2.11,7.75h1.05c.13.38.28.7.45.99-.57-.21-1.09-.55-1.5-.99ZM6.39,8.74c.17-.28.33-.61.45-.99h1.05c-.42.44-.93.77-1.5.99Z"/>
            </svg>
          `,
        },
        link: "https://digikar.eu/",
      },
    ],
    search: {
      provider: "local",
    },
  },
});
