'use strict';

const theme = localStorage.getItem('theme');
if (theme === null) {
    setTheme('light')
} else {
    setTheme(theme)
}

const themeDots = document.querySelectorAll('.theme-dot');
for (let i=0; i < themeDots.length; i++) {
    themeDots[i].addEventListener('click', function () {
        let mode = this.dataset.mode;
        setTheme(mode)
    })
}

function setTheme(mode) {
    if (mode === 'light') {
        document.querySelector('#theme-style').href = 'static/css/default.css'
    }
    if (mode === 'blue') {
        document.querySelector('#theme-style').href = 'static/css/blue.css'
    }
    if (mode === 'green') {
        document.querySelector('#theme-style').href = 'static/css/green.css'
    }
    if (mode === 'purple') {
        document.querySelector('#theme-style').href = 'static/css/purple.css'
    }
    localStorage.setItem('theme', mode);
}