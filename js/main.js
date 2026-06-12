document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('search-input');
  const filterButtons = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.solution-card');
  const noResults = document.getElementById('no-results');
  
  let currentFilter = 'all';
  let searchQuery = '';

  function filterCards() {
    let visibleCount = 0;
    
    cards.forEach(card => {
      const cardTemas = card.getAttribute('data-temas').split(',');
      const cardSearchText = card.getAttribute('data-search').toLowerCase();
      
      // Check category match
      let categoryMatch = false;
      if (currentFilter === 'all') {
        categoryMatch = true;
      } else if (cardTemas.includes(currentFilter)) {
        categoryMatch = true;
      }
      
      // Check search match
      const searchMatch = cardSearchText.includes(searchQuery);
      
      // Apply visibility
      if (categoryMatch && searchMatch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });
    
    // Show/hide empty state
    if (visibleCount === 0) {
      noResults.style.display = 'block';
    } else {
      noResults.style.display = 'none';
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      filterCards();
    });
  }

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.getAttribute('data-filter');
      filterCards();
    });
  });

  // Modal interaction for Concept Note Info
  const btnAbout = document.getElementById('btn-about');
  const modalOverlay = document.getElementById('about-modal');
  const modalClose = document.getElementById('modal-close');

  if (btnAbout && modalOverlay && modalClose) {
    btnAbout.addEventListener('click', () => {
      modalOverlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    });

    modalClose.addEventListener('click', () => {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    });

    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }
});
