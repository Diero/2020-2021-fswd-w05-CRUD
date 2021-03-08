'use strict';

const showToonKlant = function (jsonObject) {
  console.log(jsonObject);
};

const init = function () {
  handleData(`http://127.0.0.1:5000/api/v1/klanten/100`, showToonKlant);

  document.querySelector('.js-update').addEventListener('click', function () {
    const url = `http://127.0.0.1:5000/api/v1/klanten/100`;
  });
};

document.addEventListener('DOMContentLoaded', function () {
  console.info('DOM geladen');
  init();
});
