const WIDTH = 1000;
const HEIGHT = 600;

class GameScene extends Phaser.Scene {
  constructor() {
    super("game");
  }

  create() {
    /* ===== PLAYER ===== */
    this.playerSize = 50;
    this.playerSpeed = 25;

    this.player = this.add.rectangle(
      WIDTH / 2,
      HEIGHT - 100,
      this.playerSize,
      this.playerSize,
      0x0000ff
    );
    this.physics.add.existing(this.player);
    this.player.body.setCollideWorldBounds(true);

    /* ===== JUMP ===== */
    this.isJumping = false;
    this.jumpDuration = 10;
    this.jumpCounter = 0;

    /* ===== SHIELD ===== */
    this.shieldActive = true;
    this.shieldDuration = 100;
    this.shieldCooldown = 0;

    this.shieldAura = this.add.circle(
      this.player.x,
      this.player.y,
      this.playerSize + 10,
      0x00ffff,
      0.3
    );

    /* ===== BLOCKS ===== */
    this.blockSize = 50;
    this.blockSpeed = 300;
    this.blocks = this.physics.add.group();

    for (let i = 0; i < 5; i++) {
      const block = this.add.rectangle(
        Phaser.Math.Between(0, WIDTH - this.blockSize),
        Phaser.Math.Between(-HEIGHT, 0),
        this.blockSize,
        this.blockSize,
        0xff0000
      );
      this.physics.add.existing(block);
      block.body.setVelocityY(this.blockSpeed);
      this.blocks.add(block);
    }

    /* ===== SCORE ===== */
    this.score = 0;
    this.scoreText = this.add.text(10, 10, "Score: 0", {
      fontSize: "24px",
      fill: "#fff",
    });

    /* ===== INPUT ===== */
    this.keys = this.input.keyboard.addKeys("A,D,SPACE,E,R,C");

    /* ===== COLLISION ===== */
    this.physics.add.overlap(this.player, this.blocks, () => {
      if (!this.shieldActive) {
        this.gameOver();
      }
    });
  }

  update() {
    /* ===== MOVE ===== */
    if (this.keys.A.isDown) this.player.x -= this.playerSpeed;
    if (this.keys.D.isDown) this.player.x += this.playerSpeed;

    /* ===== JUMP ===== */
    if (this.keys.SPACE.isDown && !this.isJumping) {
      this.isJumping = true;
      this.jumpCounter = this.jumpDuration;
    }

    if (this.isJumping) {
      this.player.y -= 20;
      this.jumpCounter--;
      if (this.jumpCounter <= 0) {
        this.isJumping = false;
      }
    } else {
      this.player.y = HEIGHT - 100;
    }

    /* ===== SHIELD ACTIVATE ===== */
    if (this.keys.E.isDown && this.shieldCooldown <= 0) {
      this.shieldActive = true;
      this.shieldDuration = 100;
      this.shieldCooldown = 200;
    }

    if (this.shieldActive) {
      this.shieldDuration--;
      this.player.fillColor = 0x00ff00;
      if (this.shieldDuration <= 0) {
        this.shieldActive = false;
      }
    } else {
      this.player.fillColor = 0x0000ff;
    }

    if (this.shieldCooldown > 0) this.shieldCooldown--;

    /* ===== SHIELD AURA ===== */
    this.shieldAura.setVisible(this.shieldActive);
    this.shieldAura.x = this.player.x;
    this.shieldAura.y = this.player.y;

    /* ===== BLOCK UPDATE ===== */
    this.blocks.children.iterate(block => {
      if (block.y > HEIGHT) {
        block.y = Phaser.Math.Between(-HEIGHT, 0);
        block.x = Phaser.Math.Between(0, WIDTH - this.blockSize);
        this.score++;
        this.scoreText.setText("Score: " + this.score);
      }
    });
  }

  gameOver() {
    this.scene.pause();

    const text = this.add.text(
      WIDTH / 2,
      HEIGHT / 2 - 40,
      `GAME OVER\nScore: ${this.score}`,
      {
        fontSize: "48px",
        fill: "#fff",
        align: "center",
      }
    ).setOrigin(0.5);

    const hint = this.add.text(
      WIDTH / 2,
      HEIGHT / 2 + 40,
      "Press R to Restart | C to Quit",
      { fontSize: "24px", fill: "#fff" }
    ).setOrigin(0.5);

    this.input.keyboard.once("keydown-R", () => {
      this.scene.restart();
    });

    this.input.keyboard.once("keydown-C", () => {
      window.close();
    });
  }
}

/* ===== GAME CONFIG ===== */
const config = {
  type: Phaser.AUTO,
  width: WIDTH,
  height: HEIGHT,
  backgroundColor: "#000000",
  physics: {
    default: "arcade",
    arcade: { debug: false },
  },
  scene: GameScene,
};

new Phaser.Game(config);
