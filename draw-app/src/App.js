
import './App.css';
import Drawpage from './components/drawpage';
import LandingPage from './components/LandingPage';

import { GlobalStyle } from './GlobalStyle';

function App() {
  return (
    <div className="App">
      <LandingPage>
       
      </LandingPage>
      <Drawpage></Drawpage>
      <GlobalStyle/>
    </div>
  );
}

export default App;
