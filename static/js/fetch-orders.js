document.addEventListener('DOMContentLoaded', async function() {
    const tbody = document.getElementById('api-orders-tbody');
    const apiUrl = tbody.getAttribute('data-url');
    try {
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
            throw new Error('Error al cargar los pedidos.');
        }

        const orders = await response.json();

        if (orders.length === 0) {
            console.log(orders)
            tbody.innerHTML = '<tr><td class="pad-300 text-center text-muted">No hay pedidos recientes.</td></tr>';
            return;
        }

        tbody.innerHTML = orders.map(order => `
            <tr class="border-bottom">
                <td class="pad-300 text-left weight-medium">#${order.id}</td>
                <td class="pad-300 text-left">${order.user.first_name} ${order.user.last_name}</td>
                <td class="pad-300 text-left">${order.delivery_type_display || order.delivery_type}</td>
                <td class="pad-300 text-left weight-bold">${order.total}€</td>
                <td class="pad-300 text-left">
                    <span class="${order.pay_status ? 'color-primary' : 'color-danger'} weight-bold">
                        ${order.pay_status ? 'Pagado' : 'Pendiente'}
                    </span>
                </td>
                <td class="pad-300 text-left text-muted">${new Date(order.order_date).toLocaleString('es-ES', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' })}</td>
            </tr>
        `).join('');
    } catch(error) {
        console.error('Error con la api:', error);
        tbody.innerHTML = '<tr><td class="pad-300 text-center text-danger">Error cargando pedidos.</td></tr>';
    }
});