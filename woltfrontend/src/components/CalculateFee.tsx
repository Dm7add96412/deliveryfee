import React from "react"

// Calculating the delivery fee

interface theValues {
    cart: number
    distance: number
    items: number
    time: string
  }

const CalculateFee: React.FC<theValues> = ({cart, distance, items, time}) => {
    let min_distance = 1000
    let mdist_fee = 2
    let min_items = 5
    let mitems_fee = 0
    let cart_fee = 0
    let dist_fee = 0
    let items_fee = 0
    let time_fee = 1
    let date = new Date(time)
    let day = date.getDay()
    let hours = date.getHours()
    let minutes = date.getMinutes()

    // if cart value is 100€ or more, delivery fee will be 0€
    if (cart >= 100) {
        return <>Delivery price: 0€</>
    }

    // if cart value is less than 10€ an a subcharge between the cart value and 10€ is added
    if (cart < 10) {
        cart_fee = 10 - cart
    } else {
        cart_fee = 0
    }

    // distance fee for first 1km is 2€, after which 1€ is added for every additional 500m
    if (distance <= min_distance) {
        dist_fee = mdist_fee
    } else {
        while (min_distance < distance) {
            min_distance += 500
            mdist_fee += 1
        }
        dist_fee = mdist_fee
    }

    // if there are more than 5 items, an additional 50 cents is added for every extra item
    // if there are more than 12 items, an additional 1,2€ is added
    if (items < min_items) {
        items_fee = 0
    } else {
        if (items > 12) {
            mitems_fee = 1.2
        }
        while (min_items < items) {
            min_items += 1
            mitems_fee += 0.5
        }
        items_fee = mitems_fee
    }

    // if delivery will be made during rush hour Friday 3PM - 7PM, the delivery fee will be multiplied by 1,2x
    if (day === 5) {
        if (hours >= 15) {
            if (hours < 19) {
                time_fee = 1.2
            }
            if (hours === 19) {
                if (minutes === 0) {
                    time_fee = 1.2
                }
            }
        }
    }

    let total = Math.round(((cart_fee + dist_fee + items_fee) * time_fee) * 10) / 10

    // delivery fee can never be more than 15€
    if (total > 15) {
        total = 15
    }

    return(
        <>Delivery price: {total} €</>
    )
}

export default CalculateFee