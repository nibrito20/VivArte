document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.getElementById("toggleBtn");
  const genresDiv = document.getElementById("genresDiv");
  const buttons = document.querySelectorAll(".filter-btn");
  const books = document.querySelectorAll(".book");

  if (!toggleBtn || !genresDiv) return;

  genresDiv.style.display = "none";

  toggleBtn.addEventListener("click", () => {
    if (genresDiv.style.display === "none" || genresDiv.style.display === "") {
      genresDiv.style.display = "flex";
      genresDiv.style.flexWrap = "wrap";
      genresDiv.style.justifyContent = "space-around";
      genresDiv.style.gap = "8px";
      toggleBtn.textContent = "Gêneros ▲";
    } else {
      genresDiv.style.display = "none";
      toggleBtn.textContent = "Gêneros ▼";
    }
  });

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      buttons.forEach(btn => btn.classList.remove("active")); // remove de todos
      button.classList.add("active"); // adiciona ao selecionado

      const genero = button.getAttribute("data-genero");

      books.forEach(book => {
        const generosLivro = book.getAttribute("data-generos").split(",");
        if (genero === "todos" || generosLivro.includes(genero)) {
          book.style.display = "block";
          book.style.opacity = "1";
          book.style.transition = "opacity 0.3s ease";
        } else {
          book.style.opacity = "0";
          setTimeout(() => {
            book.style.display = "none";
          }, 300);
        }
      });
    });
  });
});
