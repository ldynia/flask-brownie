fetch('/skills')
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    const footer = document.getElementById('footer');
    footer.textContent = data.skill
  });