// Teaching schematic: whole-word toy tokens, no measured attention weights.
const words = ['A', 'robot', 'writes', 'a', 'brief'];
const targets = ['robot', 'writes', 'a', 'brief', '.'];
const ink = '#000B1C', teal = '#246E70', violet = '#943890';
const paper = '#F4F4F2', orange = '#ED6D24', muted = '#5C6470';
let stage = 0, selected = 2, started = -1, generated = 1, font;
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function preload() { font = loadFont('../../vendor/fonts/Inter-Variable.ttf'); }
function setup() {
  createCanvas(1680, 640); pixelDensity(1); textFont(font); frameRate(30);
  const c = document.querySelector('canvas');
  c.tabIndex = 0; c.setAttribute('role', 'img');
  c.setAttribute('aria-label', 'Interactive Transformer explanation. Keys 1 to 4 select tokens, context, training or generation. Space replays. In context, click a token or use left and right arrows.');
}
function label(t, x, y, size = 30, color = ink, align = LEFT) {
  noStroke(); fill(color); textSize(size); textAlign(align, CENTER); text(t, x, y);
}
function tile(x, y, w, h, t, active = false, faded = false) {
  stroke(active ? teal : '#CED4D5'); strokeWeight(active ? 3 : 2);
  fill(active ? '#E5F0ED' : faded ? '#EBECEA' : '#FFFFFF'); rect(x,y,w,h,14);
  label(t,x+w/2,y+h/2,40,faded ? muted : ink,CENTER);
}
function switchStage(n) { stage=n; started=-1; generated=1; }
function play() { started=millis(); generated=1; }
function draw() {
  background(paper);
  ['1  Tokens','2  Context','3  Training','4  Generation'].forEach((t,i) => {
    noStroke(); fill(stage===i ? ink : '#E4E7E5'); rect(20+i*350,8,330,64,12);
    label(t,185+i*350,40,28,stage===i ? '#FFFFFF' : ink,CENTER);
  });
  noStroke(); fill(orange); rect(1430,8,230,64,12);
  label(stage<2 ? 'NEXT →' : 'REPLAY ↻',1545,40,27,ink,CENTER);
  const elapsed=started<0 ? 0 : millis()-started;
  if(stage===3 && started>=0) generated=reduced ? 5 : min(5,1+floor(elapsed/1000));
  words.forEach((w,i) => {
    const visible=stage!==3 || i<generated;
    if(visible) tile(35+i*328,145,298,100,w,stage===1 && i===selected,stage===1 && i>selected);
    else { noFill(); stroke('#CDD2D0'); strokeWeight(2); rect(35+i*328,145,298,100,14); }
    label('POSITION '+(i+1),184+i*328,117,21,muted,CENTER);
  });
  if(stage===0) {
    label('Text becomes a sequence of tokens.',840,345,46,ink,CENTER);
    label('A token may be a word, part of a word, or punctuation.',840,420,32,muted,CENTER);
    label('This small example uses whole words. Order matters.',840,565,28,teal,CENTER);
  }
  if(stage===1) {
    const cx=184+selected*328;
    for(let j=0;j<=selected;j++) {
      const x=184+j*328; noFill(); stroke(teal); strokeWeight(4);
      bezier(x,250,x,330,cx,320,cx,382);
      if(!reduced) { const t=(millis()%2400)/2400; noStroke(); fill(orange);
        circle(bezierPoint(x,x,cx,cx,t),bezierPoint(250,330,320,382,t),13); }
    }
    tile(cx-140,392,280,78,words[selected],true);
    label('Click a token: it can use itself and earlier tokens.',840,535,34,ink,CENTER);
    label('Later tokens are hidden. Connections show access, not attention strength.',840,578,26,muted,CENTER);
  }
  if(stage===2) {
    const p=started<0 ? 1 : reduced ? 1 : min(1,elapsed/2400);
    words.forEach((w,i) => {
      const x=184+i*328; stroke(teal); strokeWeight(4); line(x,257,x,399);
      if(p<1) { noStroke(); fill(orange); circle(x,265+124*p,20); }
      noStroke(); fill(paper); rect(x-145,282,290,45);
      label('predict → compare',x,305,22,ink,CENTER);
      if(p>0.75) { tile(x-149,390,298,87,targets[i],true); }
    });
    label('Known next tokens are the training targets.',840,522,32,ink,CENTER);
    label('All positions work in parallel; errors guide changes to the weights.',840,568,28,teal,CENTER);
  }
  if(stage===3) {
    label(words.slice(0,generated).join(' ')+(generated===5 ? '.' : ' ▌'),840,355,60,ink,CENTER);
    label('Predict → choose one token → append → repeat.',840,468,36,teal,CENTER);
    label('Writing a new reply still proceeds one token at a time.',840,575,31,muted,CENTER);
  }
}
function mousePressed() {
  if(mouseY>=8 && mouseY<=72) {
    if(mouseX>=20 && mouseX<1400) switchStage(floor((mouseX-20)/350));
    if(mouseX>=1430 && mouseX<=1660) { if(stage<2) switchStage(stage+1); else play(); }
  }
  if(stage===1 && mouseY>=145 && mouseY<=245 && mouseX>=35 && mouseX<=1645)
    selected=constrain(floor((mouseX-35)/328),0,4);
  return false;
}
function keyPressed() {
  if(['1','2','3','4'].includes(key)) { switchStage(Number(key)-1); return false; }
  if(key===' ') { if(stage<2) switchStage(stage+1); else play(); return false; }
  if(stage===1 && (keyCode===LEFT_ARROW || keyCode===RIGHT_ARROW)) {
    selected=constrain(selected+(keyCode===RIGHT_ARROW?1:-1),0,4); return false;
  }
}
