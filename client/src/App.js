import "./App.css";
import Location from "./components/Location";
import FlightDetails from "./components/FlightDetails";
import axios from "axios"
function App() {
 
 
  return (
    <div>
    <h1>Flight Search App</h1>
            <br />
      <div className="form-style">
        <Location />
      </div>
     
    </div>
  );
}

export default App;
