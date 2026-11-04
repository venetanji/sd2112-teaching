"""Course-owned local-video player using Deckgen's existing live-frame API."""

PRODUCT_VIDEO = r"""
function setup() {
  noCanvas();
  noLoop();
  const video = document.createElement('video');
  video.src = '../../week10-nicolo-media/product-demo.mp4';
  video.poster = '../../week10-nicolo-media/product-video-poster.png';
  video.controls = true;
  video.loop = true;
  video.autoplay = true;
  video.muted = true;
  video.playsInline = true;
  video.preload = 'metadata';
  video.setAttribute('aria-label', 'Original product promotional video; Space to play or pause');
  const standalone = self === top;
  Object.assign(video.style, {
    position: 'absolute', left: '0', top: standalone ? '44px' : '0',
    width: '100%', height: standalone ? 'calc(100% - 44px)' : '100%',
    objectFit: 'contain', background: '#000B1C'
  });
  document.body.appendChild(video);
  const pause = () => video.pause();
  const active = () => standalone || (
    frameElement.closest('section').classList.contains('present') &&
    !parent.document.body.classList.contains('ho') && !parent.Reveal.isOverview()
  );
  // Capture before native controls and Reveal's embed forwarding: one key, one toggle.
  const onKey = event => {
    if (!active() || event.ctrlKey || event.altKey || event.metaKey) return;
    const target = event.target;
    if (target && (target.isContentEditable || /^(INPUT|TEXTAREA|SELECT|BUTTON)$/.test(target.tagName))) return;
    if (event.code !== 'Space' && event.key !== ' ') return;
    event.preventDefault();
    event.stopImmediatePropagation();
    if (event.repeat) return;
    if (video.paused) video.play().catch(() => {});
    else pause();
  };
  window.addEventListener('keydown', onKey, true);
  video.addEventListener('play', () => { if (!active()) pause(); });
  const onVisibility = () => { if (document.hidden) pause(); };
  document.addEventListener('visibilitychange', onVisibility);
  if (!standalone && parent.Reveal) {
    // Only this course-owned player omits the generic LIVE overlay.
    const chip = frameElement.parentElement.querySelector('.live');
    if (chip) chip.style.display = 'none';
    parent.window.addEventListener('keydown', onKey, true);
    const onSlide = () => {
      if (active()) video.play().catch(() => {});
      else pause();
    };
    const observer = new MutationObserver(() => { if (!active()) pause(); });
    parent.Reveal.on('slidechanged', onSlide);
    parent.Reveal.on('overviewshown', pause);
    observer.observe(parent.document.body, {attributes: true, attributeFilter: ['class']});
    addEventListener('pagehide', () => {
      parent.window.removeEventListener('keydown', onKey, true);
      window.removeEventListener('keydown', onKey, true);
      document.removeEventListener('visibilitychange', onVisibility);
      parent.Reveal.off('slidechanged', onSlide);
      parent.Reveal.off('overviewshown', pause);
      observer.disconnect();
      pause();
    }, {once: true});
  }
  if (active()) video.play().catch(() => {});
}
"""
