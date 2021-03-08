'use strict';

const showInsertKlaar = function (jsonObject) {
  console.log(jsonObject);
};

const init = function () {
  document.querySelector('.js-insert').addEventListener('click', function () {
    const url = 'http://127.0.0.1:5000/api/v1/klanten';
    const body = JSON.stringify({
      FNaam: document.querySelector('.js-fnaam').value,
      Gemeente: document.querySelector('.js-gemeente').value,
      Nummer: document.querySelector('.js-nummer').value,
      Postcode: document.querySelector('.js-postcode').value,
      Straat: document.querySelector('.js-straat').value,
      VNaam: document.querySelector('.js-vnaam').value,
    });
    handleData(url, showInsertKlaar, null, 'POST', body);
  });
};

document.addEventListener('DOMContentLoaded', function () {
  console.info('DOM geladen');
  init();
});
