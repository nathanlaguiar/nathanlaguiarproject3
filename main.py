import arcade


my_window = arcade.open_window(650,600, "First Window Demo UwU")

arcade.set_background_color(arcade.color.ARMY_GREEN)



# arcade.color.
arcade.start_render()
arcade.draw_xywh_rectangle_filled(0,400, 650, 250,
                                  arcade.color.EERIE_BLACK,)



arcade.draw_circle_outline(287,492, 49,
                           arcade.color.KHAKI, 6)
# THE ABOVE CIRCLE IS THE COVER OF PACMAN'S UFO, WHY PACMAN IS FLYING A UFO IS BEYOND ME
arcade.draw_circle_filled(378, 462, 19,
                          arcade.color.RED,)
arcade.draw_circle_filled(200, 462, 19,
                           arcade.color.BLUEBERRY, 4)
#the above circles were wheels for a car but became edges of the ufo
arcade.draw_lrtb_rectangle_filled (200,379,480,443,
                                   arcade.color.BUFF)
arcade.draw_line (240, 40, 240, 160,
                  arcade.color.DIRT, 30)
arcade.draw_line (0, 20, 650, 20,
                  arcade.color.BLACK, 40)
#THE FOLLOWING YELLOW OUTLINE IS THE SUPER AMAZING TRACTOR BEAM THAT TOOK FAR TOO LONG TO CENTER.
# DO NOT MOVE IT!!!
arcade.draw_triangle_outline(40, 110, 290, 440, 590, 100,
                             arcade.color.YELLOW_ROSE,)

arcade.draw_xywh_rectangle_filled(207,200,75, 75,
                                  arcade.color.RUBY_RED,)
arcade.draw_line (220, 202, 270, 235,
                  arcade.color.WOOD_BROWN, 6)
arcade.draw_line (220, 235, 270, 202,
                  arcade.color.WOOD_BROWN, 6)
arcade.draw_line (270, 200, 270, 238,
                  arcade.color.WOOD_BROWN, 5)
arcade.draw_line (220, 238, 220, 200,
                  arcade.color.WOOD_BROWN, 5)
arcade.draw_line (220, 235, 270, 235,
                  arcade.color.WOOD_BROWN, 6)
arcade.draw_arc_filled(290, 500, 67, 34,
                       arcade.color.LEMON, 60, 340)
arcade.draw_triangle_filled(319, 275, 267, 315, 220,307,
                            arcade.color.RUBY_RED, )
arcade.draw_circle_filled(370, 275, 10,
                           arcade.color.GHOST_WHITE)
arcade.draw_line (376, 273, 375, 260,
                  arcade.color.BLACK, 2)
#a
arcade.draw_line (365, 273, 360, 260,
                  arcade.color.BLACK, 2)

#cow will haunt me forever
arcade.draw_triangle_filled(378, 289, 381, 294, 383, 289,
                            arcade.color.BLACK, )
arcade.draw_circle_filled(380, 285, 5,
                           arcade.color.GHOST_WHITE)
arcade.draw_circle_filled(382, 286, 2,
                           arcade.color.BLACK)

arcade.draw_triangle_filled(370, 282, 358, 276, 358, 283,
                            arcade.color.GHOST_WHITE, )
arcade.draw_circle_filled(370, 281, 4,
                           arcade.color.BLACK)
arcade.draw_circle_filled(375, 279, 3,
                           arcade.color.BLACK)
arcade.draw_circle_filled(370, 281, 4,
                           arcade.color.BLACK)
arcade.draw_circle_filled(365, 280, 3,
                           arcade.color.BLACK)
arcade.draw_circle_filled(368, 274, 3,
                           arcade.color.BLACK)
arcade.draw_circle_filled(385, 284, 2,
                           arcade.color.RUBY_RED)








arcade.draw_circle_filled(590, 545, 50,
                           arcade.color.GHOST_WHITE,)
arcade.draw_text("Nathan L Aguiar", 450,15)



arcade.finish_render()

arcade.run()

