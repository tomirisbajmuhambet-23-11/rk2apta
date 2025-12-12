// Simple static library app: loads books from books.json, search, and "booking" stored in localStorage
const DATA = 'books.json';
let books = [];

async function loadBooks(){
  const res = await fetch(DATA);
  books = await res.json();
  renderBooks(books);
}

function renderBooks(list){
  const container = document.getElementById('books');
  container.innerHTML = '';
  if(list.length === 0) { container.innerHTML = '<p>Кітаптар табылмады.</p>'; return; }
  list.forEach(b => {
    const card = document.createElement('div'); card.className = 'card';
    card.innerHTML = `
      <h4>${b.title}</h4>
      <div class="meta">Автор: ${b.author} | Жанр: ${b.genre}</div>
      <div class="meta">Бет: ${b.pages} | Қалған: ${b.available}</div>
      <p>${b.description ? b.description.substring(0,120) + '...' : ''}</p>
      <button data-id="${b.id}">${b.available > 0 ? 'Брондау' : 'Қол жетімді емес'}</button>
    `;
    container.appendChild(card);
  });
  document.querySelectorAll('.card button').forEach(btn => {
    btn.addEventListener('click', ()=> openModal(btn.dataset.id));
  });
}

function openModal(id){
  const book = books.find(x=>x.id==id);
  if(!book) return alert('Кітап табылмады');
  if(book.available <= 0) return alert('Кітап қолжетімді емес');
  document.getElementById('mTitle').textContent = 'Брондау: ' + book.title;
  document.getElementById('mInfo').textContent = book.author + ' | ' + book.genre;
  document.getElementById('mMsg').textContent = '';
  document.getElementById('u_name').value = '';
  document.getElementById('u_phone').value = '';
  document.getElementById('confirm').dataset.id = id;
  document.getElementById('modal').classList.remove('hidden');
}

document.getElementById('close').addEventListener('click', ()=> document.getElementById('modal').classList.add('hidden'));
document.getElementById('confirm').addEventListener('click', ()=> {
  const id = document.getElementById('confirm').dataset.id;
  const name = document.getElementById('u_name').value.trim();
  const phone = document.getElementById('u_phone').value.trim();
  if(!name || !phone){ document.getElementById('mMsg').textContent = 'Барлық өрістерді толтырыңыз'; document.getElementById('mMsg').style.color='red'; return; }
  const book = books.find(x=>x.id==id);
  if(book.available <= 0){ document.getElementById('mMsg').textContent = 'Кітап қолжетімсіз'; return; }
  // save booking to localStorage
  const bookings = JSON.parse(localStorage.getItem('lb_bookings')||'[]');
  const newBooking = {id: Date.now(), bookId: book.id, title: book.title, name, phone, createdAt:new Date().toISOString()};
  bookings.push(newBooking);
  localStorage.setItem('lb_bookings', JSON.stringify(bookings));
  // decrement available locally (not persistent on server)
  book.available -= 1;
  renderBooks(books);
  document.getElementById('mMsg').textContent = 'Брондау сәтті жасалды!';
  document.getElementById('mMsg').style.color = 'green';
});

document.getElementById('searchBtn').addEventListener('click', ()=> {
  const q = document.getElementById('q').value.trim().toLowerCase();
  if(!q) return renderBooks(books);
  const res = books.filter(b => (b.title + ' ' + b.author + ' ' + b.genre).toLowerCase().includes(q));
  renderBooks(res);
});
document.getElementById('allBtn').addEventListener('click', ()=> renderBooks(books));

// init
loadBooks();
