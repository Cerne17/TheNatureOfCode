let walker;

function setup() {
  createCanvas(600, 600);
  walker = new Walker();
  background(220, 200, 250);
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

  show() {
    stroke(0);
    strokeWeight(4);
    point(this.x, this.y);
  }

  step() {
    let xstep, ystep;
    let choice = random(0, 1);
    if (choice < 0.5) {
      xstep = floor(random(-1, 1));
      ystep = floor(random(-1, 1));
    }
    else {
      if (mouseX <= this.x) {
        xstep = -1;
      } else {
        xstep = 1;
      }
      if (mouseY <= this.y) {
        ystep = -1;
      }
      else {
        ystep = 1;
      }
    }
    this.x += xstep;
    this.y += ystep;

    this.x = this.x % width;
    this.y = this.y % height;
  }
}