
import './Song.css';

import { useState } from 'react';
import Verse from './Verse';

function Song() {
    const lyrics =
`Lass uns die Wolke vier bitte nie mehr verlassen
Weil wir auf Wolke sieben viel zu viel verpassen
Ich war da schon ein Mal, bin zu tief gefallen
Lieber Wolke vier mit Dir als unten wieder ganz allein

Ziemlich gut, wie wir das so gemeistert haben
Wie wir die großen Tage unter kleinen Dingen begraben
Der Moment der die Wirklichkeit maskiert
Es tut nur gut zu wissen, dass das wirklich funktioniert

Lass uns die Wolke vier bitte nie mehr verlassen
Weil wir auf Wolke sieben viel zu viel verpassen
Ich war da schon ein Mal, bin zu tief gefallen
Lieber Wolke vier mit Dir, als unten wieder ganz allein

Hab nicht gesehen, was da vielleicht noch kommt
Was am Ende dann mein Leben und mein kleines Herz zerbombt
Denn der Moment ist das, was es dann zeigt, dass die Tage ziemlich dunkel sind
Doch Dein Lächeln bleibt. Doch Dein Lächeln bleibt...

Lass uns die Wolke vier bitte nie mehr verlassen
Weil wir auf Wolke sieben, viel zu viel verpassen
Ich war da schon ein Mal, bin zu tief gefallen

Lieber Wolke vier mit Dir als unten wieder ganz allein
Lieber Wolke vier mit Dir als unten wieder ganz allein`

    const song = 
        lyrics.split( "\n\n" ).map( s => s.split( "\n" ) )
    
    const [verseIndex, setVerseIndex] = useState( 0 );

    const selectNextVerse = (event) => { 
        const len = song[verseIndex].length;

        setVerseIndex( (verseIndex + 1) % len );
      }; // selectNextVerse()

    return (
        <div className="song">
          <Verse 
            verse={song[verseIndex]} 
            className="song-verse"/>

          <button id="song-button" 
              onClick={selectNextVerse}>
            NEXT VERSE
          </button>
      </div>
    );
} // Song()

export default Song;
