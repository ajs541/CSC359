import React, { Fragment, useState } from "react";
import { BrowserRouter as Router, Route, Link, Routes, Outlet } from "react-router-dom";
import styled from "styled-components";

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

function MenuGroup({ selected, setSelected, items }) {
  const handleItemClick = (index) => {
    setSelected(items[index]); // Update the selected image URL directly
  };
  
  return (
    <div>
      {items.map((item, index) => (
        <Tab
          key={item}
          active={selected === item}
          onClick={() => handleItemClick(index)}
        >
          {index + 1} {/* Display a number instead of the image */}
        </Tab>
      ))}
    </div>
  );
}

export default function App() {
  const [selectedPrimatesImage, setSelectedPrimatesImage] = useState("");
  const [selectedReptilesImage, setSelectedReptilesImage] = useState("");
  const [selectedBirdsImage, setSelectedBirdsImage] = useState("");

  const numberOptions = ["1", "2", "3"]; // Number options for the MenuGroup

  return (
    <Router>
      <main>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/Primates">Primates</Link></li>
            <li><Link to="/Reptiles">Reptiles</Link></li>
            <li><Link to="/Birds">Birds</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route index element={<Home />} />
          <Route path="/*" element={<Main />} />
          <Route path="/Primates" element={<Primates />} />
          <Route path="/Reptiles" element={<Reptiles />} />
          <Route path="/Birds" element={<Birds />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </Router>
  );
}

const Main = () => (
  <Fragment>
    <h1>Error 404</h1>
    <p>Section not found.</p>
    <Outlet />
  </Fragment>
);


const Home = () => (
  <Fragment>
    <h1>Aaron's Zoo</h1>
    <p>Welcome, select an animal category to get started.</p>
  </Fragment>
);

const Primates = () => {
  const [selectedPrimatesImage, setSelectedPrimatesImage] = useState("");

  return (
    <Fragment>
      <h1>Primates</h1>
      <p>Mammals that are defined by having opposable thumbs, allowing them to grip and create tools.</p>
      <p>The two main categories are Apes and Monkeys. While similar, apes are much larger and do not have tails, unlike the smaller monkeys.</p>
      <MenuGroup
        selected={selectedPrimatesImage}
        setSelected={setSelectedPrimatesImage}
        items={[
          "https://outforia.com/wp-content/uploads/2021/03/Types_Monkeys_East_Javan_Langur_0321.jpg",
          "https://1.bp.blogspot.com/-Dt4zQZIq_U4/TvfeRMwptnI/AAAAAAAAEOg/hp_0XRDmQCY/s1600/monkey_5.jpg",
          "https://4.bp.blogspot.com/-vA4SiaM3rk8/TvfdbwcVGZI/AAAAAAAAENk/EQEbBrNEPqc/s1600/monkey_1.jpg"
        ]} // Add your image URLs for primates
      />
      <img src={selectedPrimatesImage} alt="Primates Image" />
    </Fragment>
  );
}

const Reptiles = () => (
  <Fragment>
    <h1>Reptiles</h1>
    <p>Reptiles section content goes here</p>
  </Fragment>
);

const Birds = () => (
  <Fragment>
    <h1>Birds</h1>
    <p>Birds section content goes here</p>
  </Fragment>
);

const NotFound = () => (
  <h1>404: Page not found</h1>
);
