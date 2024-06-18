function setsdxlres(x, y) {
    var width = gradioApp().querySelector("#txt2img_width input[type=number]");
    var height = gradioApp().querySelector("#txt2img_height input[type=number]");

    width.value = x;
    height.value = y;

    updateInput(width);
    updateInput(height);
    return [];
}