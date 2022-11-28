const sidenav = () => {
    const menu = document.querySelector(".menu-icon");
    const nav = document.querySelector(".nav");

    menu.addEventListener("click", () => {
        menu.classList.toggle("menu-icon-active");
        nav.classList.toggle("nav-active");
    })
}

sidenav();


