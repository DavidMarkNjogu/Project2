// NAVBAR START
document.querySelector('.hamburger').addEventListener('click', function() {
    const navLinks = document.querySelector('.nav-links');
    if (navLinks.style.display === 'none') {
        navLinks.style.display = 'block';
    } else {
        navLinks.style.display = 'none';
    }
});

// SCROLL
const myDiv = document.getElementById('myDiv');
const logo = document.getElementById('logo');
const scrolledLogo = document.getElementById('scrolledLogo');

window.addEventListener('scroll', function() {
    if (window.scrollY >= 90) {
        myDiv.className = 'header header-bg';
        logo.style.display = 'none';
        scrolledLogo.style.display = 'block';
    } else {
        myDiv.className = 'header';
        logo.style.display = 'block';
        scrolledLogo.style.display = 'none';
    }
});


// NAVBAR END

// faq items
const faqData = [
    {
        question: 'What is Haven Heights?',
        answer: 'Haven Heights is a comprehensive real estate management system designed to facilitate property management, listings, and client interactions. It allows users to browse property listings, inquire about properties, and manage real estate transactions efficiently.'
    },
    {
        question: 'How do I search for properties on Haven Heights?',
        answer: 'To search for properties on Haven Heights, simply use the search bar on the homepage or navigate to the property listings section. You can filter results by location, price range, property type, and other criteria to find properties that match your needs.'
    },
    {
        question: 'Can I list my property on Haven Heights?',
        answer: 'Yes, you can list your property on Haven Heights. To do so, create an account or log in if you already have one. Once logged in, navigate to the "List a Property" section, fill in the required details about your property, and submit your listing for review. Our team will review and approve your listing before it goes live on the platform.'
    },
    {
        question: 'How can I contact Haven Heights customer support?',
        answer: 'You can contact Haven Heights customer support by visiting the "Contact Us" page on our website. Fill out the contact form with your name, email, and message, and our support team will get back to you promptly. Alternatively, you can reach us via email or phone as provided on the contact page.'
    },
    {
        question: 'Are there any fees for using Haven Heights?',
        answer: 'Browsing properties on Haven Heights is free for users. However, listing properties and certain premium features may incur fees. We offer various pricing plans to accommodate different needs. Please visit our pricing page for detailed information on the available plans and their respective costs.'
    },
    {
        question: 'How secure is my data on Haven Heights?',
        answer: 'At Haven Heights, we prioritize the security of your data. We implement robust security measures, including encryption, secure servers, and regular security audits, to ensure your personal and property information is protected. Your data is handled in accordance with our privacy policy.'
    },
    { 
        question: 'How do I schedule a property viewing?',
        answer: 'To schedule a property viewing, find the property you\'re interested in and click on the "Schedule a Viewing" button. Fill out the form with your preferred date and time, and the property owner or agent will confirm the appointment. You will receive a notification once the appointment is confirmed.'
    },
    {
        question: 'Can I get a mortgage through Haven Heights?',
        answer: 'Haven Heights collaborates with several financial institutions to help users obtain mortgages. You can use our mortgage calculator to estimate your monthly payments and explore mortgage options. For detailed assistance, contact our support team or visit the "Mortgage Assistance" section on our website.'
    }
];         









$(document).ready(function() {
    faqData.forEach(function(faq, index) {
        const faqItem = `
            <div class="faq-item">
                <div class="faq-question" id="faq-question-${index}">
                    <h3>${faq.question}</h3>
                    <div id="icon-${index}" style="font-size: 1.8rem;">+</div>

                </div>
                <div class="faq-answer" id="faq-answer-${index}" style="display: none;">${faq.answer}</div>
                <hr class="faq-line" />
            </div>
        `;
        $('#faq-container-wrap').append(faqItem);

        $(`#faq-question-${index}`).click(function() {
            const answer = $(`#faq-answer-${index}`);
            const icon = $(`#icon-${index}`);
            if (answer.is(":visible")) {
                answer.hide();
                icon.text('+');
            } else {
                // Close all FAQ items
                $('.faq-answer').hide();
                $('.faq-question div').text('+');

                // Open the clicked FAQ item
                answer.show();
                icon.text('-');
            }
        });
    });
});

// FAQ END

// YEAR

function getNewYear() {
    const today = new Date();
    const year = today.getFullYear();
    return year;
}

document.getElementById("year").textContent = getNewYear();
// END

// SCROLL TO TOP
 // When the user scrolls down 20px from the top of the document, show the button
 window.onscroll = function() {scrollFunction()};

 function scrollFunction() {
     var myBtn = document.getElementById("myBtn");
     if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
         myBtn.style.display = "block";
     } else {
         myBtn.style.display = "none";
     }
 }

 // When the user clicks on the button, scroll to the top of the document smoothly
 function topFunction() {
     window.scrollTo({ top: 0, behavior: 'smooth' });
 }
// END