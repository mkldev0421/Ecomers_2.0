/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
/* File: scripts.js
   Purpose: Site-wide JavaScript helpers and initializers.
   Sections:
   - Initialize UI components (tooltips, toasts)
   - Custom AJAX handlers (add-to-cart, cart updates)
*/

// Initialize Bootstrap tooltips (used for sale-star tooltips)
document.addEventListener('DOMContentLoaded', function () {
	var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
	tooltipTriggerList.map(function (tooltipTriggerEl) {
		return new bootstrap.Tooltip(tooltipTriggerEl);
	});
});

// NOTE: Add other page-specific scripts in the template or here with a short label.
// Example: AJAX helpers, UI utilities, small DOM helpers.