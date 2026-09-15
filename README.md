# yichen-xu.github.io

Personal academic website for Yichen Xu (Ph.D. candidate, EE, Columbia University).

Plain HTML/CSS, no build step, no framework — just `index.html` + `css/style.css`.
Deliberately kept simple so it's easy to hand-edit later.

## File structure

```
.
├── index.html        # all page content lives here (single page, anchor sections)
├── css/
│   └── style.css      # all styling — colors/fonts are CSS variables at the top
└── assets/            # put a headshot / project images / a PDF CV here later
```

## How to edit content

Everything is in `index.html`, split into `<section>` blocks with ids:
`#about`, `#publications`, `#projects`, `#experience`, `#contact`.
To add a paper, copy one `<li>` inside `#publications .pub-list` and edit it.
To add a project, copy one `<article class="project-card">` inside `#projects`.

To change colors/fonts, edit the `:root { ... }` variables at the top of
`css/style.css` — `--color-accent` is the one accent color used for links,
project period labels, etc. A dark-mode palette is already defined and
switches automatically based on the visitor's OS setting.

## Deploying with GitHub Pages

Run these from inside this folder, on your own computer (this assumes `git`
is installed and you're logged into GitHub — either via `gh auth login` or
with git credentials already configured):

```bash
git init
git add .
git commit -m "Initial personal website"

# Option A: create the repo from the command line (needs GitHub CLI: gh)
gh repo create p1zdontsay.github.io --public --source=. --remote=origin --push

# Option B: create the repo manually on github.com first (name it exactly
# p1zdontsay.github.io), then:
git remote add origin https://github.com/p1zdontsay/p1zdontsay.github.io.git
git branch -M main
git push -u origin main
```

Once pushed, GitHub Pages serves it automatically at:

**https://p1zdontsay.github.io**

(A repo named exactly `<username>.github.io` is auto-published at the root
domain with no extra config. If you'd rather use a different repo name,
e.g. `personal-website`, enable Pages manually in the repo's
Settings → Pages → Deploy from branch `main` / root, and the site will be
served at `https://p1zdontsay.github.io/personal-website/` instead.)

## Updating the site later

Any time you edit `index.html` or `style.css`:

```bash
git add .
git commit -m "Update publications"
git push
```

GitHub Pages rebuilds automatically, usually live within a minute.
