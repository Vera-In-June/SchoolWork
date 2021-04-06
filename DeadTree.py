import arcade

arcade.open_window(800, 600, "Dead tree by the river")
# skybox
arcade.set_background_color((95, 46, 163))
arcade.start_render()
# field
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, (25, 115, 27))
# river
arcade.draw_polygon_filled(((400, 300),
                            (380, 300),
                            (390, 200),
                            (360, 0),
                            (600, 0)
                            ),
                           arcade.csscolor.DODGER_BLUE)
# tree trunk
arcade.draw_polygon_filled(((340, 200),
                            (350, 190),
                            (390, 310),
                            (450, 330),
                            (380, 317)
                            ),
                           arcade.csscolor.SADDLE_BROWN)
# tree trunk shade
arcade.draw_polygon_filled(((350, 190),
                            (360, 200),
                            (395, 300),
                            (450, 330),
                            (390, 310)
                            ),
                           arcade.csscolor.BROWN)
# tree branch
arcade.draw_polygon_filled(((380, 317),
                            (340, 345),
                            (350, 370),
                            (348, 346),
                            (385, 317)
                            ),
                           arcade.csscolor.SADDLE_BROWN)
# tree branch shade
arcade.draw_polygon_filled(((385, 317),
                            (390, 318),
                            (353, 346),
                            (350, 370),
                            (348, 346),
                            (385, 317)
                            ),
                           arcade.csscolor.BROWN)
arcade.finish_render()

arcade.run()
