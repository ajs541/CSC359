import React, { useState } from "react";
import styled from "styled-components";

const theme = {
  blue: {
    default: "#3f51b5",
    hover: "#283593"
  },
  pink: {
    default: "#e91e63",
    hover: "#ad1457"
  }
};

const Button = styled.button`
  background-color: ${(props) => theme[props.theme].default};
  color: white;
  padding: 5px 15px;
  border-radius: 5px;
  outline: 0;
  text-transform: uppercase;
  margin: 10px 0px;
  cursor: pointer;
  box-shadow: 0px 2px 2px lightgray;
  transition: ease background-color 250ms;
  &:hover {
    background-color: ${(props) => theme[props.theme].hover};
  }
  &:disabled {
    cursor: default;
    opacity: 0.7;
  }
`;

Button.defaultProps = {
  theme: "blue"
};


const Tab = styled.button`
  padding: 10px 30px;
  cursor: pointer;
  opacity: 0.6;
  background: white;
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

function BreadGroup() {
  const [active, setActive] = useState(breads[0]);
  return (
    <>
      <div>
        {breads.map((bread) => (
          <Tab
            key={bread}
            active={active === bread}
            onClick={() => setActive(bread)}
          >
            {bread}
          </Tab>
        ))}
      </div>
      <p />
      <p> Your bread selection: {active} </p>
    </>
  );
}

function EggGroup() {
  const [active, setActive] = useState(eggs[0]);
  return (
    <>
      <div>
        {eggs.map((bread) => (
          <Tab
            key={bread}
            active={active === bread}
            onClick={() => setActive(bread)}
          >
            {bread}
          </Tab>
        ))}
      </div>
      <p />
      <p> How you want your eggs: {active} </p>
    </>
  );
}

function FruitGroup() {
  const [active, setActive] = useState(fruits[0]);
  return (
    <>
      <div>
        {fruits.map((fruit) => (
          <Tab
            key={fruit}
            active={active === fruit}
            onClick={() => setActive(fruit)}
          >
            {fruit}
          </Tab>
        ))}
      </div>
      <p />
      <p> Your fruit selection: {active} </p>
    </>
  );
}

const breads = ["Toast", "English Muffin", "Bagel", "Croissant"];
const eggs = ["scrambled", "sunny side up", "over easy", "boiled"];
const fruits = ["orange", "grapefruit", "grape", "apple juice"];

export default function App() {
  return (
    <>
      <h1>Breakfast Options:</h1>
      <BreadGroup />
      <EggGroup />
      <FruitGroup />
    </>
  );
}
