// JS for fading out feedback messages

// Get all alert elements
document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll('.alert-success, .alert-danger');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show');
            alert.classList.add('fade');
            alert.style.display = 'none';
        }, 5000); // Fade out after 5 seconds
    });
});