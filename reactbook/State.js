
import './State.css';

import { useState } from 'react';


function State() {
    function makeState(stateName, yearOfAdmission) {
        return ({
            stateName: stateName,
            yearOfAdmission: yearOfAdmission
        });
    } // makeState()

    const neighboringStates = [
        makeState('Illinois', 1818),
        makeState('Iowa', 1846),
        makeState('Minnesota', 1858),
        makeState('Missouri', 1821),
        makeState('Nebraska', 1867),
        makeState('South Dakota', 1889),
        makeState('Wisconsin', 1848)
    ]; // neighboringStates

    const [neighbors, setNeighbors] =
        useState(neighboringStates);

    const [index, setIndex] = useState(0);

    const [count, setCount] = useState(0);

    function compareYears(a, b) {
        if (a.yearOfAdmission < b.yearOfAdmission) {
            return -1;
        } // if
        else if (a.yearOfAdmission > b.yearOfAdmission) {
            return 1;
        } // else if
        else {
            return 0;
        } // else
    } // compareYears()

    function compareNames(a, b) {
        if (a.stateName < b.stateName) {
            return -1;
        } // if
        else if (a.stateName > b.stateName) {
            return 1;
        } // else if
        else {
            return 0;
        } // else
    } // compareNames()

    function nextState(e) {
        let i = (index + 1);

        if (i === neighbors.length) {
            const copy = neighbors.map(state =>
            ({
                stateName: state.stateName,
                yearOfAdmission: state.yearOfAdmission
            }));


            if (count % 2 === 0) {
                copy.sort(compareYears);
            } // if
            else {
                copy.sort(compareNames);
            } // else

            setNeighbors(copy);

            setCount(count + 1);
            i = 0;
        } // if

        setIndex(i);
    } // nextState()


    return (
        <button
            onClick={nextState}
            className='State-button'>
            <hr className='State-rule' />
            {neighbors[index].stateName}
            <hr className='State-rule' />
            {neighbors[index].yearOfAdmission}
        </button>
    );
} // State()

export default State;
