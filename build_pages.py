#!/usr/bin/env python3
"""
Splits the single-page site into multiple pages sharing the same
header/nav/footer, css/style.css and js/i18n.js.
Run: python3 build_pages.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

PAGES = ["index", "about", "journey", "chips", "projects", "publications", "photography", "experience", "contact"]

def nav(current):
    items = [
        ("index.html", "nav.home", "Home"),
        ("about.html", "nav.about", "About"),
        ("journey.html", "nav.journey", "Journey"),
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
<link rel="stylesheet" href="css/style.css">
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

FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <p data-i18n="footer.text">&copy; 2026 Yichen Xu. Built with plain HTML/CSS/JS, hosted on GitHub Pages.</p>
  </div>
</footer>

<script src="js/i18n.js"></script>
</body>
</html>
"""

def page(current, title, desc, body):
    return head(title, desc) + header(current) + "<main>\n" + body + "\n</main>\n\n" + FOOTER


# ---------------- INDEX (home) ----------------
index_body = """
  <section id="top" class="hero">
    <div class="wrap hero-grid">
      <div class="hero-photo">
        <div class="ring"></div>
        <div class="photo-placeholder">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4">
            <circle cx="12" cy="8" r="4"></circle>
            <path d="M4 20c0-4.4 3.6-7 8-7s8 2.6 8 7"></path>
          </svg>
          <span class="ph-label" data-i18n="hero.photoPlaceholder">Replace with<br>your photo<br>(assets/headshot.jpg)</span>
        </div>
      </div>

      <div>
        <div class="eyebrow" data-i18n="hero.eyebrow">Ph.D. Candidate &middot; Electrical Engineering &middot; Columbia University</div>
        <h1>Yichen Xu</h1>
        <p class="tagline" data-i18n="hero.tagline">Power management IC designer, chip photographer, and occasional artist.</p>
        <p class="hero-text" data-i18n="hero.text">
          I design power management circuits for modern SoC platforms and emerging AI hardware
          systems &mdash; computational digital LDOs, SIMO DC&ndash;DC converters, switched-capacitor
          converters, and voltage-stacked power delivery for high-bandwidth memory systems.
          Advised by Prof. Mingoo Seok at Columbia University. Beyond the lab, this site also
          collects the chips I've taped out and a few frames from my camera.
        </p>
        <div class="hero-links">
          <a class="pill-link" href="mailto:yx2613@columbia.edu" data-i18n="hero.linkEmail">Email</a>
          <a class="pill-link" href="https://www.linkedin.com/in/yichen-xu-5718911b2/" target="_blank" rel="noopener">LinkedIn</a>
          <a class="pill-link" href="https://github.com/p1zdontsay" target="_blank" rel="noopener">GitHub</a>
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
        <a class="hub-card" href="journey.html">
          <h3 data-i18n="nav.journey">Journey</h3>
          <p data-i18n="home.journey.desc">Zigong &rarr; Chengdu &rarr; New York &rarr; San Jose.</p>
        </a>
        <a class="hub-card" href="chips.html">
          <h3 data-i18n="nav.chips">Chip Gallery</h3>
          <p data-i18n="home.chips.desc">Die shots and test boards from every tape-out.</p>
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
          <p data-i18n="home.photography.desc">A few frames outside the cleanroom.</p>
        </a>
        <a class="hub-card" href="experience.html">
          <h3 data-i18n="nav.experience">Experience</h3>
          <p data-i18n="home.experience.desc">Internships, industry work, and teaching.</p>
        </a>
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

# ---------------- JOURNEY ----------------
def stop(idx, city_key, city_en, region_key, region_en, period_key, period_en, body_key, body_en, coord):
    return f"""        <li class="journey-stop">
          <div class="journey-marker"><span class="journey-dot"></span></div>
          <div class="journey-content">
            <div class="journey-coord">{coord}</div>
            <h3><span data-i18n="{city_key}">{city_en}</span></h3>
            <p class="project-meta"><span data-i18n="{region_key}">{region_en}</span> &middot; <span data-i18n="{period_key}">{period_en}</span></p>
            <p data-i18n="{body_key}">{body_en}</p>
          </div>
        </li>"""

journey_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="journey.eyebrow">01b &mdash; Journey</div>
        <h2 data-i18n="journey.title">Zigong &rarr; Chengdu &rarr; New York &rarr; San Jose</h2>
        <p class="lede" data-i18n="journey.lede">
          A quick map of how a kid from a small city in Sichuan ended up designing power
          management chips on two continents.
        </p>
      </div>

      <ul class="journey-line">
""" + "\n".join([
    stop(1, "journey.s1.city", "Zigong", "journey.s1.region", "Sichuan, China", "journey.s1.period", "Where it started", "journey.s1.body", "Born and raised in Zigong &mdash; a small industrial city in Sichuan known for salt mining, dinosaur fossils, and lantern festivals. First taste of taking things apart to see how they work.", "29.35&deg;N, 104.78&deg;E"),
    stop(2, "journey.s2.city", "Chengdu", "journey.s2.region", "Sichuan, China", "journey.s2.period", "2016 &ndash; 2020", "journey.s2.body", "Moved to the provincial capital for a B.S. in Electrical Engineering at UESTC &mdash; roughly 180&nbsp;km from home, but a first real step away. This is where circuits stopped being a subject and became the thing I wanted to do.", "30.66&deg;N, 104.07&deg;E"),
    stop(3, "journey.s3.city", "New York", "journey.s3.region", "United States", "journey.s3.period", "2021 &ndash; present", "journey.s3.body", "~11,700&nbsp;km from Chengdu for an M.S. &amp; Ph.D. at Columbia University. New country, new language of instruments, same question: how do you keep power clean and efficient when everything around it is switching?", "40.71&deg;N, 74.01&deg;W"),
    stop(4, "journey.s4.city", "San Jose", "journey.s4.region", "California, United States", "journey.s4.period", "Summer 2026", "journey.s4.body", "~4,100&nbsp;km west to Samsung's DRAM Design Lab for a circuit design internship &mdash; from lecture halls in Manhattan to the middle of Silicon Valley's memory industry.", "37.34&deg;N, 121.89&deg;W"),
]) + """
      </ul>
    </div>
  </section>
"""

