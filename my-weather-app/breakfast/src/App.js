import React, { useState } from "react";
import styled from "styled-components";
import "./App.css";

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
`;

function MenuGroup({ selected, setSelected, items }) {
  const handleItemClick = (index) => {
    const updatedSelection = items.map((item, i) => (i === index ? item : '')); //this is how I change the elements on the fly of the order sentence.
    setSelected(updatedSelection);  //by setting the update within the MenuGroup, it allows the selection to update in real time as buttons are changed and pressed.
  };

  return (
    <>
      <div>
        {items.map((item, index) => (
          <Tab
            key={item}
            active={selected[index] === items[index]}
            onClick={() => handleItemClick(index)}
          >
            {item}
          </Tab>
        ))}
      </div>
    </>
  );
}


export default function App() {
  const [selectedBreads, setSelectedBreads] = useState(["", "", ""]); //sets the useState of each element
  const [selectedEggs, setSelectedEggs] = useState(["", "", ""]);  //initial value of each are three blank strings
  const [selectedFruits, setSelectedFruits] = useState(["", "", ""]); //using arrays for values and useState's for the changing variables ended up working out well

  const breads = ["Toast", "English Muffin", "Bagel", "Croissant"];  //food arrays
  const eggs = ["Scrambled Eggs", "Sunny Side Up Eggs", "Eggs Over Easy", "Boiled Eggs"];
  const fruits = ["Orange", "Grapefruit", "Grape", "Apple Juice"];

  return (
    <body>
      <h1>Breakfast Options:</h1>
      <MenuGroup
        selected={selectedBreads}
        setSelected={setSelectedBreads}
        items={breads}
      />
      <MenuGroup
        selected={selectedEggs}
        setSelected={setSelectedEggs}
        items={eggs}
      />
      <MenuGroup
        selected={selectedFruits}
        setSelected={setSelectedFruits}
        items={fruits}
      />
      <p>Your order: {selectedBreads.filter(item => item !== '').join(", ")}, {selectedEggs.filter(item => item !== '').join(", ")}, and {selectedFruits.filter(item => item !== '').join(", ")}</p>
    </body>
  );
}
