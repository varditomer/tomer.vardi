function refreshPage(){
    window.location.reload();
}

function hand() {
  var a;
  a = document.getElementById("div1");
  a.innerHTML = "&#xf25a;";
  setTimeout(function () {
      a.innerHTML = "&#xf256;";
    }, 500);
  setTimeout(function () {
      a.innerHTML = "&#xf259;";
    }, 1000);
  setTimeout(function () {
      a.innerHTML = "&#xf256;";
    }, 1500);
}
hand();
setInterval(hand, 2000);