import arcade


my_window = arcade.open_window(900,900, "First Window Demo UwU")

arcade.set_background_color(arcade.color.ARMY_GREEN)



# arcade.color.
arcade.start_render()
arcade.draw_line (100, 100, 150, 100,
                  arcade.color.LEMON, 1)
arcade.draw_lrtb_rectangle_outline (40,309,68,30,
                                   arcade.color.BUFF)
arcade.draw_circle_outline(80,230, 45,
                           arcade.color.KHAKI, 5)
arcade.draw_triangle_filled(40, 610, 140, 688, 190, 600,
                             arcade.color.YELLOW_ROSE,)
arcade.draw_arc_filled(420, 500, 567, 134,
                       arcade.color.BAKER_MILLER_PINK, 60, 340)
arcade.draw_triangle_filled(799,747, 799, 797, 759, 899,
                            arcade.color.IRRESISTIBLE)
arcade.draw_xywh_rectangle_filled(707,105,25, 135,
                                  arcade.color.RED,)
arcade.draw_xywh_rectangle_filled(657,175, 125, 20,
                                  arcade.color.RED,)
arcade.draw_circle_filled(790, 300, 45,
                          arcade.color.KHAKI,)
arcade.draw_circle_outline(790, 300, 55,
                           arcade.color.GOLD, 5)
arcade.draw_circle_outline(790, 300, 65,
                           arcade.color.QUARTZ, 7)




arcade.finish_render()

arcade.run()

