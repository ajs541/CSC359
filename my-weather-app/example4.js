// Define a recursive function.
// sequence is an arry of integers.
// n is a non-negative integer.
const f = function (sequence, n) {
    if (n === 0) {
        return sequence;
    } //if
    else {
        if (sequence.length === 0) {
            sequence.push(1);
        } //if
        else if (sequence.length === 1) {
            sequence.push(1);
        } //else if
        else {
            const i = sequence.length - 1;
            current = sequence[i];
            previous = sequence[i - 1];
            sequence.push(current + previous);
        } //else
        return f(sequence, n - 1);
    } //else
};

// Define a second function.
const g = n => f([], n);

// Call the function.
const n = 24;
g(n).map((k) => console.log(k));