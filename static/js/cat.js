document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.dropdown-submenu > a').forEach(function(el) {
      el.addEventListener("click", function (e) {
        if (window.innerWidth < 992) { // Prevent auto-close on mobile
          e.preventDefault();
          this.nextElementSibling.classList.toggle("show");
        }
      });
    });
  });
  