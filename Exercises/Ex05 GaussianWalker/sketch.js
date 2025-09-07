let walker;

function setup() {
  createCanvas(400, 400);
  walker = new Walker();
}

function draw() {
  walker.step();
  walker.show();
}

class Walker {
  constructor() {
    this.x = width / 2;
    this.y = height / 2;
  }

  step() {
    this.x += randomGaussian(0, 2);
    this.y += randomGaussian(0, 2);
  }

  show() {
    stroke(0);
    strokeWeight(2);
    point(this.x, this.y);
  }
}