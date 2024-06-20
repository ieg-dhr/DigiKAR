import { defineConfig } from "vitepress";

export const en = defineConfig({
  lang: "en-US",
  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      { text: "Links", link: "/project-bibliography-and-links" },
      { text: "Mobility", link: "/mobility-schema" },
      { text: "Rights and right holders", link: "/rights-holders-saxony" },
      { text: "Visualisations", link: "/visualisations/" },
    ],
    sidebar: [
      {
        text: "Project",
        link: "/project/",
        collapsed: true,
        items: [
          // add pages from current website here
        ],
      },
      {
        text: "General",
        items: [
          {
            text: "Links and bilbiography",
            link: "/project-bibliography-and-links",
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
        collapsed: true,
        items: [
          { text: "Data Schema", link: "/mobility-schema" },
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
              { text: "JSON", link: "/json" },
              { text: "TXT", link: "/txt" },
              { text: "XML", link: "/xml" },
            ],
          },
        ],
      },
      {
        text: "Rights and right holders data",
        link: "rights-holders-saxony",
        collapsed: true,
        items: [
          {
            text: "Workflow",
            items: [{ text: "QGIS to Postgres" }, { text: "Normalization" }],
          },
          {
            text: "Data structure",
            items: [{ text: "Places" }, { text: "Rights and right holders" }],
          },
          {
            text: "Data access",
            items: [{ text: "Postgres" }, { text: "PostgREST" }],
          },
        ],
      },
      {
        text: "Visualisations",
        link: "/visualisations/",
        collapsed: true,
        items: [
          {
            text: "Experimental approach",
            link: "/visualisations/experimental-approach",
          },
          { text: "Processes", link: "/visualisations/process-driven" },
          { text: "Technology", link: "visualisations/technology" },
        ],
      },
    ],
  },
});
