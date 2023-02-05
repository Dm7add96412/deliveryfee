import React, {useState} from "react"
import { theForm as Props } from "../App"

// Handling the inputs and delivering values for delivery fee calculations

interface IProps {

    setValues: React.Dispatch<React.SetStateAction<Props['theInputs']>>
}

const Inputs: React.FC<IProps> = ({setValues}) => {
    const [input, setInput] = useState({
        cart: '',
        distance: '',
        items: '',
        time: ''
    })

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>): void => {
        setInput({
            ...input,
            [e.target.name]: e.target.value
        })
    }
// handling button click and data validation
    const handleClick = (): void => {
        if (!input.cart ||
            !input.distance ||
            !input.items ||
            !input.time
        ) { 
            return alert('Please add values to all fields')
        }
        if ((parseFloat(input.cart)) <= 0.0 ||
        (parseInt(input.distance)) <= 0 ||
        (parseInt(input.items)) < 1
        ) {
        return alert('Please insert values that make sense :) (cart value decimals with (.)-character)')
        }
        if (!(parseFloat(input.cart)) ||
            !(parseInt(input.distance)) ||
            !(parseInt(input.items))
        ) {
            return alert('Please fill in only numbers, no letters or special characters')
        }

        setValues([{
            cart: parseFloat(input.cart),
            distance: parseInt(input.distance),
            items: parseInt(input.items),
            time: input.time    
            }
        ])
    }

    return(
        <div className="Inputs">
            <div>Cart value <input type='text' value={input.cart} name='cart' onChange={handleChange}/> €</div>
            <div>Delivery distance <input type='text' value={input.distance} name='distance' onChange={handleChange}/> m</div>
            <div>Amount of items <input type='text' value={input.items} name='items' onChange={handleChange}/> kpl</div>
            <div>Time <input type='datetime-local' value={input.time} name='time' onChange={handleChange}/> </div>
            <div className="Button">
                <button onClick={handleClick}>Calculate delivery price</button>
            </div>
        </div>
    )
}

export default Inputs