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
    const updatedSelection = items.map((item, i) => (i === index ? item : ''));
    setSelected(updatedSelection);
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
  const [selectedEggs, setSelectedEggs] = useState(["", "", ""]);
  const [selectedFruits, setSelectedFruits] = useState(["", "", ""]);

  const breads = ["Toast", "English Muffin", "Bagel", "Croissant"];  //food arrays
  const eggs = ["scrambled", "sunny side up", "over easy", "boiled"];
  const fruits = ["orange", "grapefruit", "grape", "apple juice"];

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
