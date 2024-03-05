// Configuramos el lienzo
const canvas = document.getElementById("canvas-container");
const app = new PIXI.Application({
  view: canvas,
  width: 500,
  height: 500,
});

// Cargamos las texturas
const spriteSheet = PIXI.Texture.from("spritesheet.png");
const caballoSprite = new PIXI.Sprite(spriteSheet);
const jineteSprite = new PIXI.Sprite(spriteSheet);

// Posicionamos y escalamos los sprites
caballoSprite.x = 100;
caballoSprite.y = 100;
caballoSprite.scale.set(2);
jineteSprite.x = 120;
jineteSprite.y = 80;
jineteSprite.scale.set(1.5);

// Animamos al caballo
const caballoAnim = new PIXI.AnimatedSprite(spriteSheet, [
  0, 1, 2, 3, 4, 5, 6, 7,
]);
caballoAnim.x = 100;
caballoAnim.y = 100;
caballoAnim.scale.set(2);
caballoAnim.animationSpeed = 0.1;
caballoAnim.play();

// Agregamos los sprites al escenario
app.stage.addChild(caballoSprite);
app.stage.addChild(jineteSprite);
app.stage.addChild(caballoAnim);

// Función para actualizar la animación
app.ticker.add(() => {
  // Rotamos al caballo
  caballoSprite.rotation += 0.01;

  // Actualizamos la animación del caballo
  caballoAnim.update();
});
