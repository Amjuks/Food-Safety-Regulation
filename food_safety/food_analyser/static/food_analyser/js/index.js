document.addEventListener('DOMContentLoaded', () => {
    const imageInput = document.querySelector('#imageInput');
    const preview = document.getElementById('preview');

    imageInput.addEventListener('input', () => {
        const file = imageInput.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function(e) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            };

            reader.readAsDataURL(file);
        } else {
            preview.style.display = 'none';
        }
    })

    imageInput.dispatchEvent(new Event('input'));
})