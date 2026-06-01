import React, { useState, useEffect } from 'react';

export default function CatalogRoot(){
    const [products, setProducts] = useState([]);
    const [error, setError] = useState(false);

    const fetchProducts = async () => {
        try{
            const response = await fetch('/products/')
            if(!response.ok) throw new Error('Error en fetch api')
            const data = await response.json()
            console.log(data)
            setProducts(data)
        }catch(error){
            console.error(error)
            setError(true);
        }
    }

    useEffect(() => {
        fetchProducts();
    }, []);

    return (
        <div class="box-flex flex-column gap-500"> Catalogo</div>
    )
}