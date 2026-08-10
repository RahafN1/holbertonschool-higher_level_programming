fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then((response) => response.json())
  .then((data) => {
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelector('#hello').textContent = data.hello;
    });
  })
  .catch((error) => {
    console.error(error);
  });
