document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloDiv = document.querySelector('#hello');

  fetch(url)
    .then(response => response.json())
    .then(data => {
      helloDiv.textContent = data.hello;
    });
});
