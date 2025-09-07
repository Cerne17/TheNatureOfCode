function setup() {
  createCanvas(400, 400);
}

function draw() {
  let x = randomGaussian(width / 2, 20); // let x = 20 * randomGaussian() + (width / 2);
  noStroke();
  fill(0, 10);
  circle(x, height / 2, 16, 16);
}
