let walker;

function setup() {
  createCanvas(400, 400);
  walker = new Walker();
  background(230, 230, 245);
}

function draw() {
  // background(255);
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
    let xstep = 2 * random(-1, 1);
    let ystep = 2 * random(-1, 1);
    this.x += xstep;
    this.y += ystep;
  }

  // step() {
  //   let choice = floor(random(4));
  //   if (choice === 0) {
  //     this.x++;
  //   } else if (choice === 1) {
  //     this.x--;
  //   } else if (choice === 2) {
  //     this.y++;
  //   } else {
  //     this.y--;
  //   }
}

