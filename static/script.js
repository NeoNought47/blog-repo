// ===== 夜间模式切换功能 =====

// 等待页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {

    // 获取按钮元素
    const toggleButton = document.getElementById('theme-toggle');

    // 页面加载时检查用户之前的选择
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
        toggleButton.textContent = '☀️';
    }

    // 点击按钮切换主题
    toggleButton.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');

        // 更新按钮图标
        if (document.body.classList.contains('dark-mode')) {
            toggleButton.textContent = '☀️';
            localStorage.setItem('theme', 'dark');
        } else {
            toggleButton.textContent = '🌙';
            localStorage.setItem('theme', 'light');
        }
    });

});
