import handleResponseFromAPI from './2-then.js';

const promise = Promise.resolve();
const p = handleResponseFromAPI(promise);
console.log(p);
