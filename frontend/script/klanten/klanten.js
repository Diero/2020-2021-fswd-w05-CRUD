'use strict';

const showKlanten = function (jsonObject) {
  console.log(jsonObject);
};

const init = function () {
  handleData(`http://127.0.0.1:5000/api/v1/klanten`, showKlanten);
};

document.addEventListener('DOMContentLoaded', function () {
  console.info('DOM geladen');
  init();
});
