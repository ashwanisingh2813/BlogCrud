document.addEventListener('DOMContentLoaded', function () {
    var shareIcons = document.querySelectorAll('.post-share');

    shareIcons.forEach(function (icon) {
      icon.addEventListener('click', function () {
        var postContent = icon.closest('.blog-post').querySelector('.down-content p').innerText;

        if (navigator.share) {
          navigator.share({
            title: 'Share Post',
            text: postContent,
            url: window.location.href
          })
          .then(() => console.log('Successful share'))
          .catch((error) => console.log('Error sharing:', error));
        } else {
          alert('Sharing not supported in this browser.');
        }
      });
    });
  });

