let walker;

function setup() {
  createCanvas(600, 400);
  walker = new Walker();
}

function draw() {
  walker.show();
  walker.step();
}

class Walker {
  constructor() {
    this.x = width / 2;
    this.y = height / 2;
  }

  show() {
    stroke(0);
    point(this.x, this.y);
  }

  step() {
    let xstep = floor(random(-1.5, 3));
    let ystep = floor(random(-1.5, 3));
    this.x += xstep;
    this.y += ystep;
    this.x = this.x % width;
    this.y = this.y % height;
  }
}