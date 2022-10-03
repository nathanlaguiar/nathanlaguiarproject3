import arcade


my_window = arcade.open_window(650,600, "First Window Demo UwU")

arcade.set_background_color(arcade.color.ARMY_GREEN)



# arcade.color.
arcade.start_render()
arcade.draw_xywh_rectangle_filled(0,400, 650, 250,
                                  arcade.color.BLACK,)
arcade.draw_line (100, 100, 150, 100,
                  arcade.color.BAKER_MILLER_PINK, 6)


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
#THE FOLLOWING YELLOW OUTLINE IS THE SUPER AMAZING TRACTOR BEAM THAT TOOK FAR TOO LONG TO CENTER.
# DO NOT MOVE IT!!!
arcade.draw_triangle_outline(40, 110, 295, 440, 590, 100,
                             arcade.color.YELLOW_ROSE,)
arcade.draw_arc_filled(290, 500, 67, 34,
                       arcade.color.LEMON, 60, 340)
arcade.draw_triangle_outline(199,147, 199, 197, 159, 199,
                            arcade.color.IRRESISTIBLE)
arcade.draw_xywh_rectangle_filled(107,105,25, 35,
                                  arcade.color.TROLLEY_GREY,)



arcade.draw_circle_filled(590, 545, 50,
                           arcade.color.GHOST_WHITE,)
arcade.draw_text("Nathan L Aguiar", 450,50)



arcade.finish_render()

arcade.run()

