$('.owl-carousel').owlCarousel({
    rewind: true,
    margin: 10,
    nav: true,
    dots: true,
    dotsEach: true,
    navText: ['<i class="fas fa-chevron-left"></i>', '<i class="fas fa-chevron-right"></i>'],
    navContainer: '.custom-nav',
    dotsContainer: '.owl-dots',
    responsive: {
        0: {
            items: 1
        },
        576: {
            items: 2
        },
        768: {
            items: 3
        },
        992: {
            items: 4
        },
        1200: {
            items: 5
        }
    }
})