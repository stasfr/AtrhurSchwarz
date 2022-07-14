// Tests popup
const testsPopup = document.querySelector('.tests_popup')

document.querySelector('#tests_button').addEventListener('click', () => {
    testsPopup.style.display = 'flex'
})

document.querySelector('#schwarz_test_choose').addEventListener('click', () => {
    testsPopup.style.display = 'none'
})

// Contacts popup 
const contactsPopup = document.querySelector('.contacts_popup')

document.querySelector('#contacts_button').addEventListener('click', () => {
    contactsPopup.style.display = 'flex'
})

document.querySelector('#contacts_popup_exit_button').addEventListener('click', () => {
    contactsPopup.style.display = 'none'
})
