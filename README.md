<div style="display:flex;justify-content:center;padding-bottom:3em;">
  <img src="./DigiKAR_logo-small.png" alt="DigiKAR" width="100"/>
</div>

# DigiKAR

Scripts for managing spatial and biographic data in the DigiKAR project

**DE**: Skripte zur Bearbeitung von Ortsdaten und biographischen Angaben im DigiKAR Projekt

**FR**: Scripts pour la gestion des données spatiales et biographiques dans le projet DigiKAR

## Documentation

This repository also contains `VitePress` [docs](https://ieg-dhr.github.io/DigiKAR/).

### How to contribute content to the docs

New content can be added to the docs by creating a new markdown file in the `docs` directory.
Note that the name of the markdown files should use kebab-case and should not contain any special characters (including spaces).
Every markdown file will be compiled into a page in the docs.

However, if you want to add the section to the sidebar or the main navigation bar, you need to update the files `docs/.vitepress/config/<locale>.ts` accordingly. Where locale is currently one of the following: `en`, `de`, `fr`.

> [!WARNING]
> The automatic redirection to the current language is currently not working.

### How to develop the docs locally

Follow these steps to develop the docs locally:

- Firstly, install the dependencies by running:

  ```bash
  pnpm install
  ```

- After that you can start a `VitePress` dev server locally by running:

  ```bash
  pnpm docs:dev
  ```
