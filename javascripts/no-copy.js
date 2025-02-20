// 禁止右键点击
// document.addEventListener('contextmenu', function (e) {
//     e.preventDefault();
// });

// document.addEventListener('copy', function (e) {
//     e.preventDefault();
// });
document.addEventListener('dragstart', function (e) {
    e.preventDefault();
});