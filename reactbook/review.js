
const primes = [2, 3, 5, 7, 11, 13, 17, 19];

const f0 = (accumulator, element) => accumulator + " " + element;

const f1 = (arrayOfNumbers) => arrayOfNumbers.reduce( f0, "" );

console.log( `a few primes = ${f1(primes)}` );
console.log();

function f2( accumulator, element, index, array ) {
    return accumulator.concat(
        (index > 0) ? (element-array[index - 1]) : element )
} // f2()

const f3 = (arrayOfNumbers) => arrayOfNumbers.reduce( f2, [] );
console.log(
    `How are these numbers related to the primes? ${f1(f3(primes))}` )
console.log();

console.log(
    `just some of the primes = ${f1(primes.filter( k => k < 10 ))}` )
console.log();

function f4( arrayOfPrimes ) {
    const result = primes.map( k => k+1 )
        .filter(k => Number.isInteger(Math.log(k)/Math.log(2)))
        .map( k => k - 1)

    return result
}; //f4()

console.log( `some special primes = ${f1(f4(primes))}` )
console.log();

const b = [...primes, 23];

console.log( `one more prime = ${f1(b)}` )
console.log();

const c = {state: `Iowa`, capital: `Des Moines`};

console.log(c);
console.log();

const {state, capital} = c;

console.log(
    `name of state = ${state} name of capital = ${capital}`)
console.log();

function f(j) {
    let n=0;

    function g() {
        const result = n;
        n+=j;
        return result;
    } // g()

    return g;
} //f()

const h = f(5);

for( let i = 0, i < 8, i++ ) {
    console.log ( h() );
} //for
console.log();