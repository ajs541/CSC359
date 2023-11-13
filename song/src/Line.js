
import "./Line.css";

import Word from './Word';

import { useState } from 'react';

// Define a component that models
// one line of a song.
//
// The value of a property of this component
// will determine whether the words in the
// line appear in their correct order or shuffled.
//
// In the case of shuffled words, the component
// will give a user of the program a means of
// putting the words into correct order. 
function Line( props ) {

  // Define a function that can be
  // used to shuffle the elements
  // of an array.
  const shuffle = values => {
    const pairs = values.map( v => [v, Math.random()] )
    pairs.sort( (a, b) => a[1] - b[1] )
    return pairs.map( pair => pair[0] )
  } // shuffle()

  const unscrambled = props.line.split( " ");
  const scrambled = shuffle( unscrambled );

  // Define the state variables for this component. 
  const [inOrder, setInOrder] = useState( unscrambled );
  const [shuffled, setShuffled] = useState( scrambled );
  const [orderedPrefix, setOrderedPrefix] = useState( [] );
  const [nextWordIndex, setNextWordIndex] = useState( 0 );

  // Define a function that can be used
  // to remove a given target string from
  // an array of strings.
  function makeFilter( target ) {
    let found = false;

    function filter( name ) {

      if( !found ) {
        if( name !== target ) {
          return true;
        } // if
        else {
          found = true;
          return false;
        } // else
      } // if
      else {
        return true;
      } // else
    } // filter()

    return filter;
  } // makeFilter()

  // Define a function that, given an
  // array of strings, returns a single
  // string that contains all of the words
  // in the input separated by spaces.
  const makePhrase = wordArray => {
    const reducer = (product, next) => product + " " + next;
    return wordArray.reduce( reducer, "" ).trim();
  } // makePhrase()


  function onClick( event ) {
    // What is the word on the button
    // on which our user just clicked?
    const selectedWord = event.target.innerHTML;

    // What is the index of that selected word
    // in our shuffled array of words that are
    // not yet in the solution to this problem?
    const k = shuffled.indexOf( selectedWord );

    if( selectedWord === inOrder[nextWordIndex] ) {
        // Compute index of the next word in this line
        // in the solution.
        setNextWordIndex( nextWordIndex + 1 );
        setOrderedPrefix( orderedPrefix.concat( selectedWord ) );

        // Remove selected word from list of shuffled words.
        const shorterArray = shuffled.filter( makeFilter( selectedWord ) );
        setShuffled( shorterArray );      
    } // if
  } // onClick( event )

  if( props.shuffle ) {

      return (
         <>
         <p className="solution">{makePhrase(inOrder)}</p>
         <span className="prefix"> {makePhrase(orderedPrefix)} </span>
         {shuffled.map( 
          (word, k) => 
            <Word
              listener={onClick}
              word={word} />)}
         </>
      );
  } // if
  else {
      return (
        <p className="unscrambled">
          {props.line.trim()}
        </p>);
  } // else
} // Line()

export default Line;
