let splatter;

function setup() {
  createCanvas(800, 600);
  splatter = new PaintSplatter();
}

function draw() {
  splatter.step();
  splatter.draw();
}

class PaintSplatter {
  constructor() {
    this.x = this.setX();
    this.y = this.setY();
    this.size = this.setSize();
    this.color = this.setColor();
  }

  setX() {
    this.x = randomGaussian(width / 2, width / 6) % width;
  }

  setY() {
    this.y = randomGaussian(height / 2, height / 6) % height;
  }

  setSize() {
    this.size = randomGaussian(30, 9);
  }

  setColor() {
    this.color = color(randomGaussian(100, 50), randomGaussian(100, 50), randomGaussian(100, 50), 100);
  }

  step() {
    this.setX();
    this.setY();
    this.setSize();
    this.setColor();
  }

  draw() {
    noStroke();
    fill(this.color);
    circle(this.x, this.y, this.size);
  }
}
