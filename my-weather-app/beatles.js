const fab4 = ['John', 'Paul', 'George', 'Ringo'];

const band = [];
for (const beatle of fab4) {
    band.push('<th>' + beatle + '</th>');
} //for
console.log(band);

const group = fab4.map(
    beatle => '<th>' + beatle + '</th>');

console.log(group);

const g = fab4.map((beatle, index) =>
    '<th key = ' + index + '>' + beatle + '</th>');
console.log(g);