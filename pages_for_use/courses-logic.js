let btn_a = document.querySelector("#a");
let btn_b = document.querySelector("#b");
let btn_c = document.querySelector("#c");
let btn_d = document.querySelector("#d");
let cancel1 = document.querySelector("#cross-a");
let cancel2 =  document.querySelector("#cross-b");
let cancel3 = document.querySelector("#cross-c");
let cancel4 =  document.querySelector("#cross-d");

btn_a.addEventListener("click", () => {
    document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".popup_a").classList.add("popup_a-after");
});
cancel1.addEventListener("click", () => {
    document.querySelector(".overlay").classList.remove("overlay-nt");
    document.querySelector(".popup_a").classList.remove("popup_a-after");
});

btn_b.addEventListener("click", () => {
    document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".popup_b").classList.add("popup_b-after");
});
cancel2.addEventListener("click", () => {
    document.querySelector(".overlay").classList.remove("overlay-nt");
    document.querySelector(".popup_b").classList.remove("popup_b-after");
});

btn_c.addEventListener("click", () => {
    document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".popup_c").classList.add("popup_c-after");
});
cancel3.addEventListener("click", () => {
    document.querySelector(".overlay").classList.remove("overlay-nt");
    document.querySelector(".popup_c").classList.remove("popup_c-after");
});

btn_d.addEventListener("click", () => {
    document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".popup_d").classList.add("popup_d-after");
});
cancel4.addEventListener("click", () => {
    document.querySelector(".overlay").classList.remove("overlay-nt");
    document.querySelector(".popup_d").classList.remove("popup_d-after");
});



