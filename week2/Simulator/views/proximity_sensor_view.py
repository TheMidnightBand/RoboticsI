#!/usr/bin/python
# -*- Encoding: utf-8 -*

from math import *
import Euv.Shapes as Shapes

class ProximitySensorView:

  def __init__( self, viewer, proximity_sensor ):
    self.viewer = viewer
    self.proximity_sensor = proximity_sensor

  def draw_proximity_sensor_to_frame( self, frame ):
    # grab proximity sensor pose values
    sensor_x, sensor_y, sensor_theta = self.proximity_sensor.pose.unpack()

    # build the sensor cone
    r = self.proximity_sensor.max_range
    phi = self.proximity_sensor.phi_view
    sensor_cone_poly = [ [0.0, 0.0],
                         [r*cos(-phi/2), r*sin(-phi/2)],
                         [r, 0.0],
                         [r*cos(phi/2), r*sin(phi/2)] ]
    sensor_cone_poly = Shapes.rotate_and_move_poly( sensor_cone_poly,
                                                    sensor_theta,
                                                    [ sensor_x, sensor_y ],
                                                    scale = 1.0 )

    # add the sensor cone to the frame
    frame.add_polygons( [ sensor_cone_poly ],
                        color = "red",
                        alpha = 0.3 )
