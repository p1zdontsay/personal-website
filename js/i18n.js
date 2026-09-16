/* ------------------------------------------------------------
   Bilingual (EN / 中文) text for Yichen Xu's site.
   Every element in index.html with a data-i18n="key" attribute
   gets its innerHTML replaced from this dictionary on toggle.
   Publication/patent citations are NOT translated (standard
   academic convention — citations stay in their original form).
   ------------------------------------------------------------ */

const I18N = {
  en: {
    "nav.home": "Home",
    "nav.about": "About",
    "nav.journey": "Journey",
    "nav.chips": "Chip Gallery",
    "nav.projects": "Projects",
    "nav.publications": "Publications",
    "nav.photography": "Photography",
    "nav.experience": "Experience",
    "nav.contact": "Contact",

    "hero.photoPlaceholder": "Replace with<br>your photo<br>(assets/headshot.jpg)",
    "hero.name": "Yichen Xu",
    "hero.eyebrow": "Ph.D. Candidate &middot; Electrical Engineering &middot; Columbia University",
    "hero.tagline": "Power management IC designer and occasional video maker.",
    "hero.text": "I design power management circuits for modern SoC platforms and emerging AI hardware systems &mdash; computational digital LDOs, SIMO DC&ndash;DC converters, switched-capacitor converters, and voltage-stacked power delivery for high-bandwidth memory systems. Advised by Prof. Mingoo Seok at Columbia University. Beyond the lab, this page also collects the chips I've taped out and a few frames from my camera.",
    "hero.linkEmail": "Email",

    "home.eyebrow": "Explore",
    "home.title": "Around the site",
    "home.about.desc": "Education, research interests, and honors.",
    "home.journey.desc": "Zigong &rarr; Chengdu &rarr; Suzhou &rarr; Shanghai &rarr; New York &rarr; San Jose.",
    "home.chips.desc": "Die shots and test boards from every tape-out.",
    "home.projects.desc": "Research projects, from course work to current tape-outs.",
    "home.publications.desc": "Papers and patents.",
    "home.photography.desc": "A few frames outside the cleanroom.",
    "home.experience.desc": "Internships, industry work, and teaching.",

    "visitors.eyebrow": "Live",
    "visitors.title": "Visitors",
    "visitors.lede": "A small live map of where people are reading this site from right now.",

    "about.eyebrow": "01 &mdash; About",
    "about.title": "About",
    "about.education.title": "Education",
    "about.education.columbia": "<strong>Columbia University</strong> &mdash; M.S. &amp; Ph.D. in Electrical Engineering (Advisor: Mingoo Seok)<span class=\"meta\">2021&ndash;2027</span>",
    "about.education.uestc": "<strong>UESTC</strong> &mdash; B.S. in Electrical Engineering<span class=\"meta\">2016&ndash;2020</span>",
    "about.interests.title": "Research Interests",
    "about.interests.body": "<li>Computational digital LDOs (DLDOs), DC&ndash;DC SIMO converters, and switched-capacitor (SC) power converters</li><li>Droop detection, DVFS, and power delivery network design</li>",
    "about.honors.title": "Honors",
    "about.honors.body": "<li>Master of Science Award of Excellence, Columbia University (top 5%)</li><li>Outstanding Student Scholarship, UESTC</li><li>Best Poster Award, IBM AI Symposium 2024</li>",

    "journey.sectionTitle": "Journey",
    "journey.lede": "Zigong &rarr; Chengdu &rarr; Suzhou &rarr; Shanghai &rarr; New York &rarr; San Jose.",
    "journey.s1.city": "Zigong",
    "journey.s1.region": "Sichuan, China",
    "journey.s1.period": "Where it started",
    "journey.s1.body": "Born and raised in Zigong &mdash; a small industrial city in Sichuan known for salt mining, dinosaur fossils, and lantern festivals. First taste of taking things apart to see how they work.",
    "journey.s2.city": "Chengdu",
    "journey.s2.region": "Sichuan, China",
    "journey.s2.period": "2016 &ndash; 2020",
    "journey.s2.body": "Moved to the provincial capital for a B.S. in Electrical Engineering at UESTC &mdash; roughly 180&nbsp;km from home, but a first real step away. This is where circuits stopped being a subject and became the thing I wanted to do.",
    "journey.s3.city": "Suzhou",
    "journey.s3.region": "Jiangsu, China",
    "journey.s3.period": "2019",
    "journey.s3.body": "A spell in Suzhou in 2019 &mdash; [tell me what you were doing here and I'll fill this in properly].",
    "journey.s4.city": "Shanghai",
    "journey.s4.region": "China",
    "journey.s4.period": "2020 &ndash; 2021",
    "journey.s4.body": "Joined Chip Dance Technology (a startup) as an Analog and System IC Engineer, leading a True Wireless Stereo battery-charging chip architecture that taped out in GF 180nm &mdash; first time seeing a chip I designed go from schematic to silicon.",
    "journey.s5.city": "New York",
    "journey.s5.region": "United States",
    "journey.s5.period": "2021 &ndash; present",
    "journey.s5.body": "~11,700&nbsp;km from Shanghai for an M.S. &amp; Ph.D. at Columbia University. New country, new language of instruments, same question: how do you keep power clean and efficient when everything around it is switching?",
    "journey.s6.city": "San Jose",
    "journey.s6.region": "California, United States",
    "journey.s6.period": "Summer 2026",
    "journey.s6.body": "~4,100&nbsp;km west to Samsung's DRAM Design Lab for a circuit design internship &mdash; from lecture halls in Manhattan to the middle of Silicon Valley's memory industry.",

    "chips.eyebrow": "02 &mdash; Silicon",
    "chips.title": "Chip Gallery",
    "chips.lede": "Packaged parts and bare die from tape-outs and lab work over the years.",
    "chips.packaged.title": "Packaged",
    "chips.packaged.item": "Packaged chip",
    "chips.bare.title": "Bare Die",
    "chips.bare.item": "Bare die",
    "chips.tag": "PLACEHOLDER",

    "projects.eyebrow": "03 &mdash; Research",
    "projects.title": "Projects",
    "projects.p1.title": "Continuously Scalable Conversion Ratio (CSCR) Power Converter for Stacked Systems",
    "projects.p1.body": "Designing a CSCR-based mismatch compensator for stacked voltage-domain systems, with automatic source/sink mode selection to maintain high efficiency under large current mismatch.",
    "projects.p2.title": "HBM Voltage-Stacked Power Delivery &amp; Memory-System Modeling",
    "projects.p2.body": "Built a DRAMSim3/Accel-Sim&ndash;based framework to analyze per-channel power, latency, and current mismatch in HBM2/HBM3 systems under GPU workloads. Proposed a voltage-stacked HBM power delivery architecture and load-mismatch metrics, identifying up to 113&nbsp;mA of inter-channel current mismatch and evaluating TSV / power-efficiency trade-offs.",
    "projects.p3.title": "Bidirectional SIMO Mismatch Compensator for Stacked Voltage-Domain Systems",
    "projects.p3.body": "Invented a bidirectional zero-current detector (Bi-ZCD) for source/sink current regulation in voltage-stacked systems, achieving 98.5% peak efficiency and 82% efficiency under 360&nbsp;mA load mismatch.",
    "projects.p3.pub": "&rarr; Published as VSIMO, IEEE VLSI Symposium 2026",
    "projects.p4.title": "Computational DLDO-Assisted Buck DC&ndash;DC Converter",
    "projects.p4.body": "Designed a DLDO-assisted buck converter with one-step computational droop compensation and DLDO-controlled current handover, achieving 68-mV droop, 112-ns settling time, and 95.5% peak efficiency for 1A/0.8ns load transients.",
    "projects.p4.pub": "&rarr; Published in IEEE SSCL 2025",
    "projects.p5.title": "Computational DLDO with Load-Dependent Feedback and Fast DVS",
    "projects.p5.body": "Designed a rising-edge computational DLDO with load-dependent feedback and DVS computation, achieving a 0.15-ps FoM, 25-mV/ns DVS rate, and low ripple across a 1-to-1050&nbsp;mA load range.",
    "projects.p5.pub": "&rarr; Published at IEEE VLSI Symposium 2026; invited manuscript, IEEE JSSC 2027",
    "projects.p6.title": "Dynamic Load Regulation Limit Model for Digital LDOs",
    "projects.p6.body": "Established an analytical model of dynamic load regulation for commonly used DLDO architectures, analyzing the impact of design parameters and providing optimal design points for power switch sizing.",
    "projects.p6.pub": "&rarr; Published in IEEE TVLSI 2024",
    "projects.p7.title": "Ultrasound Range Finder Analog Front End",
    "projects.p7.tag": "Course Project",
    "projects.p7.body": "Designed a 9-setting programmable-gain amplifier using replica-based common-mode feedback, and developed the strong-arm comparator, track-and-hold, and capacitor-based DAC for a 125&nbsp;kHz 8-bit SAR ADC.",

    "publications.eyebrow": "04 &mdash; Writing",
    "publications.title": "Publications",
    "publications.patents": "Patents",

    "photo.eyebrow": "05 &mdash; Outside the lab",
    "photo.title": "Photography",
    "photo.lede": "A few frames outside the cleanroom. Placeholder art below &mdash; drop real photos into <code>assets/photography/</code> and swap the tiles.",
    "photo.item1": "Travel",
    "photo.item2": "Street",
    "photo.item3": "Nature",
    "photo.item4": "Architecture",
    "photo.item5": "Long Exposure",
    "photo.item6": "Film",
    "photo.video.title": "Video",
    "photo.video.lede": "A short video I made.",

    "experience.eyebrow": "06 &mdash; Industry",
    "experience.title": "Experience",
    "experience.e1.title": "Circuit Design Intern &mdash; DRAM Design Lab, Samsung",
    "experience.e1.body": "Designed a fully integrated voltage regulator for the LPDDR6 Built-of-Test (LP6BOT) chip, and a three-path regulation architecture (feedback, PSR feedforward, transient feedforward) achieving &gt;20&nbsp;dB PSRR at 100&nbsp;MHz. Coordinated the chip power delivery network layout in Samsung 14nm CMOS.",
    "experience.e2.title": "Graduate Technical Intern &mdash; Intel",
    "experience.e2.body": "Developed SPICE/Verilog-A models for adaptive clocking, clock throttling, and switched-capacitor load balancing; created a critical-path replica circuit with background calibration for setup violation detection in Intel 16nm CMOS.",
    "experience.e3.title": "Mixed-Signal Design Engineer Intern &mdash; Ambarella",
    "experience.e3.body": "Performed low-power standard-cell schematic and layout design in Samsung 4nm FinFET, and developed an automated Python-based .lib generation flow for digital place-and-route.",
    "experience.e4.title": "Analog and System IC Engineer &mdash; Chip Dance Technology",
    "experience.e4.body": "Led a True Wireless Stereo lithium battery charging chip architecture, taped out in GF 180nm. Designed a sub-threshold BGR with digital trimming DAC and a PVT-tolerant hysteresis comparator, and an LDO-based linear battery charger for 5V-to-4.2V regulation (first inventor on related patent).",
    "experience.teaching": "Teaching",
    "experience.t1": "Teaching Assistant, Modern Power Management IC Design (ELEN 6920) &mdash; Fall 2022 / 2023 / 2024",
    "experience.t2": "Teaching Assistant, VLSI Design Lab (ELEN 6350) &mdash; Spring 2025",

    "contact.eyebrow": "07 &mdash; Say hello",
    "contact.title": "Contact",

    "footer.text": "&copy; 2026 Yichen Xu. Built with plain HTML/CSS/JS, hosted on GitHub Pages."
  },

  zh: {
    "nav.home": "首页",
    "nav.about": "关于我",
    "nav.journey": "成长之路",
    "nav.chips": "芯片墙",
    "nav.projects": "项目",
    "nav.publications": "论文发表",
    "nav.photography": "摄影",
    "nav.experience": "经历",
    "nav.contact": "联系方式",

    "hero.photoPlaceholder": "替换为你的照片<br>(assets/headshot.jpg)",
    "hero.name": "徐一宸",
    "hero.eyebrow": "哥伦比亚大学 &middot; 电子工程 &middot; 博士候选人",
    "hero.tagline": "电源管理芯片设计师，业余视频制作者。",
    "hero.text": "我从事面向现代 SoC 平台与新兴 AI 硬件系统的电源管理电路设计 &mdash; 包括计算式数字 LDO（DLDO）、SIMO 多路输出 DC&ndash;DC 转换器、开关电容转换器，以及面向高带宽内存系统的电压堆叠式电源传输。导师是哥伦比亚大学的 Mingoo Seok 教授。实验室之外，这个页面也收录了我流过片的芯片，以及一些随手拍的照片。",
    "hero.linkEmail": "邮箱",

    "home.eyebrow": "浏览",
    "home.title": "站点导览",
    "home.about.desc": "教育背景、研究方向与荣誉奖项。",
    "home.journey.desc": "自贡 &rarr; 成都 &rarr; 苏州 &rarr; 上海 &rarr; 纽约 &rarr; 圣何塞。",
    "home.chips.desc": "每次流片的芯片照片与测试板。",
    "home.projects.desc": "从课程项目到最新流片的研究项目。",
    "home.publications.desc": "论文与专利。",
    "home.photography.desc": "实验室之外拍的一些照片。",
    "home.experience.desc": "实习、工业界经历与助教经历。",

    "visitors.eyebrow": "实时",
    "visitors.title": "访客地图",
    "visitors.lede": "一份实时的小地图，展示此刻正在浏览这个网站的人来自哪里。",

    "about.eyebrow": "01 &mdash; 关于",
    "about.title": "关于我",
    "about.education.title": "教育背景",
    "about.education.columbia": "<strong>哥伦比亚大学</strong> &mdash; 电子工程硕士 &amp; 博士（导师：Mingoo Seok）<span class=\"meta\">2021&ndash;2027</span>",
    "about.education.uestc": "<strong>电子科技大学（UESTC）</strong> &mdash; 电子工程学士<span class=\"meta\">2016&ndash;2020</span>",
    "about.interests.title": "研究方向",
    "about.interests.body": "<li>计算式数字 LDO（DLDO）、DC&ndash;DC SIMO 转换器、开关电容（SC）电源转换器</li><li>压降检测、DVFS，以及电源传输网络设计</li>",
    "about.honors.title": "荣誉奖项",
    "about.honors.body": "<li>哥伦比亚大学理学硕士优秀奖（前 5%）</li><li>电子科技大学优秀学生奖学金</li><li>2024 IBM AI Symposium 最佳海报奖</li>",

    "journey.sectionTitle": "成长之路",
    "journey.lede": "自贡 &rarr; 成都 &rarr; 苏州 &rarr; 上海 &rarr; 纽约 &rarr; 圣何塞。",
    "journey.s1.city": "自贡",
    "journey.s1.region": "中国 四川",
    "journey.s1.period": "起点",
    "journey.s1.body": "在自贡出生长大 &mdash; 这是四川的一座小型工业城市，以盐业、恐龙化石和灯会闻名。这里也是我第一次因为好奇拆开东西、想搞明白它们如何运转的地方。",
    "journey.s2.city": "成都",
    "journey.s2.region": "中国 四川",
    "journey.s2.period": "2016 &ndash; 2020",
    "journey.s2.body": "为了在电子科技大学（UESTC）读电子工程本科，搬到了省会成都 &mdash; 离家大约 180&nbsp;公里，却是第一次真正意义上离开家。也是从这里开始，电路不再只是一门课，而变成了我真正想做的事。",
    "journey.s3.city": "苏州",
    "journey.s3.region": "中国 江苏",
    "journey.s3.period": "2019",
    "journey.s3.body": "2019 年在苏州待过一段时间 &mdash; [告诉我你当时在那里做什么，我会把这里补充完整]。",
    "journey.s4.city": "上海",
    "journey.s4.region": "中国",
    "journey.s4.period": "2020 &ndash; 2021",
    "journey.s4.body": "加入芯动科技（Chip Dance Technology，一家创业公司）担任模拟与系统芯片工程师，主导了一款 TWS 真无线立体声电池充电芯片的架构设计，并在 GF 180nm 工艺下完成流片 &mdash; 第一次亲眼看到自己设计的芯片从原理图变成真正的硅片。",
    "journey.s5.city": "纽约",
    "journey.s5.region": "美国",
    "journey.s5.period": "2021 &ndash; 至今",
    "journey.s5.body": "从上海出发，跨越约 11,700&nbsp;公里，来到哥伦比亚大学攻读硕士与博士。换了国家，换了一整套新的仪器和语言，问题却没变：当周围一切都在高速开关时，怎么让电源既干净又高效？",
    "journey.s6.city": "圣何塞",
    "journey.s6.region": "美国 加利福尼亚州",
    "journey.s6.period": "2026 年夏",
    "journey.s6.body": "向西约 4,100&nbsp;公里，来到三星 DRAM 设计实验室做电路设计实习 &mdash; 从曼哈顿的教室，来到了硅谷存储产业的中心。",

    "chips.eyebrow": "02 &mdash; 硅片",
    "chips.title": "芯片墙",
    "chips.lede": "多年流片与实验室工作中的封装芯片与裸片照片。",
    "chips.packaged.title": "封装芯片",
    "chips.packaged.item": "封装芯片",
    "chips.bare.title": "裸片",
    "chips.bare.item": "裸片",
    "chips.tag": "占位图",

    "projects.eyebrow": "03 &mdash; 研究",
    "projects.title": "项目",
    "projects.p1.title": "面向堆叠系统的连续可调转换比（CSCR）电源转换器",
    "projects.p1.body": "为电压堆叠系统设计基于 CSCR 的失配补偿器，具备自动源/汇模式切换能力，在大电流失配下依然维持高效率。",
    "projects.p2.title": "HBM 电压堆叠电源传输与存储系统建模",
    "projects.p2.body": "搭建了基于 DRAMSim3/Accel-Sim 的分析框架，用于研究 GPU 负载下 HBM2/HBM3 系统各通道的功耗、延迟与电流失配。提出了电压堆叠式 HBM 电源传输架构及负载失配指标，发现通道间电流失配最高可达 113&nbsp;mA，并评估了 TSV 与功耗效率之间的取舍。",
    "projects.p3.title": "面向电压堆叠系统的双向 SIMO 失配补偿器",
    "projects.p3.body": "发明了用于电压堆叠系统源/汇电流调节的双向零电流检测器（Bi-ZCD），在 360&nbsp;mA 负载失配下实现 98.5% 峰值效率与 82% 的效率表现。",
    "projects.p3.pub": "&rarr; 以 VSIMO 发表于 IEEE VLSI Symposium 2026",
    "projects.p4.title": "计算式 DLDO 辅助 Buck DC&ndash;DC 转换器",
    "projects.p4.body": "设计了一款采用单步计算式压降补偿与 DLDO 控制电流切换的 DLDO 辅助 Buck 转换器，在 1A/0.8ns 负载瞬变下实现 68-mV 压降、112-ns 建立时间与 95.5% 峰值效率。",
    "projects.p4.pub": "&rarr; 发表于 IEEE SSCL 2025",
    "projects.p5.title": "具备负载相关反馈与快速 DVS 的计算式 DLDO",
    "projects.p5.body": "设计了一款采用上升沿计算与负载相关反馈的 DLDO，实现 0.15-ps 的品质因数（FoM）、25-mV/ns 的 DVS 速率，并在 1-to-1050&nbsp;mA 负载范围内保持低纹波。",
    "projects.p5.pub": "&rarr; 发表于 IEEE VLSI Symposium 2026；受邀投稿 IEEE JSSC 2027",
    "projects.p6.title": "数字 LDO 动态负载调节极限模型",
    "projects.p6.body": "为常见的 DLDO 架构建立了动态负载调节的解析模型，分析了设计参数的影响，并给出了功率开关设计的最优点。",
    "projects.p6.pub": "&rarr; 发表于 IEEE TVLSI 2024",
    "projects.p7.title": "超声测距模拟前端",
    "projects.p7.tag": "课程项目",
    "projects.p7.body": "设计了一款基于复制式共模反馈、具有 9 档增益的可编程增益放大器，并为 125&nbsp;kHz 8-bit SAR ADC 开发了 strong-arm 比较器、采样保持电路与电容式 DAC。",

    "publications.eyebrow": "04 &mdash; 论文",
    "publications.title": "论文发表",
    "publications.patents": "专利",

    "photo.eyebrow": "05 &mdash; 实验室之外",
    "photo.title": "摄影作品",
    "photo.lede": "一些实验室之外拍的照片。下面是占位图 &mdash; 把真实照片放进 <code>assets/photography/</code> 并替换对应的格子即可。",
    "photo.item1": "旅行",
    "photo.item2": "街拍",
    "photo.item3": "自然",
    "photo.item4": "建筑",
    "photo.item5": "长曝光",
    "photo.item6": "胶片",
    "photo.video.title": "视频",
    "photo.video.lede": "一段我拍的短视频。",

    "experience.eyebrow": "06 &mdash; 工业界经历",
    "experience.title": "经历",
    "experience.e1.title": "电路设计实习生 &mdash; 三星 DRAM 设计实验室",
    "experience.e1.body": "为 LPDDR6 Built-of-Test（LP6BOT）芯片设计了全集成电压调节器，以及一套三路调节架构（反馈、PSR 前馈、瞬态前馈），在 100&nbsp;MHz 下实现 &gt;20&nbsp;dB PSRR。负责协调芯片电源传输网络在三星 14nm 工艺下的版图设计。",
    "experience.e2.title": "研究生技术实习生 &mdash; Intel",
    "experience.e2.body": "为自适应时钟、时钟节流与开关电容负载均衡开发了 SPICE/Verilog-A 模型；在 Intel 16nm 工艺下设计了带背景校准的关键路径复制电路，用于建立时间违例检测。",
    "experience.e3.title": "混合信号设计工程师实习生 &mdash; Ambarella",
    "experience.e3.body": "在三星 4nm FinFET 工艺下完成了低功耗标准单元的原理图与版图设计，并开发了基于 Python 的自动化 .lib 文件生成流程，用于数字布局布线。",
    "experience.e4.title": "模拟与系统芯片工程师 &mdash; 芯动科技（Chip Dance Technology）",
    "experience.e4.body": "主导了一款 TWS 真无线立体声锂电池充电芯片的架构设计，在 GF 180nm 工艺下完成流片。设计了带数字修调 DAC 的亚阈值带隙基准（BGR）与 PVT 容忍迟滞比较器，以及一款支持 5V 转 4.2V 的 LDO 线性电池充电器（相关专利第一发明人）。",
    "experience.teaching": "教学经历",
    "experience.t1": "现代电源管理集成电路设计（ELEN 6920）助教 &mdash; 2022 / 2023 / 2024 秋季学期",
    "experience.t2": "VLSI 设计实验课（ELEN 6350）助教 &mdash; 2025 春季学期",

    "contact.eyebrow": "07 &mdash; 联系我",
    "contact.title": "联系方式",

    "footer.text": "&copy; 2026 Yichen Xu. 使用 HTML/CSS/JS 构建，托管于 GitHub Pages。"
  }
};

