document.addEventListener("DOMContentLoaded", function () {
  // Gets the #{id} from the url
  const hash = window.location.hash.substring(1);
  if (hash) {
    // Gets the DOM element by id of the referenced hash
    const el = document.getElementById(hash);
    // If the element is found set the open class
    if (el && el.tagName.toLowerCase() === "details") {
      el.setAttribute("open", "true");
    }
  }
});