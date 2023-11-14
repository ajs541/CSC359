import React, { Fragment, useState } from "react";
import { BrowserRouter as Router, Route, Link, Routes, Outlet } from "react-router-dom";
import styled from "styled-components";
import './App.css';
import image from "./crab.png";

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
`; //button function.  This is the base button element and used in MenuGroup

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
  /*
  const [selectedPrimatesImage, setSelectedPrimatesImage] = useState("");
  const [selectedReptilesImage, setSelectedReptilesImage] = useState("");
  const [selectedBirdsImage, setSelectedBirdsImage] = useState("");
  */
  return (
    <body style={{ backgroundImage:`url(${image})`}}>
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
    </body>
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
        ]}
      />
      <img src={selectedPrimatesImage} alt="Primates" />
    </Fragment>
  );
}

const Reptiles = () => {
  const [selectedReptilesImage, setSelectedReptilesImage] = useState("");

  return (
    <Fragment>
      <h1>Reptiles</h1>
      <p>Cold blooded, has scales.  Uses eggs for offspring.  Come in many colors but usually green.</p>
      <MenuGroup
        selected={selectedReptilesImage}
        setSelected={setSelectedReptilesImage}
        items={[
          "https://wallup.net/wp-content/uploads/2016/03/12/321711-animals-beach-lizards-reptile.jpg",
          "https://www.thoughtco.com/thmb/WJqyU9lE1sGRxvNzZ0owGnJfDZ0=/1274x0/filters:no_upscale():max_bytes(150000):strip_icc()/shutterstock_52214-56a006fe5f9b58eba4ae8c7b.jpg",
          "https://images.internetstores.de/products/889817/01/98baed/Crocs_Classic_Clogs_army_green[1920x1920].jpg?forceSize=false&forceAspectRatio=true&useTrim=true"
        ]} />
      <img src={selectedReptilesImage} alt="Reptiles" />
    </Fragment>
  );
}

const Birds = () => {
  const [selectedBirdsImage, setSelectedBirdsImage] = useState("");

  return (
    <Fragment>
      <h1>Birds</h1>
      <p>Warm blooded, usually with feathers.  Most fly but a few don't.</p>
      <MenuGroup
        selected={selectedBirdsImage}
        setSelected={setSelectedBirdsImage}
        items={[
          "https://2.bp.blogspot.com/-hK3WJtcEkUI/TphTufCdz0I/AAAAAAAACRs/KcGjipK7qyM/s1600/lovebirds_beautifulbirds_picturespool_19.jpg",
          "https://images7.alphacoders.com/759/759593.jpg",
          "https://res.cloudinary.com/teepublic/image/private/s--FDkhbc8Y--/t_Preview/b_rgb:484849,c_limit,f_auto,h_630,q_90,w_630/v1584563970/production/designs/8545411_0.jpg"
        ]} />
      <img src={selectedBirdsImage} alt="Birds" />
    </Fragment>
  );
}

const NotFound = () => (
  <h1>404: Page not found</h1>
);
