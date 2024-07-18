function fetchData(endpoint) {
    fetch(`/${endpoint}`)
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = ''; // Limpiar contenido previo

            if (data.body && data.body.length > 0) {
                const table = document.createElement('table');
                table.className = 'data-table';

                const thead = document.createElement('thead');
                const headerRow = document.createElement('tr');
                const headers = ['Clave', 'Créditos', 'Cve Plan', 'Grado', 'Horas Prácticas', 'Horas Teóricas', 'Materia'];
                headers.forEach(headerText => {
                    const th = document.createElement('th');
                    th.textContent = headerText;
                    headerRow.appendChild(th);
                });
                thead.appendChild(headerRow);
                table.appendChild(thead);

                const tbody = document.createElement('tbody');
                data.body.forEach(record => {
                    const row = document.createElement('tr');
                    Object.values(record).forEach(value => {
                        const td = document.createElement('td');
                        td.textContent = value;
                        row.appendChild(td);
                    });
                    tbody.appendChild(row);
                });
                table.appendChild(tbody);

                resultDiv.appendChild(table);
            } else {
                resultDiv.textContent = 'No se encontraron datos.';
            }
        })
        .catch(error => console.error('Error:', error));
}
