const SLIDER = document.querySelector('.ac_flex_animes')

var isDown = false;
var startX;
var scrollLeft;

const MOVEMENT_SCALAR = 3;

SLIDER.addEventListener('mousedown', (event) =>
{
    console.log(isDown);
    isDown = true;
    SLIDER.classList.add('active');
    startX = event.pageX - SLIDER.offsetLeft;
    scrollLeft = SLIDER.scrollLeft;
});
SLIDER.addEventListener('mouseleave', () =>
{
    console.log(isDown);
    isDown = false;
    SLIDER.classList.remove('active');
});
SLIDER.addEventListener('mouseup', () =>
{
    console.log(isDown);
    isDown = false;
    SLIDER.classList.remove('active');
});
SLIDER.addEventListener('mousemove', (event) =>
{
    console.log(isDown);
    if(!isDown)
        return;

    event.preventDefault();
    x = event.pageX - SLIDER.offsetLeft;
    movement = (x - startX) * MOVEMENT_SCALAR;

    SLIDER.scrollLeft = scrollLeft - movement;
});