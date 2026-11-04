"""Course-owned local-video player using Deckgen's existing live-frame API."""

PRODUCT_VIDEO = r"""
function setup() {
  noCanvas();
  noLoop();
  const video = document.createElement('video');
  video.src = '../../week10-nicolo-media/product-demo.mp4';
  video.poster = '../../week10-nicolo-media/product-video-poster.png';
  video.controls = true;
  video.playsInline = true;
  video.preload = 'metadata';
  video.setAttribute('aria-label', 'Original product promotional video');
  const standalone = self === top;
  Object.assign(video.style, {
    position: 'absolute', left: '0', top: standalone ? '44px' : '0',
    width: '100%', height: standalone ? 'calc(100% - 44px)' : '100%',
    objectFit: 'contain', background: '#000B1C'
  });
  document.body.appendChild(video);
  // Native controls own their keys; the slide shell must not turn Space into Next.
  video.addEventListener('keydown', event => {
    event.stopPropagation();
    if (event.key === 'Escape') video.pause();
  });
  const pause = () => video.pause();
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pause();
  });
  if (!standalone && parent.Reveal) {
    const onSlide = () => {
      if (!frameElement.closest('section').classList.contains('present')) pause();
    };
    const observer = new MutationObserver(() => {
      if (parent.document.body.classList.contains('ho')) pause();
    });
    parent.Reveal.on('slidechanged', onSlide);
    observer.observe(parent.document.body, {attributes: true, attributeFilter: ['class']});
    addEventListener('pagehide', () => {
      parent.Reveal.off('slidechanged', onSlide);
      observer.disconnect();
      pause();
    }, {once: true});
  }
}
"""
