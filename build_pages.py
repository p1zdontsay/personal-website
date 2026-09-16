#!/usr/bin/env python3
"""
Splits the single-page site into multiple pages sharing the same
header/nav/footer, css/style.css and js/i18n.js.
Run: python3 build_pages.py
"""
import os
import time

OUT = os.path.dirname(os.path.abspath(__file__))
BUILD_VERSION = str(int(time.time()))  # cache-busting query param for css/js so pushes take effect immediately

PAGES = ["index", "about", "chips", "projects", "publications", "photography", "experience", "contact"]

def nav(current):
    items = [
        ("index.html", "nav.home", "Home"),
        ("about.html", "nav.about", "About"),
        ("chips.html", "nav.chips", "Chip Gallery"),
        ("projects.html", "nav.projects", "Projects"),
        ("publications.html", "nav.publications", "Publications"),
        ("photography.html", "nav.photography", "Photography"),
        ("experience.html", "nav.experience", "Experience"),
        ("contact.html", "nav.contact", "Contact"),
    ]
    links = []
    for href, key, label in items:
        cls = ' class="active"' if href == current else ""
        links.append(f'      <a href="{href}"{cls} data-i18n="{key}">{label}</a>')
    return "\n".join(links)

def head(title_key_text, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Yichen Xu &mdash; {title_key_text}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v={BUILD_VERSION}">
</head>
<body>
"""

def header(current):
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html">Yichen<span>.</span>Xu</a>

    <button class="nav-toggle-btn" id="navToggleBtn" aria-label="Toggle menu">&#9776;</button>

    <nav class="nav nav-links" id="navLinks">
{nav(current)}
    </nav>

    <div class="lang-toggle" role="group" aria-label="Language">
      <button type="button" id="langEn" class="active" data-lang="en">EN</button>
      <button type="button" id="langZh" data-lang="zh">中文</button>
    </div>
  </div>
</header>
"""

FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <p data-i18n="footer.text">&copy; 2026 Yichen Xu. Built with plain HTML/CSS/JS, hosted on GitHub Pages.</p>
  </div>
</footer>

<script src="js/i18n.js?v={BUILD_VERSION}"></script>
</body>
</html>
"""

def page(current, title, desc, body, extra_scripts=""):
    return head(title, desc) + header(current) + "<main>\n" + body + "\n</main>\n\n" + FOOTER.replace(
        f'<script src="js/i18n.js?v={BUILD_VERSION}"></script>',
        extra_scripts + f'<script src="js/i18n.js?v={BUILD_VERSION}"></script>'
    )


# ---------------- INDEX (home) ----------------
index_body = """
  <section id="top" class="hero">
    <div class="wrap hero-grid">
      <div class="hero-photo">
        <div class="ring"></div>
        <img class="hero-photo-img" src="assets/headshot.jpg" alt="Yichen Xu">
      </div>

      <div>
        <div class="eyebrow" data-i18n="hero.eyebrow">Ph.D. Candidate &middot; Electrical Engineering &middot; Columbia University</div>
        <h1 data-i18n="hero.name">Yichen Xu</h1>
        <p class="tagline" data-i18n="hero.tagline">Mixed-Signal IC Designer &amp; Occasional Filmmaker</p>
        <p class="hero-text" data-i18n="hero.text1">
          I design integrated circuits for energy-efficient computing, reducing energy per
          token through high-speed power management and voltage-stacking architectures.
        </p>
        <p class="hero-text" data-i18n="hero.text2">
          My work spans voltage regulators and PDN designs for modern SoCs and accelerators,
          clock generation, digital control, and physical design. I am also interested in
          hardware architectures and simulators at the boundary of circuits and computation.
        </p>
        <p class="hero-text" data-i18n="hero.text3">
          Advised by Prof. Mingoo Seok at Columbia University. Outside the lab, I shoot photos
          and short films with my camera and drone; this site collects a few of them.
        </p>
        <div class="hero-links">
          <a class="pill-link" href="mailto:yx2613@columbia.edu" data-i18n="hero.linkEmail">Email</a>
          <a class="pill-link" href="https://www.linkedin.com/in/yichen-xu-5718911b2/" target="_blank" rel="noopener">LinkedIn</a>
          <a class="pill-link" href="https://space.bilibili.com/32956785" target="_blank" rel="noopener">Bilibili</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="home.eyebrow">Explore</div>
        <h2 data-i18n="home.title">Around the site</h2>
      </div>
      <div class="hub-grid">
        <a class="hub-card" href="about.html">
          <h3 data-i18n="nav.about">About</h3>
          <p data-i18n="home.about.desc">Education, research interests, and honors.</p>
        </a>
        <a class="hub-card" href="chips.html">
          <h3 data-i18n="nav.chips">Chip Gallery</h3>
          <p data-i18n="home.chips.desc">Die shots and package.</p>
        </a>
        <a class="hub-card" href="projects.html">
          <h3 data-i18n="nav.projects">Projects</h3>
          <p data-i18n="home.projects.desc">Research projects, from course work to current tape-outs.</p>
        </a>
        <a class="hub-card" href="publications.html">
          <h3 data-i18n="nav.publications">Publications</h3>
          <p data-i18n="home.publications.desc">Papers and patents.</p>
        </a>
        <a class="hub-card" href="photography.html">
          <h3 data-i18n="nav.photography">Photography</h3>
          <p data-i18n="home.photography.desc">A few frames outside of the lab.</p>
        </a>
        <a class="hub-card" href="experience.html">
          <h3 data-i18n="nav.experience">Experience</h3>
          <p data-i18n="home.experience.desc">Internships, industry work, and teaching.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="visitors.eyebrow">Live</div>
        <h2 data-i18n="visitors.title">Visitors</h2>
        <p class="lede" data-i18n="visitors.lede">A small live map of where people are reading this site from right now.</p>
      </div>
      <div class="visitor-map-wrap">
        <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=1BsmQQTtG9AVT_iJg1JJlvb_ykU5HgRPunwFZ4erUIM&cl=ffffff&w=a"></script>
      </div>
    </div>
  </section>
"""

# ---------------- ABOUT ----------------
about_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="about.eyebrow">01 &mdash; About</div>
        <h2 data-i18n="about.title">About</h2>
      </div>

      <div class="about-grid">
        <div class="about-block">
          <h3 data-i18n="about.education.title">Education</h3>
          <ul class="plain-list">
            <li data-i18n="about.education.columbia">
              <strong>Columbia University</strong> &mdash; M.S. &amp; Ph.D. in Electrical Engineering (Advisor: Mingoo Seok)
              <span class="meta">2021&ndash;2027</span>
            </li>
            <li data-i18n="about.education.uestc">
              <strong>UESTC</strong> &mdash; B.S. in Electrical Engineering
              <span class="meta">2016&ndash;2020</span>
            </li>
          </ul>
        </div>

        <div class="about-block">
          <h3 data-i18n="about.interests.title">Research Interests</h3>
          <ul class="plain-list" data-i18n="about.interests.body">
            <li>Computational digital LDOs (DLDOs), DC&ndash;DC SIMO converters, and switched-capacitor (SC) power converters</li>
            <li>Droop detection, DVFS, and power delivery network design</li>
          </ul>
        </div>

        <div class="about-block">
          <h3 data-i18n="about.honors.title">Honors</h3>
          <ul class="plain-list" data-i18n="about.honors.body">
            <li>Master of Science Award of Excellence, Columbia University (top 5%)</li>
            <li>Outstanding Student Scholarship, UESTC</li>
            <li>Best Poster Award, IBM AI Symposium 2024</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""

# ---------------- JOURNEY (compact, embedded in Experience) ----------------
def stop(idx, lat, lon, city_key, city_en, region_key, region_en, period_key, period_en):
    ns = "N" if lat >= 0 else "S"
    ew = "E" if lon >= 0 else "W"
    coord = f"{abs(lat):.2f}&deg;{ns}, {abs(lon):.2f}&deg;{ew}"
    return f"""        <li class="journey-stop journey-stop-compact" id="stop-{idx}" data-lat="{lat}" data-lon="{lon}" data-order="{idx}">
          <div class="journey-marker"><span class="journey-dot"></span></div>
          <div class="journey-content">
            <div class="journey-coord">{coord}</div>
            <h3><span data-i18n="{city_key}">{city_en}</span></h3>
            <p class="project-meta"><span data-i18n="{region_key}">{region_en}</span> &middot; <span data-i18n="{period_key}">{period_en}</span></p>
          </div>
        </li>"""

journey_mini_body = """
      <h3 class="subhead" data-i18n="journey.sectionTitle">Journey</h3>
      <p class="lede" data-i18n="journey.lede">
        Zigong &rarr; Chengdu &rarr; Suzhou &rarr; Shanghai &rarr; New York &rarr; San Jose.
      </p>

      <div class="journey-map-wrap journey-map-wrap-small">
        <svg id="journeyMap" viewBox="0 0 960 480" role="img" aria-label="World map showing Yichen's journey"></svg>
      </div>

      <ul class="journey-line journey-line-compact">
""" + "\n".join([
    stop(1, 29.35, 104.78, "journey.s1.city", "Zigong", "journey.s1.region", "Sichuan, China", "journey.s1.period", "Where it started"),
    stop(2, 30.66, 104.07, "journey.s2.city", "Chengdu", "journey.s2.region", "Sichuan, China", "journey.s2.period", "2016 &ndash; 2020"),
    stop(3, 31.30, 120.62, "journey.s3.city", "Suzhou", "journey.s3.region", "Jiangsu, China", "journey.s3.period", "2019"),
    stop(4, 31.23, 121.47, "journey.s4.city", "Shanghai", "journey.s4.region", "China", "journey.s4.period", "2020 &ndash; 2021"),
    stop(5, 40.71, -74.01, "journey.s5.city", "New York", "journey.s5.region", "United States", "journey.s5.period", "2021 &ndash; present"),
    stop(6, 37.34, -121.89, "journey.s6.city", "San Jose", "journey.s6.region", "California, United States", "journey.s6.period", "Summer 2026"),
]) + """
      </ul>
"""

# Shared lightbox markup (click-to-enlarge, with prev/next nav) — used by any page whose
# script wires up buttons with a data-full attribute into #photoLightbox.
LIGHTBOX_HTML = """
  <div class="lightbox" id="photoLightbox">
    <button type="button" class="lightbox-close" id="lightboxClose" aria-label="Close">&times;</button>
    <button type="button" class="lightbox-nav lightbox-prev" id="lightboxPrev" aria-label="Previous photo">&#10094;</button>
    <img id="lightboxImg" src="" alt="">
    <button type="button" class="lightbox-nav lightbox-next" id="lightboxNext" aria-label="Next photo">&#10095;</button>
  </div>
"""

# ---------------- CHIP GALLERY ----------------
def dtile(img, label_key, label_en, idx_label):
    path = f"assets/chips/{img}"
    return f"""        <article class="tile">
          <button type="button" class="tile-art tile-thumb" data-full="{path}" aria-label="{label_en} {idx_label}">
            <img class="tile-img" src="{path}" alt="{label_en} {idx_label}" loading="lazy">
          </button>
          <div class="tile-caption">
            <h4 data-i18n="{label_key}">{label_en}</h4>
            <div class="tile-meta">{idx_label}</div>
          </div>
        </article>"""

chips_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="chips.eyebrow">02 &mdash; Silicon</div>
        <h2 data-i18n="chips.title">Chip Gallery</h2>
        <p class="lede" data-i18n="chips.lede">
          Packaged parts and bare die from tape-outs and lab work over the years.
        </p>
      </div>

      <h3 class="subhead" data-i18n="chips.packaged.title">Packaged</h3>
      <div class="gallery-grid">
""" + "\n".join([
    dtile("die-1.jpg", "chips.packaged.item", "Packaged chip", "01"),
    dtile("die-2.jpg", "chips.packaged.item", "Packaged chip", "02"),
    dtile("die-3.jpg", "chips.packaged.item", "Packaged chip", "03"),
]) + """
      </div>

      <h3 class="subhead" data-i18n="chips.bare.title">Bare Die</h3>
      <div class="gallery-grid">
""" + "\n".join([
    dtile("die-4.jpg", "chips.bare.item", "Bare die", "01"),
    dtile("die-5.jpg", "chips.bare.item", "Bare die", "02"),
    dtile("die-6.jpg", "chips.bare.item", "Bare die", "03"),
    dtile("die-7.jpg", "chips.bare.item", "Bare die", "04"),
]) + """
      </div>
    </div>
  </section>
""" + LIGHTBOX_HTML

# ---------------- PROJECTS ----------------
projects_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="projects.eyebrow">03 &mdash; Research</div>
        <h2 data-i18n="projects.title">Projects</h2>
      </div>

      <div class="project-grid">
        <article class="project-card">
          <div class="project-period">2026&ndash;present</div>
          <h3 data-i18n="projects.p1.title">Continuously Scalable Conversion Ratio (CSCR) Power Converter for Stacked Systems</h3>
          <p class="project-meta">65 nm CMOS</p>
          <p data-i18n="projects.p1.body">
            Designing a CSCR-based mismatch compensator for stacked voltage-domain systems, with automatic
            source/sink mode selection to maintain high efficiency under large current mismatch.
          </p>
        </article>

        <article class="project-card">
          <div class="project-period">2025&ndash;2026</div>
          <h3 data-i18n="projects.p2.title">HBM Voltage-Stacked Power Delivery &amp; Memory-System Modeling</h3>
          <p data-i18n="projects.p2.body">
            Built a DRAMSim3/Accel-Sim&ndash;based framework to analyze per-channel power, latency, and current
            mismatch in HBM2/HBM3 systems under GPU workloads. Proposed a voltage-stacked HBM power delivery
            architecture and load-mismatch metrics, identifying up to 113&nbsp;mA of inter-channel current mismatch
            and evaluating TSV / power-efficiency trade-offs.
          </p>
        </article>

        <article class="project-card">
          <div class="project-period">2025&ndash;2026</div>
          <h3 data-i18n="projects.p3.title">Bidirectional SIMO Mismatch Compensator for Stacked Voltage-Domain Systems</h3>
          <p class="project-meta">65 nm CMOS</p>
          <p data-i18n="projects.p3.body">
            Invented a bidirectional zero-current detector (Bi-ZCD) for source/sink current regulation in
            voltage-stacked systems, achieving 98.5% peak efficiency and 82% efficiency under 360&nbsp;mA load
            mismatch.
          </p>
          <p class="project-pub" data-i18n="projects.p3.pub">&rarr; Published as VSIMO, IEEE VLSI Symposium 2026</p>
        </article>

        <article class="project-card">
          <div class="project-period">2024&ndash;2025</div>
          <h3 data-i18n="projects.p4.title">Computational DLDO-Assisted Buck DC&ndash;DC Converter</h3>
          <p class="project-meta">28 nm CMOS</p>
          <p data-i18n="projects.p4.body">
            Designed a DLDO-assisted buck converter with one-step computational droop compensation and
            DLDO-controlled current handover, achieving 68-mV droop, 112-ns settling time, and 95.5% peak
            efficiency for 1A/0.8ns load transients.
          </p>
          <p class="project-pub" data-i18n="projects.p4.pub">&rarr; Published in IEEE SSCL 2025</p>
        </article>

        <article class="project-card">
          <div class="project-period">2023&ndash;2024</div>
          <h3 data-i18n="projects.p5.title">Computational DLDO with Load-Dependent Feedback and Fast DVS</h3>
          <p class="project-meta">28 nm CMOS</p>
          <p data-i18n="projects.p5.body">
            Designed a rising-edge computational DLDO with load-dependent feedback and DVS computation,
            achieving a 0.15-ps FoM, 25-mV/ns DVS rate, and low ripple across a 1-to-1050&nbsp;mA load range.
          </p>
          <p class="project-pub" data-i18n="projects.p5.pub">&rarr; Published at IEEE VLSI Symposium 2026; invited manuscript, IEEE JSSC 2027</p>
        </article>

        <article class="project-card">
          <div class="project-period">2022&ndash;2023</div>
          <h3 data-i18n="projects.p6.title">Dynamic Load Regulation Limit Model for Digital LDOs</h3>
          <p data-i18n="projects.p6.body">
            Established an analytical model of dynamic load regulation for commonly used DLDO architectures,
            analyzing the impact of design parameters and providing optimal design points for power switch sizing.
          </p>
          <p class="project-pub" data-i18n="projects.p6.pub">&rarr; Published in IEEE TVLSI 2024</p>
        </article>

        <article class="project-card">
          <div class="project-period">2021&ndash;2022</div>
          <h3><span data-i18n="projects.p7.title">Ultrasound Range Finder Analog Front End</span> <span class="project-tag" data-i18n="projects.p7.tag">Course Project</span></h3>
          <p class="project-meta">65 nm CMOS &middot; EE6350</p>
          <p data-i18n="projects.p7.body">
            Designed a 9-setting programmable-gain amplifier using replica-based common-mode feedback, and
            developed the strong-arm comparator, track-and-hold, and capacitor-based DAC for a 125&nbsp;kHz
            8-bit SAR ADC.
          </p>
        </article>
      </div>
    </div>
  </section>
"""

# ---------------- PUBLICATIONS ----------------
publications_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="publications.eyebrow">04 &mdash; Writing</div>
        <h2 data-i18n="publications.title">Publications</h2>
      </div>

      <ol class="pub-list">
        <li>
          Yichen Xu, Rentao Wan, Mao Li, Zhaoqing Wang, Suhwan Kim, Ram K. Krishnamurthy, Xin Zhang, and Mingoo Seok,
          &ldquo;A Rising-Edge Computational Digital LDO With Load-Dependent Feedback and Fast Dynamic Voltage Scaling,&rdquo;
          <em>invited manuscript under review, IEEE Journal of Solid-State Circuits (JSSC)</em>, 2027.
        </li>
        <li>
          Yichen Xu, Shahreer Ahmed Al Hossain, Baoqi Zhu, Suhwan Kim, Ram K. Krishnamurthy, Xin Zhang, Mingoo Seok,
          &ldquo;VSIMO: A DC-DC SIMO-based Current Mismatch Compensator Supporting Per-Output Bidirectional Power Flow
          for Stacked Voltage Domains Achieving &gt;82% System Efficiency under up to 360-mA Load Mismatch,&rdquo;
          <em>IEEE Symposium on VLSI Circuits (VLSI)</em>, 2026.
        </li>
        <li>
          Yichen Xu, Rentao Wan, Mao Li, Zhaoqing Wang, Suhwan Kim, Ram K. Krishnamurthy, Xin Zhang, Mingoo Seok,
          &ldquo;A 1mA-to-1050mA DLDO with Rising-Edge Feedforward Control and Load-Dependent Feedback Achieving 0.15-ps
          Load Transient FoM, 14-mV Output Ripple, and 25-mV/ns DVS Rate in a 28nm CMOS,&rdquo;
          <em>IEEE Symposium on VLSI Circuits (VLSI)</em>, 2026.
        </li>
        <li>
          Yichen Xu, Zhaoqing Wang, Rentao Wan, Suhwan Kim, Minxiang Gong, Ram Kumar Krishnamurthy, Xin Zhang, Mingoo Seok,
          &ldquo;Digital Low-Dropout Regulator-Assisted Buck DC-DC Converter Achieving 68-mV Droop Voltage and 95.5% Efficiency,&rdquo;
          <em>IEEE Solid-State Circuits Letter (SSCL)</em>, 2025.
        </li>
        <li>
          Rentao Wan, Yichen Xu, Dong-Woo Jee, Mingoo Seok,
          &ldquo;AJPEG: A 26.4-pJ/pixel, 252-fps, 128x128 Image Sensor with an In-Sensor Analog DCT Processor for
          Data Compression,&rdquo;
          <em>IEEE Custom Integrated Circuits Conference (CICC)</em>, 2025.
        </li>
        <li>
          Zhaoqing Wang, Yichen Xu, Suhwan Kim, Nachiket Desai, Minxiang Gong, Ram K. Krishnamurthy, Xin Zhang, Mingoo Seok,
          &ldquo;A 93.9% Peak Efficiency 3V-to-40V-Input GaN-based DC-DC Converter with Unified Reliability and Efficiency
          Adaptive Control,&rdquo;
          <em>IEEE Custom Integrated Circuits Conference (CICC)</em>, 2025.
        </li>
        <li>
          Yichen Xu, Zhaoqing Wang, Jonghyun Oh, Mingoo Seok,
          &ldquo;Model-Based Study on the Limit of the Dynamic Load Regulation Performance of a Digital Low Dropout
          Regulator,&rdquo;
          <em>IEEE Transactions on VLSI Systems (TVLSI)</em>, 2024.
        </li>
        <li>
          F. Du, F. Hou, W. Song, L. Chen, Y. Nie, Y. Qing, Yichen Xu, J. Liu, Z. Liu, J. J. Liou,
          &ldquo;An Improved Silicon-Controlled Rectifier (SCR) for Low-Voltage ESD Application,&rdquo;
          <em>IEEE Transactions on Electron Devices</em>, vol. 67, no. 2, pp. 576&ndash;581, 2020.
        </li>
        <li>
          F. Du, X. Dong, C. Yang, Yichen Xu, Z. Liu, J. Liu, J. J. Liou,
          &ldquo;A Robust Dual Directional SCR without Current Saturation Effect for ESD Applications,&rdquo;
          <em>2019 IEEE 26th International Symposium on Physical and Failure Analysis of Integrated Circuits (IPFA)</em>, 2019.
        </li>
      </ol>

      <h3 class="subhead" data-i18n="publications.patents">Patents</h3>
      <ol class="pub-list">
        <li>Yichen Xu, Xizhen Yin, &ldquo;A High Voltage LDO-Based Linear Charging System,&rdquo; issued Apr 28, 2023.</li>
        <li>Yichen Xu, Xizhen Yin, &ldquo;A Substrate Switching Circuit for LDO Backflow Current Protection,&rdquo; issued Nov 18, 2022.</li>
      </ol>
    </div>
  </section>
"""

# ---------------- PHOTOGRAPHY ----------------
def rtile(folder, img, alt="Photo"):
    return f"""          <article class="tile"><img class="tile-art tile-img" src="assets/photography/{folder}/{img}" alt="{alt}" loading="lazy"></article>"""

def thumb(folder, img, alt):
    path = f"assets/photography/{folder}/{img}"
    return f"""            <button type="button" class="place-thumb" data-full="{path}"><img src="{path}" alt="{alt}" loading="lazy"></button>"""

def place(folder, cover, name_key, name_en, photos):
    thumbs = "\n".join([thumb(folder, p, name_en) for p in photos])
    return f"""        <div class="place-card">
          <button type="button" class="place-cover" aria-label="{name_en}"><img src="assets/photography/{folder}/{cover}" alt="{name_en}" loading="lazy"></button>
          <span class="place-name" data-i18n="{name_key}">{name_en}</span>
          <div class="place-thumbs">
{thumbs}
          </div>
        </div>"""

def vtile(bvid, title_key, title_en):
    return f"""        <div class="video-card">
          <h4 data-i18n="{title_key}">{title_en}</h4>
          <div class="video-embed">
            <iframe src="//player.bilibili.com/player.html?bvid={bvid}&page=1&high_quality=1&danmaku=0"
              scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true" loading="lazy"></iframe>
          </div>
        </div>"""

photography_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="photo.eyebrow">05 &mdash; Outside the lab</div>
        <h2 data-i18n="photo.title">Photography</h2>
        <p class="lede" data-i18n="photo.lede">A few frames outside of the lab.</p>
      </div>

      <h3 class="subhead" data-i18n="photo.photo.title">Photo</h3>
      <p class="lede" data-i18n="photo.photo.lede">Hover or tap a place to see a few frames from there &mdash; click one to view it larger. More places coming.</p>
      <div class="place-grid">
""" + place("Hawaii", "hawaii-7.jpg", "photo.place.hawaii", "Hawaii",
            [f"hawaii-{n}.jpg" for n in range(1, 17) if n != 7]) + """
""" + place("Altay", "altay-5.jpg", "photo.place.altay", "Altay",
            [f"altay-{n}.jpg" for n in range(1, 10) if n != 5]) + """
""" + place("Iceland", "iceland-10.jpg", "photo.place.iceland", "Iceland",
            [f"iceland-{n}.jpg" for n in range(1, 12) if n != 10]) + """
""" + place("Dubai", "dubai-1.jpg", "photo.place.dubai", "Dubai",
            [f"dubai-{n}.jpg" for n in range(2, 8)]) + """
      </div>

      <h3 class="subhead" data-i18n="photo.video.title">Video</h3>
      <p class="lede" data-i18n="photo.video.lede">A few short videos I made.</p>
      <div class="video-grid">
""" + "\n".join([
    vtile("BV1RmPTzMEkF", "photo.video.v1", "Altay"),
    vtile("BV1RMyuYeESv", "photo.video.v2", "Iceland"),
    vtile("BV15A411b7js", "photo.video.v3", "Malaysia"),
    vtile("BV13mfSB6Efp", "photo.video.v4", "Vail"),
]) + """
      </div>
    </div>
  </section>
""" + LIGHTBOX_HTML

# ---------------- EXPERIENCE ----------------
experience_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="experience.eyebrow">06 &mdash; Industry</div>
        <h2 data-i18n="experience.title">Experience</h2>
      </div>

      <ul class="timeline">
        <li>
          <div class="timeline-period">Summer 2026</div>
          <div class="timeline-body">
            <h3 data-i18n="experience.e1.title">Circuit Design Intern &mdash; DRAM Design Lab, Samsung</h3>
            <p class="project-meta">San Jose, CA</p>
            <p data-i18n="experience.e1.body">
              Designed a fully integrated voltage regulator for the LPDDR6 Built-of-Test (LP6BOT) chip, and a
              three-path regulation architecture (feedback, PSR feedforward, transient feedforward) achieving
              &gt;20&nbsp;dB PSRR at 100&nbsp;MHz. Coordinated the chip power delivery network layout in Samsung 14nm CMOS.
            </p>
          </div>
        </li>
        <li>
          <div class="timeline-period">Summer 2025</div>
          <div class="timeline-body">
            <h3 data-i18n="experience.e2.title">Graduate Technical Intern &mdash; Intel</h3>
            <p class="project-meta">Hillsboro, OR</p>
            <p data-i18n="experience.e2.body">
              Developed SPICE/Verilog-A models for adaptive clocking, clock throttling, and switched-capacitor
              load balancing; created a critical-path replica circuit with background calibration for setup
              violation detection in Intel 16nm CMOS.
            </p>
          </div>
        </li>
        <li>
          <div class="timeline-period">Summer 2022</div>
          <div class="timeline-body">
            <h3 data-i18n="experience.e3.title">Mixed-Signal Design Engineer Intern &mdash; Ambarella</h3>
            <p class="project-meta">Santa Clara, CA</p>
            <p data-i18n="experience.e3.body">
              Performed low-power standard-cell schematic and layout design in Samsung 4nm FinFET, and developed
              an automated Python-based .lib generation flow for digital place-and-route.
            </p>
          </div>
        </li>
        <li>
          <div class="timeline-period">2020&ndash;2021</div>
          <div class="timeline-body">
            <h3 data-i18n="experience.e4.title">Analog and System IC Engineer &mdash; Chip Dance Technology</h3>
            <p class="project-meta">Shanghai, China</p>
            <p data-i18n="experience.e4.body">
              Led a True Wireless Stereo lithium battery charging chip architecture, taped out in GF 180nm.
              Designed a sub-threshold BGR with digital trimming DAC and a PVT-tolerant hysteresis comparator,
              and an LDO-based linear battery charger for 5V-to-4.2V regulation (first inventor on related patent).
            </p>
          </div>
        </li>
      </ul>

      <h3 class="subhead" data-i18n="experience.teaching">Teaching</h3>
      <ul class="plain-list">
        <li data-i18n="experience.t1">Teaching Assistant, Modern Power Management IC Design (ELEN 6920) &mdash; Fall 2022 / 2023 / 2024</li>
        <li data-i18n="experience.t2">Teaching Assistant, VLSI Design Lab (ELEN 6350) &mdash; Spring 2025</li>
        <li data-i18n="experience.t3">Substitute Lecturer, Advanced Digital Electronic Circuits (EE6321) &mdash; interconnect in VLSI, Spring 2026</li>
      </ul>
""" + journey_mini_body + """
    </div>
  </section>
"""

# ---------------- CONTACT ----------------
contact_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="contact.eyebrow">07 &mdash; Say hello</div>
        <h2 data-i18n="contact.title">Contact</h2>
      </div>
      <p>
        Email: <a href="mailto:yx2613@columbia.edu">yx2613@columbia.edu</a><br>
        LinkedIn: <a href="https://www.linkedin.com/in/yichen-xu-5718911b2/" target="_blank" rel="noopener">yichen-xu-5718911b2</a><br>
        Bilibili: <a href="https://space.bilibili.com/32956785" target="_blank" rel="noopener">plzdontsay</a>
      </p>
    </div>
  </section>
"""

PAGE_DEFS = {
    "index": ("Home", "Yichen Xu — Ph.D. Candidate in Electrical Engineering, Columbia University.", index_body),
    "about": ("About", "About Yichen Xu — education, research interests, honors.", about_body),
    "chips": ("Chip Gallery", "Die shots and test boards from Yichen Xu's tape-outs.", chips_body),
    "projects": ("Projects", "Research projects by Yichen Xu.", projects_body),
    "publications": ("Publications", "Papers and patents by Yichen Xu.", publications_body),
    "photography": ("Photography", "Photography by Yichen Xu.", photography_body),
    "experience": ("Experience", "Industry experience, teaching, and Yichen Xu's journey from Zigong to San Jose.", experience_body),
    "contact": ("Contact", "Contact Yichen Xu.", contact_body),
}

EXTRA_SCRIPTS = {
    "experience": f'<script src="assets/vendor/topojson-client.min.js"></script>\n<script src="js/journey-map.js?v={BUILD_VERSION}"></script>\n',
    "photography": f'<script src="js/photo-gallery.js?v={BUILD_VERSION}"></script>\n',
    "chips": f'<script src="js/photo-gallery.js?v={BUILD_VERSION}"></script>\n',
}

for name, (title, desc, body) in PAGE_DEFS.items():
    html = page(f"{name}.html", title, desc, body, EXTRA_SCRIPTS.get(name, ""))
    with open(os.path.join(OUT, f"{name}.html"), "w") as f:
        f.write(html)

print("wrote", len(PAGE_DEFS), "pages")
