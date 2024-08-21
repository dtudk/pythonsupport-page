document.addEventListener("DOMContentLoaded", function () {
  var originalOffsetTop = null;
  var activeVideo = null;
  var stickyClass = "sticky-video";

  // Function to update the active video
  function updateActiveVideo() {
    const activeElement = document.activeElement;
    if (activeElement.tagName === "IFRAME" && activeElement !== activeVideo) {
      if (activeVideo) {
        activeVideo.classList.remove(stickyClass); // Remove sticky class from previous video
      }
      activeVideo = activeElement;
      originalOffsetTop =
        activeVideo.getBoundingClientRect().top + window.scrollY;
      originalOffsetBottom =
        activeVideo.getBoundingClientRect().bottom + window.scrollY;
    }
  }

  // Function to handle the sticky behavior
  function handleStickyBehavior() {
    if (activeVideo) {
      if (originalOffsetBottom < window.scrollY) {
        // Check if video is above the viewport
        activeVideo.classList.add(stickyClass);
      } else if (originalOffsetTop - window.innerHeight > window.scrollY) {
        // Check if video is below the viewport
        activeVideo.classList.add(stickyClass);
      } else {
        activeVideo.classList.remove(stickyClass);
      }
    }
  }

  // Periodically check for the active video
  setInterval(updateActiveVideo, 100);

  // Scroll event to handle sticky behavior
  window.addEventListener("scroll", handleStickyBehavior);
});
