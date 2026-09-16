// Place-card hover/tap expand + click-to-enlarge lightbox for the Photography page.
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var lightbox = document.getElementById("photoLightbox");
    var lightboxImg = document.getElementById("lightboxImg");
    var lightboxClose = document.getElementById("lightboxClose");
    var lightboxPrev = document.getElementById("lightboxPrev");
    var lightboxNext = document.getElementById("lightboxNext");

    var currentGallery = [];
    var currentIndex = -1;

    function updateNavVisibility() {
      var multi = currentGallery.length > 1;
      if (lightboxPrev) lightboxPrev.hidden = !multi;
      if (lightboxNext) lightboxNext.hidden = !multi;
    }

    function showIndex(i) {
      if (!currentGallery.length) return;
      currentIndex = (i + currentGallery.length) % currentGallery.length;
      var item = currentGallery[currentIndex];
      lightboxImg.src = item.src;
      lightboxImg.alt = item.alt || "";
    }

    function openLightbox(gallery, index) {
      if (!lightbox || !lightboxImg) return;
      currentGallery = gallery;
      showIndex(index);
      updateNavVisibility();
      lightbox.classList.add("is-open");
    }
    function closeLightbox() {
      if (!lightbox || !lightboxImg) return;
      lightbox.classList.remove("is-open");
      lightboxImg.src = "";
      currentGallery = [];
      currentIndex = -1;
    }

    if (lightbox) {
      lightbox.addEventListener("click", function (e) {
        if (e.target === lightbox || e.target === lightboxClose) closeLightbox();
      });
      if (lightboxPrev) lightboxPrev.addEventListener("click", function () { showIndex(currentIndex - 1); });
      if (lightboxNext) lightboxNext.addEventListener("click", function () { showIndex(currentIndex + 1); });
      document.addEventListener("keydown", function (e) {
        if (!lightbox.classList.contains("is-open")) return;
        if (e.key === "Escape") closeLightbox();
        else if (e.key === "ArrowLeft") showIndex(currentIndex - 1);
        else if (e.key === "ArrowRight") showIndex(currentIndex + 1);
      });
    }

    // Thumbnails: click to view a larger version, with prev/next through the rest of
    // that place's photos.
    document.querySelectorAll(".place-thumbs").forEach(function (row) {
      var thumbs = Array.prototype.slice.call(row.querySelectorAll(".place-thumb"));
      var gallery = thumbs.map(function (btn) {
        var img = btn.querySelector("img");
        return { src: btn.getAttribute("data-full"), alt: img ? img.alt : "" };
      });
      thumbs.forEach(function (btn, i) {
        btn.addEventListener("click", function () {
          openLightbox(gallery, i);
        });
      });
    });

    // Chip Gallery tiles: click to view a larger version, with prev/next through the
    // rest of that same grid (Packaged, Bare Die, etc.).
    document.querySelectorAll(".gallery-grid").forEach(function (grid) {
      var thumbs = Array.prototype.slice.call(grid.querySelectorAll(".tile-thumb"));
      var gallery = thumbs.map(function (btn) {
        var img = btn.querySelector("img");
        return { src: btn.getAttribute("data-full"), alt: img ? img.alt : "" };
      });
      thumbs.forEach(function (btn, i) {
        btn.addEventListener("click", function () {
          openLightbox(gallery, i);
        });
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
