import React, { Fragment } from "react";
import { BrowserRouter as Router, Route, Link, Routes, Outlet } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <main>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route index element={<Home />} />
          <Route path="/*" element={<Main />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
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
    <h1>Home</h1>
    <p>Welcome to the Home section</p>
  </Fragment>
);

const About = () => (
  <Fragment>
    <h1>About</h1>
    <p>About section content goes here</p>
  </Fragment>
);

const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
    <p>Contact information and details</p>
  </Fragment>
);

const NotFound = () => (
  <h1>404: Page not found</h1>
);
