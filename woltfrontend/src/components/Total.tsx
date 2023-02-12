import React from "react"
import { theForm as Props } from "../App"
import CalculateFee from "./CalculateFee"

// initial interfaces

interface IProps {
    values: Props['theInputs']
}

const Total: React.FC<IProps> = ({values}) => {

    const renderValues = (): JSX.Element[] => {
        return values.map(value => {
            return (
                <CalculateFee cart={value.cart} 
                distance={value.distance} 
                items={value.items} 
                time={value.time}
                key={value.cart}/>
            )
        })}

    return(
        <div>
            {renderValues()}
        </div>
    )
}

export default Total