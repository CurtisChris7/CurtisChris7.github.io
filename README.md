# Christopher Curtis — personal research website

A responsive, accessible academic portfolio built for **GitHub Pages**, with no build step, no frameworks, and no server-side requirements. Updated with user-provided resume and presentation photograph (October 2026).

## Live site address

Once you publish this repository as `CurtisChris7.github.io`, the site will be at:

**https://CurtisChris7.github.io/**

This download is a complete website but has **not** been pushed or deployed to GitHub.

## Publish to GitHub Pages

1. In GitHub, create a **public** repository named exactly **`CurtisChris7.github.io`** in the `CurtisChris7` account. (If it already exists, use it instead.)
2. Upload **all files and the `assets/` folder** from this package to the repository's root. Commit to the default `main` branch.
3. Open the repository's **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **`main`** and **`/(root)`**, and save.
4. Open `https://CurtisChris7.github.io/` after GitHub publishes the site.

You can also publish this as a project site under a different repository. All CSS, JS and asset references are relative.

## Edit content

- `index.html`: biography, publications, research, affiliations, education, open resources, external links, SEO metadata.
- `styles.css`: typography, spacing, colors, mobile breakpoints, component styles.
- `script.js`: working mobile menu, research filters, BibTeX copy actions.
- `assets/*.svg`: editable original vector artwork, favicon, social sharing visual.
- `make_assets.py`: optional local SVG generator; not needed on GitHub Pages.

The homepage uses the supplied public-speaking photograph at `assets/christopher-curtis-speaking.webp`. Replace that file to change the photo.

## Editorial accuracy / review before publishing

The website distinguishes accepted/published works from work still in progress. Key facts were cross-checked against Northeastern University, NeurIPS, ACM records, the authors' public repositories, and the CIPHERGRID dataset card (checked October 9, 2026).

**Please check personal details before publishing:**

- Confirm you want to publicly mention former U.S. Army Infantry service in the About section; remove that paragraph if not.
- The 2025-era resume supplied by Christopher Curtis confirms the MS at Northeastern (2022), BS at Stony Brook (2018), undergraduate CS minor, and WCC Honors College (2016). The exact dates and descriptions of older jobs and program participation are drawn from that resume and should be reviewed before public release.
- The NSF IRES Germany selection, GPAI student mentorship, and teaching of recurring hands-on LLM workshops are based on the supplied older resume. Confirm current program names and whether you want these on the public site.
- The Professional Legibility, ShadowWork AI and online-health projects are labeled **research in progress**, not published or accepted research.
- The ORCID identifier was cross-checked against the ACM EAAMO author page. Confirm it is the profile you want to link.
- The CIPHERGRID paper is shown as accepted/forthcoming with no invented DOI. Replace the dataset/code-only links once the official paper URL is public.
- The Research collaborations note identifies researchers at Microsoft and UNAM as collaborators, **not your employers or your own affiliations**.
- The website intentionally does **not** include the older resume PDF or its personal telephone number. You can publish a refreshed CV separately when it is ready.
- Check whether you want the contact email `curtis.ch@northeastern.edu` shown publicly.

## Source links

- [Northeastern researcher profile](https://www.khoury.northeastern.edu/people/christopher-curtis/)
- [Civic AI Lab team](https://civicai.khoury.northeastern.edu/research-team/)
- [NSF PEAR fellowship, university feature](https://coe.northeastern.edu/news/first-cohort-of-nsf-nrt-student-trainees-share-value-of-interdisciplinary-research-and-the-new-program/)
- [NeurIPS 2025 official tutorial](https://neurips.cc/virtual/2025/loc/mexico-city/128797)
- [CIPHERGRID dataset card](https://huggingface.co/datasets/AnonCC7/CIPHERGRID)
- [CIPHERGRID code repository](https://github.com/CurtisChris7/CIPHERGRID)
- [Chronemics paper DOI](https://doi.org/10.1145/3686899)
- [Office-Mind AI official conference program](https://www.networkscienceinstitute.org/ci2024)
- [Inclusive Portraits DOI](https://doi.org/10.1145/3617694.3623235)

## Privacy and accessibility

The design uses semantic headings, focus outlines, meaningful image descriptions, a skip link, reduced-motion handling, responsive layout, and plain HTML content that remains available without JavaScript. Google Fonts are loaded with system font fallbacks. All other assets are local.
