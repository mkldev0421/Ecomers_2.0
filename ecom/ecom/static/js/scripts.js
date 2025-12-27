/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener('DOMContentLoaded', function () {
    // existing tooltip init...
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Explicit carousel init (works if automatic initialization fails)
    var carouselEl = document.querySelector('#carouselExampleIndicators');
    if (carouselEl) {
        if (typeof bootstrap !== 'undefined') {
            new bootstrap.Carousel(carouselEl, {
                interval: 5000,
                ride: 'carousel',
                pause: 'hover'
            });
            console.log('Carousel initialized');
        } else {
            console.warn('Bootstrap not available; carousel not initialized');
        }
    } else {
        console.warn('Carousel element not found on the page');
    }
});