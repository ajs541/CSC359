import React, { Fragment } from "react";
import { BrowserRouter as Router, Route, Link, Routes, Outlet } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <main>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/primates">Primates</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route index element={<Home />} />
          <Route path="/*" element={<Main />} />
          <Route path="/primates" element={<Primates />} />
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
    <h1>Aaron's Zoo</h1>
    <p>Welcome, select an animal to get started.</p>
  </Fragment>
);

const Primates = () => (
  <Fragment>
    <h1>Primates</h1>
    <p>Primates section content goes here</p>
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
