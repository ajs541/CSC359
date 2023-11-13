
import './Verse.css';

import Line from './Line';

function Verse( props ) {
    // compute index of line to be shuffled
    const k = 
      Math.floor( Math.random() * props.verse.length );

    return (
        <div className="my-verse">
          {props.verse.map( 
            (line, j) => 
              <Line key={j} line={line} shuffle={j===k}/>)}
        </div>
    );
} // Verse()

export default Verse;
