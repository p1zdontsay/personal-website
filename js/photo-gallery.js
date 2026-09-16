// Place-card hover/tap expand + click-to-enlarge lightbox for the Photography page.
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var lightbox = document.getElementById("photoLightbox");
    var lightboxImg = document.getElementById("lightboxImg");
    var lightboxClose = document.getElementById("lightboxClose");

    function openLightbox(src, alt) {
      if (!lightbox || !lightboxImg) return;
      lightboxImg.src = src;
      lightboxImg.alt = alt || "";
      lightbox.classList.add("is-open");
    }
    function closeLightbox() {
      if (!lightbox || !lightboxImg) return;
      lightbox.classList.remove("is-open");
      lightboxImg.src = "";
    }

    if (lightbox) {
      lightbox.addEventListener("click", function (e) {
        if (e.target === lightbox || e.target === lightboxClose) closeLightbox();
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") closeLightbox();
      });
    }

    // Thumbnails: click to view a larger version.
    document.querySelectorAll(".place-thumb").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var full = btn.getAttribute("data-full");
        var img = btn.querySelector("img");
        if (full) openLightbox(full, img ? img.alt : "");
      });
    });

    // Cover: click/tap toggles the thumbnail row open (hover already expands it via CSS
    // on pointer devices; this covers touch and keyboard use).
    document.querySelectorAll(".place-card").forEach(function (card) {
      var cover = card.querySelector(".place-cover");
      if (!cover) return;
      cover.addEventListener("click", function () {
        var isOpen = card.classList.contains("is-open");
        document.querySelectorAll(".place-card.is-open").forEach(function (c) {
          if (c !== card) c.classList.remove("is-open");
        });
        card.classList.toggle("is-open", !isOpen);
      });
    });

    // Thumbnail row: hovering near the left/right edge auto-scrolls that direction,
    // so the rest of the photos scroll into view without a manual scrollbar drag.
    var EDGE_ZONE = 56; // px from the edge that triggers auto-scroll
    var MAX_SPEED = 9; // px per animation frame at the very edge

    document.querySelectorAll(".place-thumbs").forEach(function (row) {
      var rafId = null;
      var speed = 0;

      function step() {
        if (speed !== 0) {
          row.scrollLeft += speed;
          rafId = requestAnimationFrame(step);
        } else {
          rafId = null;
        }
      }

      function updateSpeed(e) {
        var rect = row.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var distRight = rect.width - x;
        var distLeft = x;

        if (row.scrollWidth <= row.clientWidth) {
          speed = 0;
        } else if (distRight < EDGE_ZONE) {
          speed = MAX_SPEED * (1 - distRight / EDGE_ZONE);
        } else if (distLeft < EDGE_ZONE) {
          speed = -MAX_SPEED * (1 - distLeft / EDGE_ZONE);
        } else {
          speed = 0;
        }

        if (speed !== 0 && rafId === null) rafId = requestAnimationFrame(step);
      }

      row.addEventListener("mousemove", updateSpeed);
      row.addEventListener("mouseleave", function () {
        speed = 0;
      });
    });
  });
})();
