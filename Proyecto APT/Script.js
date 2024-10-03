// Datos para las cards
const cardsData = [
    {
        img: 'Fotos/Marraqueta.jpg',
        title: 'Marraqueta Recién Horneada',
        text: 'Deliciosa marraqueta fresca recién salida del horno. ¡Perfecta para el desayuno!',
    },
    {
        img: 'Fotos/Pasteles.jpeg',
        title: 'Pasteles Variados',
        text: 'Una selección de pasteles deliciosos para cualquier ocasión.',
    },
    {
        img: 'Fotos/Torta.jpg',
        title: 'Torta de Chocolate',
        text: 'Torta de chocolate rica y esponjosa, ideal para los amantes del chocolate.',
    },
];

// Función para mostrar el contenido real de las cards
function loadCards() {
    const cardsContainer = document.getElementById('cards-container');

    // Crear y agregar cada card al contenedor
    cardsData.forEach((card) => {
        const cardCol = document.createElement('div');
        cardCol.className = 'col-auto'; // Ocupa el ancho necesario para la card

        const cardElement = document.createElement('div');
        cardElement.className = 'card';
        cardElement.innerHTML = `
            <img src="${card.img}" class="card-img-top" alt="${card.title}">
            <div class="card-body">
                <h5 class="card-title">${card.title}</h5>
                <p class="card-text">${card.text}</p>
                <a href="#" class="btn btn-primary">Ver más</a>
            </div>
        `;

        // Agregar la card a su contenedor
        cardCol.appendChild(cardElement);
        cardsContainer.appendChild(cardCol);
    });
}

// Simular una carga después de 2 segundos
setTimeout(loadCards, 1500);