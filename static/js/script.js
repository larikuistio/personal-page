function navbarDropdown() {
  if (x.className.indexOf("w3-show") == -1) { 
    x.className = x.className.replace("w3-hide", "w3-show");
  } else {
    x.className = x.className.replace("w3-show", "w3-hide");
  }
}
