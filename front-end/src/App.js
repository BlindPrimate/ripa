import './App.css';
import {
    BrowserRouter as Router,
    Link,
    Switch,
    Route
} from 'react-router-dom'
import IssuesPage from "./components/IssuesPage";
import HomePage from "./components/HomePage";

function App() {
  return (
      <Router>
          <nav id="menu-bar">
              <ul id="menu">
                  <li className="menu-item">
                      <Link to="/">Home</Link>
                  </li>
                  <li className="menu-item">
                      <Link to="/issues">Issues</Link>
                  </li>
              </ul>
          </nav>
          <div id="main">
              <Switch>
                  <Route path="/issues">
                      <IssuesPage />
                  </Route>
                  <Route path="/">
                      <HomePage/>
                  </Route>
              </Switch>
          </div>
      </Router>
  );
}

export default App;
