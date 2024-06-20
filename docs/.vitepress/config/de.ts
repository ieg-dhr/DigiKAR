import { defineConfig } from "vitepress";

export const de = defineConfig({
  lang: "de-DE",
  themeConfig: {
    nav: [
      { text: "Start", link: "/" },
      { text: "Links", link: "/project-bibliography-and-links" },
      { text: "Mobilität", link: "/mobility-schema" },
      { text: "Rechte und Rechtsinhaber", link: "/rights-holders-saxony" },
      { text: "Visualisierungen", link: "/visualisations/" },
    ],
    sidebar: [
      {
        text: "Projekt",
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
            text: "Links und Bibliographie",
            link: "/project-bibliography-and-links",
          },
          {
            text: "Daten Queries",
            link: "/data-queries",
          },
          {
            text: "Datenmanagement von Zeitangaben",
            link: "/managing-time",
          },
          {
            text: "Datenmanagement von Raum",
            link: "/managing-space",
          },
          {
            text: "Datenvisualisierung",
            link: "/data-visualisation",
          },
          {
            text: "Skripte",
            link: "/scripts",
          },
          {
            text: "Daten Strukturen",
            link: "/data-structure",
          },
          {
            text: "Tools",
            link: "/tools",
          },
          {
            text: "Daten Services",
            link: "/data-services",
          },
        ],
      },
      {
        text: "Mobilität",
        collapsed: true,
        items: [
          { text: "Daten Schema", link: "/mobility-schema" },
          {
            text: "Workflow",
            items: [
              {
                text: "Data Kategorisierung Mainz",
                link: "/data-categorisation-mainz",
              },
              {
                text: "Personen Identifizierung Mainz",
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
        text: "Rechte und Rechtsinhaber",
        link: "rights-holders-saxony",
        collapsed: true,
        items: [
          {
            text: "Workflow",
            items: [{ text: "QGIS to Postgres" }, { text: "Normalization" }],
          },
          {
            text: "Daten Struktur",
            items: [{ text: "Places" }, { text: "Rights and right holders" }],
          },
          {
            text: "Data Zugang",
            items: [{ text: "Postgres" }, { text: "PostgREST" }],
          },
        ],
      },
      {
        text: "Visualisierungen",
        link: "/visualisations/",
        collapsed: true,
        items: [
          {
            text: "Experimenteller Ansatz",
            link: "/visualisations/experimental-approach",
          },
          { text: "Prozesse", link: "/visualisations/process-driven" },
          { text: "Technologie", link: "visualisations/technology" },
        ],
      },
    ],
  },
});
