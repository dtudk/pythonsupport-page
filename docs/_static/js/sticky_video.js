document.addEventListener("DOMContentLoaded", function () {
    var videoContainer = document.querySelector("iframe[src*='panopto']");
    var originalOffsetTop = videoContainer.getBoundingClientRect().top + window.pageYOffset;
    var stickyClass = "sticky-video";

    window.addEventListener("scroll", function () {
        if (window.pageYOffset > originalOffsetTop) {
            videoContainer.classList.add(stickyClass);
        } else {
            videoContainer.classList.remove(stickyClass);
        }
    });
});

