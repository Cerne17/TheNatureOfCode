let randomCounts = [];
let total = 20; // Number of counts to generate

function setup() {
  createCanvas(640, 240);
  for (let i = 0; i < total; i++) {
    randomCounts[i] = 0;
  }
}

function draw() {
  background(255);
  let index = floor(random(randomCounts.length + 1));
  randomCounts[index]++;

  stroke(0);
  fill(177);
  let w = width / randomCounts.length;

  for (let i = 0; i < randomCounts.length; i++) {
    rect(i * w, height - randomCounts[i], w - 1, randomCounts[i]);
  }
}
