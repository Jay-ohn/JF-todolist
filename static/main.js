// JS for fading out feedback messages after 2 seconds

// Get all alert elements
document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show');
            alert.classList.add('fade');
            alert.style.display = 'none';
        }, 2000); // Fade out after 2 seconds
    });
});