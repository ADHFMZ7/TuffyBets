function rotateFunction(){
    var min = 9500;
    var max = 12500;
    var deg = Math.floor(Math.random() * (max - min)) + min;
    document.getElementById('box').style.transform = "rotate("+deg+"deg)";
  }

var element = document.getElementById('mainbox');
element.classList.remove('animate');

setTimeout(function(){
    element.classList.add('animate');
  }, 5000);