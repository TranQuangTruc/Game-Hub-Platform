document.addEventListener('DOMContentLoaded', function () {
    const body = document.querySelector('body');
    const snowflakes = [];

    for (let i = 0; i < 100; i++) {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.style.left = Math.random() * window.innerWidth + 'px';
        snowflake.style.animationDelay = Math.random() * 5 + 's';
        snowflake.style.animationDuration = Math.random() * 3 + 3 + 's';
        body.appendChild(snowflake);
        snowflakes.push(snowflake);
    }
});

// CSS animation for snowflakes
const style = document.createElement('style');
style.innerHTML = `
    .snowflake {
        position: absolute;
        top: -10px;
        width: 10px;
        height: 10px;
        background: white;
        border-radius: 50%;
        animation: fall linear infinite;
    }

    @keyframes fall {
        to {
            transform: translateY(100vh);
        }
    }
`;
document.head.appendChild(style);
