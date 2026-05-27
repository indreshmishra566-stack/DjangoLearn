// Sidebar toggle
const sidebar = document.getElementById('sidebar');
const toggleBtn = document.getElementById('toggleBtn');
const sidebarBackdrop = document.getElementById('sidebarBackdrop');
const mobileQuery = window.matchMedia('(max-width: 768px)');

function isMobileNav() {
  return mobileQuery.matches;
}

function setMobileMenu(open) {
  if (!sidebar) return;
  sidebar.classList.toggle('open', open);
  document.body.classList.toggle('nav-open', open);
  if (toggleBtn) {
    toggleBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
}

function closeMobileMenu() {
  setMobileMenu(false);
}

if (toggleBtn && sidebar) {
  toggleBtn.setAttribute('aria-controls', 'sidebar');
  toggleBtn.setAttribute('aria-expanded', 'false');
  toggleBtn.addEventListener('click', () => {
    if (isMobileNav()) {
      setMobileMenu(!sidebar.classList.contains('open'));
    } else {
      sidebar.classList.toggle('closed');
    }
  });
}

if (sidebarBackdrop) {
  sidebarBackdrop.addEventListener('click', closeMobileMenu);
}

mobileQuery.addEventListener('change', () => {
  closeMobileMenu();
  if (sidebar && isMobileNav()) {
    sidebar.classList.remove('closed');
  }
});

// Copy code buttons
document.querySelectorAll('.copy-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const code = btn.dataset.code;
    navigator.clipboard.writeText(code).then(() => {
      const orig = btn.textContent;
      btn.textContent = '✓ Copied!';
      btn.style.color = '#44b78b';
      btn.style.borderColor = '#44b78b';
      setTimeout(() => {
        btn.textContent = orig;
        btn.style.color = '';
        btn.style.borderColor = '';
      }, 2000);
    });
  });
});

// Copy command rows
document.querySelectorAll('.cmd-row').forEach(row => {
  row.addEventListener('click', () => {
    const cmd = row.dataset.cmd;
    navigator.clipboard.writeText(cmd).then(() => {
      const hint = row.querySelector('.cmd-copy-hint');
      if (hint) {
        hint.textContent = '✓';
        hint.style.color = '#44b78b';
        setTimeout(() => {
          hint.textContent = 'copy';
          hint.style.color = '';
        }, 1500);
      }
    });
  });
});

// Sidebar search
const searchInput = document.getElementById('sidebarSearch');
if (searchInput) {
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase();
    document.querySelectorAll('.chapter-link').forEach(link => {
      const title = link.querySelector('.ch-title').textContent.toLowerCase();
      link.classList.toggle('hidden', !title.includes(q));
    });
  });
}

document.querySelectorAll('.chapter-link').forEach(link => {
  link.addEventListener('click', closeMobileMenu);
});

// Track completed chapters in localStorage
const completeBtn = document.getElementById('completeBtn');
const slug = document.body.dataset.slug;

function updateCompleteBtn() {
  if (!completeBtn || !slug) return;
  const done = JSON.parse(localStorage.getItem('django-learn-progress') || '{}');
  if (done[slug]) {
    completeBtn.textContent = '✅ Chapter Completed!';
    completeBtn.classList.add('completed');
  }
  // Update sidebar checkmarks
  document.querySelectorAll('.chapter-link[data-slug]').forEach(link => {
    const s = link.dataset.slug;
    const doneEl = link.querySelector('.ch-done');
    if (doneEl) doneEl.style.display = done[s] ? 'inline' : 'none';
  });
  // Update progress bar
  const allLinks = document.querySelectorAll('.chapter-link[data-slug]');
  const total = allLinks.length;
  const count = Object.values(done).filter(Boolean).length;
  const bar = document.querySelector('.progress-bar-fill');
  const pct = document.querySelector('.progress-pct');
  const countEl = document.querySelector('.progress-count');
  if (bar) bar.style.width = `${Math.round((count / total) * 100)}%`;
  if (pct) pct.textContent = `${Math.round((count / total) * 100)}% complete`;
  if (countEl) countEl.textContent = `${count}/${total}`;
}

if (completeBtn && slug) {
  updateCompleteBtn();
  completeBtn.addEventListener('click', () => {
    const done = JSON.parse(localStorage.getItem('django-learn-progress') || '{}');
    done[slug] = true;
    localStorage.setItem('django-learn-progress', JSON.stringify(done));
    updateCompleteBtn();
  });
}
