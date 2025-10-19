const input = document.getElementById('input')
function search() {
    if (input.value === '') {
        alert("البحث فارغ تماما, اكتب شيء للبحث عنه");
    }
    else {
        window.open(`https://www.google.com/search?q=${input.value}`);
    }
}
function clearinput() {
    input.value = '';
}