function goToPage(url) {
    window.location.href = url;
}

function goBack() {
    window.location.href = 'index.html';
}

function goToLink(type) {
    let url = "";
    switch(type) {
        case 'spotify':
            url = "https://open.spotify.com/playlist/4i5m8sqVZV8fZjfyisXJ3X?si=fdc4e1a33505425a&pt=a0d00049ed4a86818eb83cda58a79235";
            break;
        case 'sketchtoy':
            url = "http://sketchtoy.com/71465749";
            break;
        case 'sendthesong':
            url = "https://sendthesong.xyz/details/6986116ca371d3479e1cc4d2";
            break;
        case 'others':
            url = "https://gifft.me/o/e/wy8gzrph2nrq6n0cuou82cwt";
            break;
    }
    if(url) window.open(url, '_blank');
}