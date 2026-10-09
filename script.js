// Tiny, dependency-free enhancements. The portfolio is fully readable without JS.
(() => {
  const navToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      const opened = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(opened));
      navToggle.setAttribute('aria-label', opened ? 'Close menu' : 'Open menu');
    });
    navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.setAttribute('aria-label', 'Open menu');
    }));
  }

  const filters = [...document.querySelectorAll('.filter-button')];
  const projects = [...document.querySelectorAll('[data-category]')];
  filters.forEach(button => button.addEventListener('click', () => {
    const value = button.dataset.filter;
    filters.forEach(item => {
      const active = item === button;
      item.classList.toggle('active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    projects.forEach(item => { item.hidden = value !== 'all' && item.dataset.category !== value; });
  }));

  const bibtex = {
    ciphergrid: `@inproceedings{curtis2026ciphergrid,\n  title = {{CIPHERGRID} Benchmark: From Multimodal Rule Inference to Sequential Action},\n  author = {Curtis, Christopher and Fragoso, Victor and Savage, Saiph},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2026},\n  note = {Accepted, Evaluations and Datasets Track}\n}`,
    chronemics: `@article{toxtli2024culturally,\n  title = {A Culturally-Aware AI Tool for Crowdworkers: Leveraging Chronemics to Support Diverse Work Styles},\n  author = {Toxtli, Carlos and Curtis, Christopher and Savage, Saiph},\n  journal = {Proceedings of the ACM on Human-Computer Interaction},\n  year = {2024},\n  doi = {10.1145/3686899}\n}`,
    officemind: `@inproceedings{curtis2024officemind,\n  title = {Office-Mind AI: A Generative AI Tool for Gig Workers},\n  author = {Curtis, Christopher and Cooper, Seth and Savage, Saiph},\n  booktitle = {Book of Extended Abstracts of the ACM Collective Intelligence Conference},\n  year = {2024}\n}`,
    portraits: `@inproceedings{flores2023inclusive,\n  title = {Inclusive Portraits: Race-Aware Human-in-the-Loop Technology},\n  author = {Flores-Saviaga, Claudia and Curtis, Christopher and Savage, Saiph},\n  booktitle = {Proceedings of the 3rd ACM Conference on Equity and Access in Algorithms, Mechanisms, and Optimization},\n  year = {2023},\n  doi = {10.1145/3617694.3623235}\n}`
  };
  const toast = document.querySelector('#toast');
  let toastTimeout;
  const notify = message => {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => toast.classList.remove('show'), 2600);
  };
  document.querySelectorAll('.bib-button').forEach(button => button.addEventListener('click', async () => {
    const citation = bibtex[button.dataset.bib];
    if (!citation) return;
    try {
      await navigator.clipboard.writeText(citation);
      notify('BibTeX copied to clipboard');
    } catch {
      // A fallback for local files / non-secure contexts.
      const area = document.createElement('textarea');
      area.value = citation; area.style.position = 'fixed'; area.style.opacity = '0';
      document.body.appendChild(area); area.select();
      try { document.execCommand('copy'); notify('BibTeX copied to clipboard'); }
      catch { notify('Copy not available in this browser'); }
      area.remove();
    }
  }));
  const year = document.querySelector('#year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
