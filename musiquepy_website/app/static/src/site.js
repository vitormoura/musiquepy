function init() {
  config_btnLogout();
}

function config_btnLogout() {
  var btnLogout = document.getElementById("btn-logout");

  if (btnLogout) {
    btnLogout.onclick = function () {
      fetch(btnLogout.dataset.logoutUrl, { method: "post" }).then(function () {
        document.location.href = "/";
      });
    };
  }
}

window.addEventListener("DOMContentLoaded", (event) => {
  init();
});
