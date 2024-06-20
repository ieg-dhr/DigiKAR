import { defineConfig } from "vitepress";

export const fr = defineConfig({
  lang: "fr-FR",
  themeConfig: {
    nav: [
      { text: "Accueil", link: "/" },
      { text: "Liens", link: "/project-bibliography-and-links" },
      { text: "Mobilité", link: "/mobility-schema" },
      {
        text: "Droits et détenteurs de droits",
        link: "/rights-holders-saxony",
      },
      { text: "Visualisations", link: "/visualisations/" },
    ],
    sidebar: [
      {
        text: "Projet",
        link: "/project/",
        collapsed: true,
        items: [
          // add pages from current website here
        ],
      },
      {
        text: "Général",
        items: [
          {
            text: "Liens et bibliographie",
            link: "/project-bibliography-and-links",
          },
          {
            text: "Requêtes de données",
            link: "/data-queries",
          },
          {
            text: "Gestion des données de temps",
            link: "/managing-time",
          },
          {
            text: "Gestion des données de temps",
            link: "/managing-space",
          },
          {
            text: "Visualisation de données",
            link: "/data-visualisation",
          },
          {
            text: "Scripts",
            link: "/scripts",
          },
          {
            text: "Structures de données",
            link: "/data-structure",
          },
          {
            text: "Outils",
            link: "/tools",
          },
          {
            text: "Services de données",
            link: "/data-services",
          },
        ],
      },
      {
        text: "Mobilité",
        collapsed: true,
        items: [
          { text: "Schéma de données", link: "/mobility-schema" },
          {
            text: "Workflow",
            items: [
              {
                text: "Catégorisation des données Mainz",
                link: "/data-categorisation-mainz",
              },
              {
                text: "Identification des personnes Mainz",
                link: "/persons-mainz",
              },
              { text: "IDs temporaires" },
              { text: "Géocodage" },
              { text: "CSV", link: "/csv-excel" },
              { text: "JSON", link: "/json" },
              { text: "TXT", link: "/txt" },
              { text: "XML", link: "/xml" },
            ],
          },
        ],
      },
      {
        text: "Droits et détenteurs de droits",
        link: "rights-holders-saxony",
        collapsed: true,
        items: [
          {
            text: "Flux de travail",
            items: [{ text: "QGIS à Postgres" }, { text: "Normalisation" }],
          },
          {
            text: "Structure de données",
            items: [
              { text: "Lieux" },
              { text: "Droits et détenteurs de droits" },
            ],
          },
          {
            text: "Accès aux données",
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
            text: "Approche expérimentale",
            link: "/visualisations/experimental-approach",
          },
          { text: "Processus", link: "/visualisations/process-driven" },
          { text: "Technologie", link: "visualisations/technology" },
        ],
      },
    ],
  },
});
