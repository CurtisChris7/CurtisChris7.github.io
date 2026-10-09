# Christopher Curtis — personal research website

Live at **https://CurtisChris7.github.io/**

A minimal academic site laid out after the
[al-folio](https://github.com/alshedivat/al-folio) theme, built with
[Jekyll](https://jekyllrb.com/). GitHub Pages builds it automatically on every
push to `main`; there is no build step to run yourself.

## Where things live

Content is kept in data files. The pages are templates that only read from them,
so every fact is written down in exactly one place.

| To change…                                         | Edit                     |
| -------------------------------------------------- | ------------------------ |
| Name, email, affiliation, photo, profile links     | `_config.yml`            |
| Papers, tutorials, workshops, code projects        | `_data/projects.yml`     |
| News items on the about page                       | `_data/news.yml`         |
| Education, experience, fellowships, skills         | `_data/cv.yml`           |
| Bio paragraphs on the about page                   | `index.md`               |
| Colors, fonts, spacing                             | `assets/css/styles.css`  |

### Adding a paper, tutorial or project

Add one entry to `_data/projects.yml` (the field list is documented at the top
of that file). Where it appears is decided by its fields:

- `type: paper` → publications page, grouped by year, and the CV
- `type: tutorial` or `workshop` → "tutorials & workshops" on the publications
  page, and "Teaching & Talks" on the CV
- `selected: true` → "selected publications" on the about page
- `project: research` or `project: code` → the projects page

To mention it in the news, add an item to `_data/news.yml` with
`project: <its id>` and write `{project}` where its linked title should go.

## Layout of the repository

```
_config.yml              site and author settings
_data/                   all content (projects, news, CV)
_layouts/default.html    page shell: head, navigation, footer
_layouts/about.html      about page: bio, photo, news, selected publications
_includes/               reusable pieces (publication entry, project card, CV row, icons)
index.md                 about page (bio text)
publications.html        publications page template
projects.html            projects page template (category order set in front matter)
cv.html                  CV page template (section order set in front matter)
assets/                  stylesheet, script and images
```

Pages appear in the navigation when their front matter sets `nav_title` and
`nav_order`.

## Previewing locally (optional)

With Ruby installed:

```sh
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
