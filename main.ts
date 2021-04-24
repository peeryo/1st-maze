scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    game.over(true)
})
let mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . 8 8 . . 8 8 . . . . 
    . . . . . . 8 2 7 7 2 8 . . . . 
    . . . . 8 8 8 8 8 8 8 8 8 8 . . 
    . . . . f 3 3 4 3 3 4 3 3 f . . 
    . . . . . f 6 4 4 4 4 6 f . . . 
    . . . . . . 6 6 4 4 6 6 . . . . 
    . . . . . . . f 4 4 f . . . . . 
    . . . . . . . . e e . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
tiles.setTilemap(tilemap`level1`)
tiles.placeOnRandomTile(mySprite, sprites.dungeon.stairLadder)
scene.cameraFollowSprite(mySprite)
info.startCountdown(10)
