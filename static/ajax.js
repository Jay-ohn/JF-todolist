document.addEventListener('DOMContentLoaded', function() {
    // Get the signup form element
    const signupForm = document.getElementById('signupForm');

    // Add event listener for form submission
    signupForm.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        const formData = new FormData(signupForm);
        const data = new URLSearchParams();
        for (const pair of formData) {
            data.append(pair[0], pair[1]); // Append each form field to URLSearchParams
        }

        try {
            // Send form data to the server using fetch API
            const response = await fetch('/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: data // Send the URL encoded form data
            });

            const result = await response.json(); // Parse the JSON response

            if (response.ok) {
                // If response is successful, display success message
                displayMessage('User registered successfully! Login to your account.', 'success');
                signupForm.reset(); // Reset the form fields
            } else {
                // If response is not successful, display error message
                displayMessage(result.message || 'An error occurred!', 'error');
            }
        } catch (error) {
            // Handle any errors that occurred during fetch
            displayMessage('An error occurred: ' + error.message, 'error');
        }
    });

    // Function to display messages to the user
    function displayMessage(message, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `alert alert-${type}`; // Set the class based on message type
        messageDiv.textContent = message; // Set the message text
        signupForm.prepend(messageDiv); // Add the message to the top of the form

        // Remove the message after 3 seconds
        setTimeout(() => {
            messageDiv.remove();
        }, 3000);
    }
});