function main(method = 2) {
    const text = $('#plain-text').val();
    const encrypted = $('#encrypted-text');
    var hash;
    switch (method) {
        case 1: hash = md4(text); break;
        case 2: hash = CryptoJS.MD5(text); break;
        case 3: hash = CryptoJS.SHA1(text); break;
        case 4: hash = CryptoJS.SHA256(text); break;
        case 5: hash = CryptoJS.HmacSHA256(text); break;
    }
    encrypted.val(hash);
}

// setting navbar
function setActive(page = "link1") {
    $('.nav-link').each( function () {
        this.classList.remove('active');
    })
    document.getElementById(page).classList.add('active');
}

function navigation() {
    document.getElementById("link1").classList.add('active');
    $('#hash-name').text('MD4');

    $('.nav-link').each( function () {
        $(this).on('click', function (e) {
            var page = $(this).attr('id');
            setActive(page);

            switch (page) {
                case 'link1': $('#hash-name').text('MD4'); break;
                case 'link2': $('#hash-name').text('MD5'); break;
                case 'link3': $('#hash-name').text('SHA1'); break;
                case 'link4': $('#hash-name').text('SHA256'); break;
                case 'link5': $('#hash-name').text('HMAC'); break;
                default: $('#hash-name').text('MD4'); break;
            }
        });
    });
}

navigation();

//setting submit btn
$('#generator-btn').on('click', function (e) {
    e.preventDefault();
    $('.nav-link').each(function () {
        if (this.classList.contains("active")) {
            main(parseInt(this.id.slice(-1)));
        }
    })
})
