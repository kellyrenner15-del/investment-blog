document.addEventListener('DOMContentLoaded', function() {
    // LINE 按钮点击处理
    const lineButtons = document.querySelectorAll('.fixed-line-btn, .cta-button-large');
    lineButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // 打开 LINE
            if (this.getAttribute('target') === '_blank') {
                window.open(this.getAttribute('href'), '_blank');
            }
        });
    });

    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});