# ---------------- CHIP GALLERY ----------------
def tile(chip_i, title_key, title_en, meta):
    return f"""        <article class="tile">
          <div class="tile-art chip-art"></div>
          <span class="tile-placeholder-tag" data-i18n="chips.tag">PLACEHOLDER</span>
          <div class="tile-caption">
            <h4 data-i18n="{title_key}">{title_en}</h4>
            <div class="tile-meta">{meta}</div>
          </div>
        </article>"""

chips_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="chips.eyebrow">02 &mdash; Silicon</div>
        <h2 data-i18n="chips.title">Chip Gallery</h2>
        <p class="lede" data-i18n="chips.lede">
          Die shots and test boards from tape-outs across three process nodes. Placeholder art
          below &mdash; swap each <code>.tile-art</code> for a real photo in <code>assets/chips/</code>.
        </p>
      </div>

      <div class="gallery-grid">
""" + "\n".join([
    tile(1, "chips.item1.title", "Computational DLDO", "28nm CMOS &middot; 2023&ndash;2024"),
    tile(2, "chips.item2.title", "DLDO-Assisted Buck Converter", "28nm CMOS &middot; 2024&ndash;2025"),
    tile(3, "chips.item3.title", "Bidirectional SIMO Compensator", "65nm CMOS &middot; 2025&ndash;2026"),
    tile(4, "chips.item4.title", "CSCR Power Converter", "65nm CMOS &middot; 2026&ndash;present"),
    tile(5, "chips.item5.title", "TWS Battery Charging IC", "GF 180nm &middot; 2020&ndash;2021"),
    tile(6, "chips.item6.title", "Ultrasound Range Finder AFE", "65nm CMOS &middot; 2021&ndash;2022"),
]) + """
      </div>
    </div>
  </section>
"""

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
def ptile(key, en):
    return f"""        <article class="tile"><div class="tile-art photo-art"></div><span class="tile-placeholder-tag" data-i18n="chips.tag">PLACEHOLDER</span>
          <div class="tile-caption"><h4 data-i18n="{key}">{en}</h4></div></article>"""

photography_body = """
  <section class="section section-first">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow" data-i18n="photo.eyebrow">05 &mdash; Outside the lab</div>
        <h2 data-i18n="photo.title">Photography</h2>
        <p class="lede" data-i18n="photo.lede">
          A few frames outside the cleanroom. Placeholder art below &mdash; drop real photos into
          <code>assets/photography/</code> and swap the tiles.
        </p>
      </div>

      <div class="gallery-grid">
""" + "\n".join([
    ptile("photo.item1", "Travel"),
    ptile("photo.item2", "Street"),
    ptile("photo.item3", "Nature"),
    ptile("photo.item4", "Architecture"),
    ptile("photo.item5", "Long Exposure"),
    ptile("photo.item6", "Film"),
]) + """
      </div>
    </div>
  </section>
"""

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
      </ul>
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
        GitHub: <a href="https://github.com/p1zdontsay" target="_blank" rel="noopener">p1zdontsay</a>
      </p>
    </div>
  </section>
"""

PAGE_DEFS = {
    "index": ("Home", "Yichen Xu — Ph.D. Candidate in Electrical Engineering, Columbia University.", index_body),
    "about": ("About", "About Yichen Xu — education, research interests, honors.", about_body),
    "journey": ("Journey", "From Zigong to Chengdu to New York and San Jose — Yichen Xu's path.", journey_body),
    "chips": ("Chip Gallery", "Die shots and test boards from Yichen Xu's tape-outs.", chips_body),
    "projects": ("Projects", "Research projects by Yichen Xu.", projects_body),
    "publications": ("Publications", "Papers and patents by Yichen Xu.", publications_body),
    "photography": ("Photography", "Photography by Yichen Xu.", photography_body),
    "experience": ("Experience", "Industry experience and teaching — Yichen Xu.", experience_body),
    "contact": ("Contact", "Contact Yichen Xu.", contact_body),
}

for name, (title, desc, body) in PAGE_DEFS.items():
    html = page(f"{name}.html", title, desc, body)
    with open(os.path.join(OUT, f"{name}.html"), "w") as f:
        f.write(html)

print("wrote", len(PAGE_DEFS), "pages")
