// //file path opener
document.querySelector('#file_path_button').addEventListener('click', async() => {
    document.querySelector('#file_path_input').value = await eel.open_file_path()()
})


// //save path opener
document.querySelector('#save_path_button').addEventListener('click', async() => {
    document.querySelector('#save_path_input').value = await eel.open_dir_path()()
})


//settings collector
function collecSettings() {
    let filePath = document.querySelector('#file_path_input').value
    let savePath = document.querySelector('#save_path_input').value
    let jsonCheck = document.querySelector('#json_checkbox').checked
    let csvCheck = document.querySelector('#csv_checkbox').checked
    let xlsxCheck = document.querySelector('#xlsx_checkbox').checked

    return {
        'file_path': filePath,
        'save_path': savePath,
        'file_format': {
            'json': jsonCheck,
            'csv': csvCheck,
            'xlsx': xlsxCheck
        }
    }
}

//call python code
document.querySelector('#process_button').addEventListener('click', async() => {
    let settings = collecSettings()
    if (settings['file_path'] === '') {
        document.querySelector('.error_popup').classList.toggle('error_popup_active')
        document.querySelector('#error_message').textContent = 'Choose file'
    } else if (settings['save_path'] === '') {
        document.querySelector('.error_popup').classList.toggle('error_popup_active')
        document.querySelector('#error_message').textContent = 'Choose save folder'
    } else {
        alert('ok')
    }
    // await eel.send_data_to_python()
})
