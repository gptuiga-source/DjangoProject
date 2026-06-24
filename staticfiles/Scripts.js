const error = document.getElementById('error');

if (error) {
  const text = error.textContent.toLowerCase();

  if (text.includes('доступное')) {
    error.classList.remove('error_red', 'error_green');
    error.classList.add('error_blue');
  }
  if (text.includes('занято')) {
    error.classList.remove('error_blue', 'error_green');
    error.classList.add('error_red');
  }
  if (text.includes('добавленно')) {
    error.classList.remove('error_red', 'error_blue');
    error.classList.add('error_green');
  }
}
