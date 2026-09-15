/* ------------------------------------------------------------
   Interactive world map for the Journey page.
   Draws a simplified world land silhouette (Natural Earth 110m,
   via world-atlas + topojson-client, both self-hosted in
   assets/) and plots markers for each .journey-stop element
   found in the page (reads data-lat / data-lon / id from the
   DOM, so the map and the story cards share one source of truth).
   Click a marker to jump to its story card; hover for a tooltip.
   ------------------------------------------------------------ */

(function () {
  var SVG_NS = "http://www.w3.org/2000/svg";
  var W = 960, H = 480;

  function project(lon, lat) {
    var x = (lon + 180) * (W / 360);
    var y = (90 - lat) * (H / 180);
    return [x, y];
  }

  function ringToPath(ring) {
    var d = "";
    for (var i = 0; i < ring.length; i++) {
      var p = project(ring[i][0], ring[i][1]);
      d += (i === 0 ? "M" : "L") + p[0].toFixed(2) + "," + p[1].toFixed(2) + " ";
    }
    return d + "Z ";
  }

  function geometryToPath(geom) {
    var d = "";
    if (geom.type === "Polygon") {
      geom.coordinates.forEach(function (ring) { d += ringToPath(ring); });
    } else if (geom.type === "MultiPolygon") {
      geom.coordinates.forEach(function (poly) {
        poly.forEach(function (ring) { d += ringToPath(ring); });
      });
    }
    return d;
  }

  function readStops() {
    var els = Array.prototype.slice.call(document.querySelectorAll(".journey-stop"));
    els.sort(function (a, b) {
      return (+a.getAttribute("data-order") || 0) - (+b.getAttribute("data-order") || 0);
    });
    return els.map(function (el) {
      return {
        id: el.id,
        lat: parseFloat(el.getAttribute("data-lat")),
        lon: parseFloat(el.getAttribute("data-lon")),
        el: el
      };
    });
  }

  function stopLabel(stop) {
    var h3 = stop.el.querySelector("h3");
    var meta = stop.el.querySelector(".project-meta");
    var city = h3 ? h3.textContent.trim() : stop.id;
    var period = meta ? meta.textContent.trim() : "";
    return period ? city + " — " + period : city;
  }

  function buildMap(svg, landGeoJSON, stops) {
    svg.innerHTML = "";
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);

    // ocean background
    var bg = document.createElementNS(SVG_NS, "rect");
    bg.setAttribute("x", 0); bg.setAttribute("y", 0);
    bg.setAttribute("width", W); bg.setAttribute("height", H);
    bg.setAttribute("class", "map-ocean");
    svg.appendChild(bg);

    // land
    var landGroup = document.createElementNS(SVG_NS, "g");
    landGroup.setAttribute("class", "map-land-group");
    (landGeoJSON.features || [landGeoJSON]).forEach(function (feature) {
      var path = document.createElementNS(SVG_NS, "path");
      path.setAttribute("d", geometryToPath(feature.geometry));
      path.setAttribute("class", "map-land");
      landGroup.appendChild(path);
    });
    svg.appendChild(landGroup);

    // connecting route
    var routeD = "";
    stops.forEach(function (s, i) {
      var p = project(s.lon, s.lat);
      routeD += (i === 0 ? "M" : "L") + p[0].toFixed(2) + "," + p[1].toFixed(2) + " ";
    });
    var route = document.createElementNS(SVG_NS, "path");
    route.setAttribute("d", routeD);
    route.setAttribute("class", "map-route");
    svg.appendChild(route);

    // markers
    stops.forEach(function (s, i) {
      var p = project(s.lon, s.lat);
      var a = document.createElementNS(SVG_NS, "a");
      a.setAttribute("href", "#" + s.id);
      a.setAttribute("class", "map-marker");
      a.setAttribute("data-target", s.id);

      var halo = document.createElementNS(SVG_NS, "circle");
      halo.setAttribute("cx", p[0]); halo.setAttribute("cy", p[1]);
      halo.setAttribute("r", 9);
      halo.setAttribute("class", "map-marker-halo");

      var dot = document.createElementNS(SVG_NS, "circle");
      dot.setAttribute("cx", p[0]); dot.setAttribute("cy", p[1]);
      dot.setAttribute("r", 4.5);
      dot.setAttribute("class", "map-marker-dot");

      var title = document.createElementNS(SVG_NS, "title");
      title.textContent = (i + 1) + ". " + stopLabel(s);

      a.appendChild(halo);
      a.appendChild(dot);
      a.appendChild(title);
      svg.appendChild(a);
    });

    return stops;
  }

  function wireActiveState(svg, stops) {
    if (!("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var marker = svg.querySelector('.map-marker[data-target="' + entry.target.id + '"]');
        if (!marker) return;
        marker.classList.toggle("is-active", entry.isIntersecting);
      });
    }, { rootMargin: "-40% 0px -40% 0px", threshold: 0 });
    stops.forEach(function (s) { io.observe(s.el); });
  }

  function refreshTooltips(svg, stops) {
    stops.forEach(function (s, i) {
      var marker = svg.querySelector('.map-marker[data-target="' + s.id + '"]');
      if (!marker) return;
      var title = marker.querySelector("title");
      if (title) title.textContent = (i + 1) + ". " + stopLabel(s);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var svg = document.getElementById("journeyMap");
    if (!svg || typeof topojson === "undefined") return;

    var stops = readStops();
    if (!stops.length) return;

    fetch("assets/data/land-110m.json")
      .then(function (r) { return r.json(); })
      .then(function (topo) {
        var land = topojson.feature(topo, topo.objects.land);
        buildMap(svg, land, stops);
        wireActiveState(svg, stops);

        document.addEventListener("site:langchange", function () {
          refreshTooltips(svg, stops);
        });
      })
      .catch(function () {
        svg.closest(".journey-map-wrap").style.display = "none";
      });
  });
})();
