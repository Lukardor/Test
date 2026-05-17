const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');

const weatherTypes = ['Sonne', 'Regen', 'Nebel', 'Gewitter', 'Schnee', 'Sandsturm'];
const biomes = [
  { name: 'Großstadt', color: '#4b5569' },
  { name: 'Dörfer', color: '#5f7a59' },
  { name: 'Autobahnen', color: '#3e4f76' },
  { name: 'Berge', color: '#6d6b63' },
  { name: 'Wüste', color: '#8c6d39' },
  { name: 'Wald', color: '#365e3a' },
  { name: 'Küstenstraßen', color: '#315f82' },
  { name: 'Rennstrecken', color: '#7a3131' },
];

const car = { x: 640, y: 360, angle: 0, speed: 0, maxSpeed: 380 };
const input = { w: false, s: false, a: false, d: false };
let tick = 0;
let players = 1;

const eventsEl = document.getElementById('events');
const speedEl = document.getElementById('speed');
const weatherEl = document.getElementById('weather');
const timeEl = document.getElementById('time');
const playersEl = document.getElementById('players');

function addEvent(text) {
  const li = document.createElement('li');
  li.textContent = text;
  eventsEl.prepend(li);
  while (eventsEl.children.length > 20) eventsEl.removeChild(eventsEl.lastChild);
}

window.addEventListener('keydown', (e) => { if (e.key in input) input[e.key] = true; });
window.addEventListener('keyup', (e) => { if (e.key in input) input[e.key] = false; });

function update() {
  tick += 1;
  const weather = weatherTypes[Math.floor(tick / 600) % weatherTypes.length];
  const isNight = Math.floor(tick / 900) % 2 === 1;

  const grip = weather === 'Schnee' ? 0.65 : weather === 'Regen' ? 0.8 : 1;
  if (input.w) car.speed += 0.9 * grip;
  if (input.s) car.speed -= 1.2;
  car.speed *= 0.985;
  car.speed = Math.max(0, Math.min(car.maxSpeed, car.speed));

  if (input.a) car.angle -= 0.028 * (car.speed / 80 + 0.2);
  if (input.d) car.angle += 0.028 * (car.speed / 80 + 0.2);

  car.x += Math.cos(car.angle) * (car.speed / 12);
  car.y += Math.sin(car.angle) * (car.speed / 12);
  car.x = (car.x + canvas.width) % canvas.width;
  car.y = (car.y + canvas.height) % canvas.height;

  if (tick % 300 === 0) {
    players = Math.min(100, players + Math.floor(Math.random() * 5));
    addEvent(`Dynamisches Event: ${['Drift-Zone', 'Straßenrennen', 'Offroad Sprint', 'Drag Race'][Math.floor(Math.random() * 4)]} gestartet.`);
  }

  speedEl.textContent = `${Math.round(car.speed)} km/h`;
  weatherEl.textContent = `Wetter: ${weather}`;
  timeEl.textContent = `Zeit: ${isNight ? 'Nacht' : 'Tag'}`;
  playersEl.textContent = `Server: ${players}/100`;

  render(weather, isNight);
  requestAnimationFrame(update);
}

function render(weather, isNight) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = isNight ? '#0d1424' : '#1c2a40';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  biomes.forEach((b, i) => {
    ctx.fillStyle = b.color;
    ctx.globalAlpha = 0.65;
    ctx.fillRect((i % 4) * 320 + 10, Math.floor(i / 4) * 350 + 10, 300, 330);
    ctx.globalAlpha = 1;
    ctx.fillStyle = '#fff';
    ctx.font = '16px sans-serif';
    ctx.fillText(b.name, (i % 4) * 320 + 20, Math.floor(i / 4) * 350 + 35);
  });

  if (weather === 'Regen' || weather === 'Gewitter') {
    ctx.strokeStyle = 'rgba(180,220,255,0.35)';
    for (let i = 0; i < 160; i++) {
      const x = (i * 47 + tick * 3) % canvas.width;
      const y = (i * 29 + tick * 6) % canvas.height;
      ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x - 4, y + 12); ctx.stroke();
    }
  }

  ctx.save();
  ctx.translate(car.x, car.y);
  ctx.rotate(car.angle);
  ctx.fillStyle = '#ff4d4d';
  ctx.fillRect(-16, -8, 32, 16);
  ctx.fillStyle = '#222';
  ctx.fillRect(-14, -10, 8, 4); ctx.fillRect(6, -10, 8, 4);
  ctx.fillRect(-14, 6, 8, 4); ctx.fillRect(6, 6, 8, 4);
  ctx.restore();
}

addEvent('Willkommen beim Horizon Festival 6.');
addEvent('700+ Fahrzeugklassen im Garage-System vorgesehen.');
addEvent('Open World mit Stadt, Wüste, Berg, Wald und Küste aktiv.');
update();
