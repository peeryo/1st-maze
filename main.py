def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
tiles.set_tilemap(tilemap("""level1"""))
tiles.place_on_random_tile(mySprite, sprites.dungeon.stair_ladder)
scene.camera_follow_sprite(mySprite)
info.start_countdown(10)