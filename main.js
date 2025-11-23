
const homeproductdetail =[{
  image:"./img/phone1.jpg",
  heading:"Nothing CMF Phone 1 5G (6GB RAM, 128GB, Light Green)",
  money:"Rs ₹15,999.00"
},{
  image:"./img/T-Shirt.avif" ,
  heading:"Fashion Men′s New Blue Work Clothes T-Shirt",
  money:"Rs ₹300.00"
},{
  image:"./img/watches.avif",
  heading:"Fossil FS5437 Townsman Analog Watch for Men",
  money:"Rs ₹12,995.00"
},{
  image:"./img/goggle.webp",
  heading:"Captain | Brown Round Polarized Sunglasses - PMG7253",
  money:"Rs ₹1,249.00"
}]

let homeproductshtml='';

homeproductdetail.forEach((product) => {
  homeproductshtml=homeproductshtml+`
  <div class="home_dev">
    <div class="home_common_design">
      <div> <img   class="imgsubmain" src="${product.image}"> </div>
        <div class="cartcontent">
          <div class="heading">${product.heading}</div>
           <div class="money">${product.money}</div>
              <div><button class="buynow">Buy Now</button></div>
      </div>
    </div>
  </div>
  `;
});
document.querySelector('.js_homecontaner').
innerHTML =homeproductshtml;


const Categoriesproductdetails=[{
  image:"./img/mobiles.jpg",
  heading:"Mobile phones"
},{
  image:"./img/watchs.jpg",
  heading:" Watches"
},{
  image:"./img/clothes.avif",
  heading:"Clothes"
},{
   image:"./img/goggles.jpg",
  heading:" Goggles"
}];
let Categoriesproducthtml='';
Categoriesproductdetails.forEach((product)=>{
  Categoriesproducthtml=Categoriesproducthtml+
  `  <div class="categories_dev">
        <div class="Categories_common_design">
              <div class="cartcontent2">
                <div><img src="${product.image}" class="Categories_img"></div>
                    <div class="heading2"> ${product.heading}</div>
              </div>
       </div>
      </div>`
})

document.querySelector('.js_categoriecontaner ').innerHTML=Categoriesproducthtml;

document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".buttonone");
  const contents = document.querySelectorAll(".AllContainer");
  contents[0].classList.add("active");
  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const tabNumber = button.dataset.forNev;
      document.querySelectorAll(".underline").forEach(ul => {
        ul.classList.remove("underline_on");
        ul.classList.add("underline_off");
      });
      contents.forEach(content => content.classList.remove("active"));
      const underline = button.querySelector(".underline");
      if (underline) {
        underline.classList.remove("underline_off");
        underline.classList.add("underline_on");
      }
      const activeContent = document.querySelector(`.AllContainer[data-nev="${tabNumber}"]`);
      if (activeContent) activeContent.classList.add("active");
    });
  });
});
  
document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".searchinput");
  const content = document.querySelector(".searchdetail");

  // Show when input is focused
  input.addEventListener("focus", () => {
    content.classList.add("active");
  });

  // Hide when input loses focus (after a short delay to allow click)
  input.addEventListener("blur", () => {
    setTimeout(() => content.classList.remove("active"), 200);
  });
});


 let searchlist='';
 homeproductdetail.forEach((list)=>{
   searchlist+=`
   
      <li>${list.heading}</li>
      `
 })


 
document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".searchinput");
  const searchlistContainer = document.querySelector(".searchdetail");
  

  // Build the list once
  // document.querySelector('.searchdetail ul').innerHTML = searchlist;
  let searchlist = '';
  homeproductdetail.forEach((item) => {
    searchlist += `<li>${item.heading}</li>`;
  });
  searchlistContainer.innerHTML = searchlist;

  // NodeList of the original LIs (live only if not reassigning innerHTML)
  const listItems = Array.from(searchlistContainer.querySelectorAll('li'));

  // helper to show a single "Not Found" item
  function showNotFound() {
    // if .no-result already present, don't add another
    if (!searchlistContainer.querySelector('.no-result')) {
      const noItem = document.createElement('li');
      noItem.className = 'no-result';
      noItem.textContent = 'Not Found';
      searchlistContainer.appendChild(noItem);
    }
  }

  // helper to remove the "Not Found" item if present
  function removeNotFound() {
    const noItem = searchlistContainer.querySelector('.no-result');
    if (noItem) noItem.remove();
  }

  // input handler
  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();

    // if input empty -> show all items and remove "Not Found"
    if (q === '') {
      listItems.forEach((li, i) => {
        li.classList.remove('hide');
        li.style.removeProperty('--delay');
      });
      removeNotFound();
      return;
    }

    let found = false;

    listItems.forEach((li, i) => {
      const text = li.textContent.toLowerCase();
      const match = text.includes(q);
      li.classList.toggle('hide', !match);
      li.style.setProperty('--delay', i / 25 + 's'); // keep stagger
      if (match) found = true;
    });

    if (!found) {
      showNotFound();
    } else {
      removeNotFound();
    }
  });
});


