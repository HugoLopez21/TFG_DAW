import React from "react";

export const ProductCard = ({product}) =>{
    console.log(product)
    return (
        <p>{product.name}</p>
    )
}