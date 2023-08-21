// Loading Spinner
function showSpinner() {
  document.getElementById('loading-spinner').classList.add('show');

  // Sentiment analysis code...
  
  document.getElementById('loading-spinner').classList.remove('show');
}

// Dark Mode Toggle
const themeSwitch = document.querySelector('.theme-switch');

themeSwitch.addEventListener('click', () => {
  document.body.classList.toggle('dark-theme');

  // Save theme to localStorage
}) 




