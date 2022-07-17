// Tests popup
const testsPopup = document.querySelector('.tests_popup')

document.querySelector('#tests_button').addEventListener('click', () => {
    testsPopup.classList.toggle('tests_popup_active')
})

document.querySelector('#schwarz_test_choose').addEventListener('click', () => {
    testsPopup.classList.toggle('tests_popup_active')
})


// Contacts popup 
const contactsPopup = document.querySelector('.contacts_popup')

document.querySelector('#contacts_button').addEventListener('click', () => {
    contactsPopup.classList.toggle('contacts_popup_active')
})

document.querySelector('#contacts_popup_exit_button').addEventListener('click', () => {
    contactsPopup.classList.toggle('contacts_popup_active')
})
