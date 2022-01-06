//document.getElementById("my_2020").addEventListener('click', () =>
//{
//    console.log("Dhaposid")
//});


const SLIDERS = document.querySelectorAll('.ac_flex_animes')

for (i = 0; i < SLIDERS.length; i++) 
{
    SLIDER = SLIDERS[i];
    console.log(SLIDER);

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
        event.pageX = scrollLeft + movement;
    });
}

