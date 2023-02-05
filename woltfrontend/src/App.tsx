import {useState} from 'react';
import './App.css';
import Inputs from './components/Inputs';
import Total from './components/Total';

// defining initial input forms

export interface theForm {
  theInputs: {
    cart: number
    distance: number
    items: number
    time: string
}[]
}

// main app
function App() {

  const [values, setValues] = useState<theForm['theInputs']>([])

  return (
    <div className="App">
      <div className="App-top">
        <h2>Delivery Fee Calculator</h2>
      </div>
      <div className='App-content'>
            <Inputs setValues={setValues}/>
      </div>
      <div className='App-bottom'>
        <Total values={values}/>
      </div>
    </div>
  );
}

export default App;
