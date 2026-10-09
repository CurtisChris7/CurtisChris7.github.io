// Small, dependency-free enhancements. Every page is fully readable without JS.
(() => {
  const root = document.documentElement;

  // Mobile menu
  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      const open = navLinks.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", String(open));
      navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
  }

  // Light / dark toggle (defaults to the system setting until the visitor chooses)
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  const current = () => root.dataset.theme || (media.matches ? "dark" : "light");
  const themeToggle = document.querySelector(".theme-toggle");
  const labelToggle = () => {
    if (themeToggle)
      themeToggle.setAttribute(
        "aria-label",
        current() === "dark" ? "Switch to light mode" : "Switch to dark mode",
      );
  };
  if (themeToggle) {
    labelToggle();
    themeToggle.addEventListener("click", () => {
      const next = current() === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try {
        localStorage.setItem("theme", next);
      } catch (e) {
        /* storage unavailable */
      }
      labelToggle();
    });
    media.addEventListener?.("change", labelToggle);
  }

  // BibTeX: show/hide and copy
  document.querySelectorAll("[data-bib-toggle]").forEach((button) => {
    const panel = document.getElementById(button.getAttribute("aria-controls"));
    if (!panel) return;
    button.addEventListener("click", () => {
      const open = panel.hidden;
      panel.hidden = !open;
      button.setAttribute("aria-expanded", String(open));
    });
  });
  document.querySelectorAll(".bibtex .copy").forEach((button) => {
    button.addEventListener("click", async () => {
      const text = button.parentElement.querySelector("pre").textContent;
      let ok = false;
      try {
        await navigator.clipboard.writeText(text);
        ok = true;
      } catch (e) {
        const area = document.createElement("textarea");
        area.value = text;
        area.style.position = "fixed";
        area.style.opacity = "0";
        document.body.appendChild(area);
        area.select();
        try {
          ok = document.execCommand("copy");
        } catch (err) {
          ok = false;
        }
        area.remove();
      }
      const original = button.textContent;
      button.textContent = ok ? "Copied" : "Copy failed";
      setTimeout(() => {
        button.textContent = original;
      }, 1600);
    });
  });

  // CV table of contents: highlight the section in view
  const tocLinks = [...document.querySelectorAll(".toc a")];
  if (tocLinks.length && "IntersectionObserver" in window) {
    const byId = new Map(tocLinks.map((a) => [a.getAttribute("href").slice(1), a]));
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          tocLinks.forEach((a) => a.classList.remove("active"));
          byId.get(entry.target.id)?.classList.add("active");
        });
      },
      { rootMargin: "-20% 0px -70% 0px" },
    );
    byId.forEach((_, id) => {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    });
  }
})();
