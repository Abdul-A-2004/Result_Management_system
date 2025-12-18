
    const collapseEl = document.getElementById('collapseExample');
    const overlay = document.getElementById('overlay');

  collapseEl.addEventListener('shown.bs.collapse', () => {
        overlay.style.display = 'block';
    document.body.classList.add('overlay-active');});

  collapseEl.addEventListener('hidden.bs.collapse', () => {
        overlay.style.display = 'none';
    document.body.classList.remove('overlay-active');
  });

  overlay.addEventListener('click', () => {
        bootstrap.Collapse.getInstance(collapseEl).hide();
  });

