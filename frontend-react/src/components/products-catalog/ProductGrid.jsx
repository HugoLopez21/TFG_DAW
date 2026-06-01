import React from 'react';
import {ProductCard} from './ProductCard';

export const ProductGrid = ({products}) =>{
    return (
        products.map(p =>{
            return <ProductCard key={p.id} product={p}/>
        })
    )
}