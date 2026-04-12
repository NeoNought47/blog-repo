// ===== 图片点击放大 =====
const overlay = document.createElement('div');
overlay.id = 'img-overlay';
const overlayImg = document.createElement('img');
overlay.appendChild(overlayImg);
document.body.appendChild(overlay);

document.querySelectorAll('img').forEach(function(img) {
  if (img.classList.contains('icon-img')) return;
  img.style.cursor = 'zoom-in';
  img.addEventListener('click', function() {
    overlayImg.src = img.src;
    overlay.classList.add('active');
  });
});

overlay.addEventListener('click', function() {
  overlay.classList.remove('active');
});

// ===== 回到顶部按钮 =====
const topBtn = document.createElement('button');
topBtn.id = 'back-to-top';
topBtn.textContent = '↑';
document.body.appendChild(topBtn);

window.addEventListener('scroll', function() {
  topBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
});

topBtn.addEventListener('click', function() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ===== 阅读进度条 =====
const bar = document.createElement('div');
bar.id = 'progress-bar';
document.body.appendChild(bar);

window.addEventListener('scroll', function() {
  const scrollTop = window.scrollY;
  const docHeight = document.body.scrollHeight - window.innerHeight;
  const progress = (scrollTop / docHeight) * 100;
  bar.style.width = progress + '%';
});

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
