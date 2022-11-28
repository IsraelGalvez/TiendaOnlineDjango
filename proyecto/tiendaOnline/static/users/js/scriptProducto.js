//Cambio de cantidad de productos ingresados por el usuario
let minusBtn = document.querySelector(".input_minus");
let plusBtn = document.querySelector(".input_plus");
let userInput = document.querySelector(".input_number");

let userInputNumer = 0;

plusBtn.addEventListener("click", () => {
  userInputNumer++;
  userInput.value = userInputNumer;
});

minusBtn.addEventListener("click", () => {
  userInputNumer--;
  if (userInputNumer <= 0) {
    userInputNumer = 0;
  }
  userInput.value = userInputNumer;
});

//Agregar el total al carrito
const addToCartBtn = document.querySelector(".details_button");
let cartNotification = document.querySelector(".header_cart--notification");
let lastValue = parseInt(cartNotification.innerText);

addToCartBtn.addEventListener("click", () => {
  lastValue = lastValue + userInputNumer;
  cartNotification.innerText = lastValue;
  userInputNumer = 0;
  userInput.value = userInputNumer;
  cartNotification.style.display = "block";
  drawProductInModal();
});

//Mostrar el carrito
const cartBtn = document.querySelector(".header_cart");
const cartModal = document.querySelector(".cart-modal");
const productContainer = document.querySelector(
  ".cart-modal_checkout-container"
);

cartBtn.addEventListener("click", () => {
  cartModal.classList.toggle("show");
  if (lastValue == 0) {
    productContainer.innerHTML = '<p class="cart-empty">Your cart is empty</p>';
  }else{
    drawProductInModal();
  }
});

//Cambiar las imagenes
const imageContainer = document.querySelector(".gallery_image-container");
const nextGalleryBtn = document.querySelector(".gallery_next");
const previusGalleryBtn = document.querySelector(".gallery_previus");
let imgIndex = 1;

nextGalleryBtn.addEventListener("click", () => {
  changeNextImage(imageContainer);
});

previusGalleryBtn.addEventListener('click', ()=>{
  changePreviusImage(imageContainer);
})

//Mostrar imagenes del modal al precionarlas
const mostrarImageModal = document.querySelector('.modal-gallery_background');
const closeImageModal = document.querySelector('.modal-gallery_close');

imageContainer.addEventListener('click', ()=>{
  mostrarImageModal.style.display = 'grid';
});

closeImageModal.addEventListener('click', ()=>{
  mostrarImageModal.style.display = 'none';
});

//Cambiar la imagen del gallery
let thumbnails = document.querySelectorAll('.gallery_thumnail');
thumbnails = [...thumbnails];

thumbnails.forEach(thumbnails => {
  thumbnails.addEventListener('click', event=>{
    imageContainer.style.backgroundImage = `url('../img/image-article_${event.target.id}-min.png')`;
  });
});

//Cambiar la imagen del modal
let modalThumbnails = document.querySelectorAll('.modal-gallery_thumnail');
const modalImageContainer = document.querySelector('.modal-gallery_image-container');

modalThumbnails = [...modalThumbnails];
modalThumbnails.forEach(modalThumbnails =>{
  modalThumbnails.addEventListener('click', event=>{
    modalImageContainer.style.backgroundImage = `url('../img/image-article_${event.target.id.slice(-1)}-min.png')`;
  });
});

//Cambiar imagen del modal usando los botones
const nextModalBtn =  document.querySelector('.modal-gallery_next');
const previusModalBtn =  document.querySelector('.modal-gallery_previus');

nextModalBtn.addEventListener('click', ()=>{
  changeNextImage(modalImageContainer);
});

previusModalBtn.addEventListener('click', ()=>{
  changePreviusImage(modalImageContainer);
});

//Mostrar navbar con el boton menu
const menuNav = document.querySelector('.header_menu');
const contNav = document.querySelector('.modal-navbar_background');
const closeNav = document.querySelector('.modal-navbar_close_icon');

menuNav.addEventListener('click', ()=>{
  contNav.style.display = 'block';
});

closeNav.addEventListener('click', ()=>{
  contNav.style.display = 'none';
});

//Cambiar a modo nocturno y viceversa
/* let darkToggle = document.querySelector('#darkToggle');

darkToggle.addEventListener('change', ()=> {
  document.body.classList.toggle('dark');
}) */

//Funciones
function deleteProduct() {
  //Borrar el contenido del carrito
  const deleteProductBtn = document.querySelector(".cart-modal_delete");

  deleteProductBtn.addEventListener("click", () => {
    productContainer.innerHTML = '<p class="cart-empty">Your cart is empty</p>';
    lastValue = 0;
    cartNotification.innerText = lastValue;
  });
}

// function drawProductInModal() {
//   productContainer.innerHTML = `        
//   <div class="cart-modal_details-container">
//     <img class="cart-modal_image" src="img/image-article-thumnail_1-min.png" alt="img product">
//     <div>
//         <p class="cart-modal_product-container">Playera del Necaza edición limitada</p>
//         <p class="cart-modal_price-container">$1,350.00 x 1 <span>$1,350.00</span></p>
//     </div>
//     <img class="cart-modal_delete" src="img/icon-delete.svg" alt="icon delete">
//   </div>
//   <button class="cart-modal_checkout">Chekout</button>`;
//   deleteProduct();
//   let proceModal = document.querySelector(".cart-modal_price-container");
//   proceModal.innerHTML = `$1,350.00 x ${lastValue} <span>$${
//     lastValue * 1350
//   }.00</span>`;
// }

function changeNextImage(imgContainer) {
  if (imgIndex === 3) {
    imgIndex = 1;
  } else {
    imgIndex++;
  }
  imgContainer.style.backgroundImage = `url('../img/image-article_${imgIndex}-min.png')`;
}

function changePreviusImage(imgContainer) {
  if (imgIndex === 1) {
    imgIndex = 3;
  } else {
    imgIndex--;
  }
  imgContainer.style.backgroundImage = `url('../img/image-article_${imgIndex}-min.png')`;
}