(function () {
  function applyLanguage(lang) {
    var dict = I18N[lang] || I18N.en;
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      if (dict[key] !== undefined) {
        el.innerHTML = dict[key];
      }
    });
    document.documentElement.setAttribute("lang", lang === "zh" ? "zh" : "en");
    document.getElementById("langEn").classList.toggle("active", lang === "en");
    document.getElementById("langZh").classList.toggle("active", lang === "zh");
    try { localStorage.setItem("site-lang", lang); } catch (e) {}
    document.dispatchEvent(new CustomEvent("site:langchange", { detail: { lang: lang } }));
  }

  document.addEventListener("DOMContentLoaded", function () {
    var saved = "en";
    try { saved = localStorage.getItem("site-lang") || "en"; } catch (e) {}
    if (saved !== "en") applyLanguage(saved);

    document.getElementById("langEn").addEventListener("click", function () { applyLanguage("en"); });
    document.getElementById("langZh").addEventListener("click", function () { applyLanguage("zh"); });

    var here = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      var href = a.getAttribute("href");
      a.classList.toggle("active", href === here || (here === "" && href === "index.html"));
    });

    var navToggleBtn = document.getElementById("navToggleBtn");
    var navLinks = document.getElementById("navLinks");
    if (navToggleBtn && navLinks) {
      navToggleBtn.addEventListener("click", function () {
        navLinks.classList.toggle("open");
      });
    }
  });
})();
