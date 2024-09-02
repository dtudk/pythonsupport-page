// var userLevel = userLevel || 'package-managed.html';

let userLevel;

function PyS_isOperatingSytem() {
  const userAgent = navigator.userAgent.toLowerCase();
  console.log("User Agent:", userAgent); // Debugging line
  if (userAgent.indexOf("android") != -1) return false;
  if (userAgent.indexOf("iphone") != -1) return false;
  if (userAgent.indexOf("ipad") != -1) return false;
  if (userAgent.indexOf("win") != -1) return "windows";
  if (userAgent.indexOf("mac") != -1) return "macos";
  if (userAgent.indexOf("linux") != -1) return "linux";
  return false;
}

function PyS_osSelector(os) {
  const baseUrl = getBaseUrl();
  console.log("Base URL:", baseUrl); // Debugging line
  if (os === "linux") {
    window.location.href = `${baseUrl}install/${os}/manual.html`;
  } else {
    window.location.href = `${baseUrl}install/${os}/automated.html`;
  }
}

function PyS_redirectUser(UserLevel) {
  let os = PyS_isOperatingSytem();
  userLevel = UserLevel;
  console.log("Operating System:", os); // Debugging line
  if (!os) {
    PyS_toggleBanner(); // Show OS selector
  } else {
    PyS_osSelector(os);
  }
}

function getBaseUrl() {
  // Get the path and remove the last segment
  let pathArray = window.location.pathname.split("/");
  pathArray.pop(); // Remove the last segment (current file name)

  // Join the remaining segments to form the new path
  let newPathname = pathArray.join("/");

  // Handle the case of local file URLs
  let origin = window.location.origin;
  if (origin === "null") {
    origin = `file://${pathArray.slice(0, 2).join("/")}`; // Construct the file origin manually
    newPathname = "/" + pathArray.slice(2).join("/"); // Adjust the pathname accordingly
  }

  console.log("Constructed Path:", newPathname); // Debugging line
  return origin + newPathname + "/";
}

function PyS_toggleBanner() {
  const bannerContainer = document.getElementById("bannerContainer");
  const topBanner = document.querySelector(".topBanner");
  const bottomBanner = document.querySelector(".bottomBanner");
  const osSelector = document.getElementById("PyS_osSelector");

  if (bannerContainer && topBanner && bottomBanner && osSelector) {
    bannerContainer.classList.toggle("collapsed");
    // Delay the execution by 0.5 seconds (500 milliseconds)
    setTimeout(() => {
      topBanner.classList.toggle("hidden");
      bottomBanner.classList.toggle("hidden");
      osSelector.classList.toggle("hidden");
      bannerContainer.classList.toggle("collapsed");
    }, 500);
  } else {
    console.error("One or more elements not found");
  }
}

function PyS_noRed() {
  const bottomBanner = document.querySelector(".bottomBanner");
  if (bottomBanner) {
    bottomBanner.classList.toggle("hidden");
  } else {
    console.error("bottomBanner element not found");
  }
}

document.addEventListener("DOMContentLoaded", function () {
  var images = document.getElementsByTagName("img");
  var childImage;
  var overlay = document.createElement("div");
  overlay.className = "zoom-overlay";
  document.body.appendChild(overlay);

  for (var i = 0; i < images.length; i++) {
    images[i].addEventListener("click", function () {
      event.preventDefault(); // Prevent the default behavior of the image or link
      let clonedImage = this.cloneNode(true);
      clonedImage.classList.toggle("zoomed-in-image");
      if (overlay.firstChild) {
        overlay.removeChild(overlay.firstChild);
      }
      overlay.appendChild(clonedImage);
      childImage = overlay.childNodes[0];
      clonedImage.classList.toggle("zoomed-in-image-display");
      overlay.classList.toggle("zoom-overlay-display");
    });
  }

  overlay.addEventListener("click", function () {
    overlay.classList.toggle("zoom-overlay-display");
    childImage.classList.toggle("zoomed-in-image-display");
  });

  document.body.addEventListener("keydown", function (e) {
    if (e.key == "Escape") {
      if (overlay.classList.contains("zoom-overlay-display")) {
        overlay.classList.toggle("zoom-overlay-display");
        childImage.classList.toggle("zoomed-in-image-display");
      }
    }
  });
});
