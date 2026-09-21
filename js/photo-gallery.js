// Place-card expand/collapse (via a button, not hover) + click-to-enlarge lightbox
// with swipe support for the Photography page.
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var lightbox = document.getElementById("photoLightbox");
    var lightboxImg = document.getElementById("lightboxImg");
    var lightboxClose = document.getElementById("lightboxClose");
    var lightboxPrev = document.getElementById("lightboxPrev");
    var lightboxNext = document.getElementById("lightboxNext");
    var lightboxHint = document.getElementById("lightboxHint");

    var currentGallery = [];
    var currentIndex = -1;

    function updateNavVisibility() {
      var multi = currentGallery.length > 1;
      if (lightboxPrev) lightboxPrev.hidden = !multi;
      if (lightboxNext) lightboxNext.hidden = !multi;
      if (lightboxHint) lightboxHint.hidden = !multi;
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

      // Swipe left/right to move through the gallery on touch devices. This is the
      // primary way to browse on mobile — the prev/next buttons are a backup, not
      // the only way in. A swipe that's mostly vertical is left alone so it doesn't
      // fight with the page or an accidental scroll.
      var touchStartX = 0, touchStartY = 0, touchTracking = false;
      var SWIPE_THRESHOLD = 40; // px
      var SWIPE_RATIO = 1.2; // how much more horizontal than vertical movement must be

      lightbox.addEventListener("touchstart", function (e) {
        if (e.touches.length !== 1) return;
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        touchTracking = true;
      }, { passive: true });

      lightbox.addEventListener("touchend", function (e) {
        if (!touchTracking) return;
        touchTracking = false;
        var touch = e.changedTouches[0];
        var dx = touch.clientX - touchStartX;
        var dy = touch.clientY - touchStartY;
        if (Math.abs(dx) < SWIPE_THRESHOLD) return;
        if (Math.abs(dx) < Math.abs(dy) * SWIPE_RATIO) return;
        if (dx < 0) showIndex(currentIndex + 1);
        else showIndex(currentIndex - 1);
      }, { passive: true });
    }

    // Photo rows (Editorial Index): each is a native <details> element, so
    // expand/collapse of the thumbnail strip is free, accessible browser behavior —
    // clicking anywhere in the row's <summary> toggles it open. The cover photo
    // inside the summary is the one exception: clicking it should open the
    // lightbox instead of toggling the row, so its handler stops that click from
    // reaching the native toggle.
    document.querySelectorAll(".photo-row").forEach(function (row) {
      var cover = row.querySelector(".photo-cover");
      var thumbs = Array.prototype.slice.call(row.querySelectorAll(".photo-thumb"));

      var coverItem = null;
      if (cover) {
        var coverImg = cover.querySelector("img");
        coverItem = { src: cover.getAttribute("data-full"), alt: coverImg ? coverImg.alt : "" };
      }
      var thumbItems = thumbs.map(function (btn) {
        var img = btn.querySelector("img");
        return { src: btn.getAttribute("data-full"), alt: img ? img.alt : "" };
      });
      var gallery = coverItem ? [coverItem].concat(thumbItems) : thumbItems;
      var thumbOffset = coverItem ? 1 : 0;

      thumbs.forEach(function (btn, i) {
        btn.addEventListener("click", function () {
          openLightbox(gallery, i + thumbOffset);
        });
      });

      if (cover) {
        cover.addEventListener("click", function (e) {
          e.preventDefault();
          e.stopPropagation();
          openLightbox(gallery, 0);
        });
        cover.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            e.stopPropagation();
            openLightbox(gallery, 0);
          }
        });
      }
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
  });
})();
