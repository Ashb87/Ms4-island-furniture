function sendMail(contactForm) {
    emailjs.send("service_efq1gzx","template_4fz42c5", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            contactForm.reset(); // To clear the page
        },
        function(error) {
            console.log("FAILED", error);
            alert("Sorry, Please try again", error);
        }
    );
    return false;  // To block from loading a new page   
}