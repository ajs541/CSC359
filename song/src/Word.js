
import './Word.css';

function Word( props ) {
  return ( 
    <button 
      onClick={props.listener}

      className="shuffled-word-button">
      {props.word}
    </button> );
} // Word()

export default Word;
