// js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Ví dụ: Thêm class 'scrolled' cho navbar khi cuộn trang
    const navbar = document.querySelector('.custom-navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        });
    }

    // Bạn có thể thêm các chức năng JavaScript khác tại đây,
    // ví dụ: xử lý click các nút điều hướng chương (nếu có nội dung động)
});
