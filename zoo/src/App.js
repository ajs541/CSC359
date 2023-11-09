import { useState } from 'react';
import 'styled-components';
import './output.css';
import 'react-router-dom';

const Tab = styled.button`
  padding: 10px 30px;   
  cursor: pointer;
  opacity: 0.6;
  font-size: 25px;
  border: 0;
  outline: 0;
  border-bottom: 2px solid transparent;
  transition: ease border-bottom 250ms;
  ${({ active }) =>
    active &&
    `
    border-bottom: 2px solid black;
    opacity: 1;
  `} 
`; //button function.  This is the base button element and used throughout the other functions.


function App() {
  return (
    <div className="App">
      <p>Hello world</p>
    </div>
  );
}

export default App;
