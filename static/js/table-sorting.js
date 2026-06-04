function sortAvailabilityTable(n) { 
    const table = event.target.closest("table");
    if (!table) return;

    let rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    switching = true;
    dir = "asc"; 
    
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            
            let valX = getCellValue(x, n);
            let valY = getCellValue(y, n);

            if (dir == "asc") {
                if (valX > valY){ 
                    shouldSwitch = true; 
                    break; 
                }
            }else if (dir == "desc"){
                if (valX < valY){ 
                    shouldSwitch = true; 
                    break; 
                }
            }
        }
        
        if(shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;      
        }else{
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

function getCellValue(td, n) {
    // Funcion para detectar que tipo de dato hay dentro de la casilla
    const hasCheck = td.querySelector('.fa-square-check');
    const hasUncheck = td.querySelector('.fa-square');

    //Casillas checkbox
    if (hasCheck || hasUncheck) {
        return hasCheck ? 1 : 0;
    }

    const text = td.innerText.trim();

    // Detectar numeros
    const cleanText = text.replace('€', '').replace(',', '.').trim();
    if (cleanText !== "" && !isNaN(cleanText)) {
        return parseFloat(cleanText);
    }

    // Valores de texto
    return text.toLowerCase();
}