document.addEventListener('DOMContentLoaded', (event) => {
    const toggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');
    
    if (currentTheme) {
        document.body.classList.add(currentTheme);
    }
    toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        let theme = 'light';
        if (document.body.classList.contains('light-mode')) {
            theme = 'dark';
        }
        localStorage.setItem('theme', theme);
    });
});
