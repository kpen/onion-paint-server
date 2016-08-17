from __future__ import unicode_literals

from django.db import models

class Drawing(models.Model):
  name = models.CharField(max_length=200)
  # user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Figure(models.Model):
  drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
  line_color = models.CharField(max_length=200)
  fill_color = models.CharField(max_length=200)

  def __str__(self):
    return "Line color: " + self.line_color + ", Fill color: " + self.fill_color

class Point(models.Model):
  figure = models.ForeignKey(Figure, on_delete=models.CASCADE)
  x = models.IntegerField(default=0)
  y = models.IntegerField(default=0)

  def __str__(self):
    return "x: " + self.x + ", y: " + self.y

# Drawing
#
#
# drawing has many points
# point belongs to drawing
#
# drawing belongs to account
# account has many drawings
#
# drawings
# - id
# - name
# - user_id
#
# figures
# - id
# - drawing_id
# - line_color
# - fill_color
#
# points
# - id
# - figure_id
#
# accounts
# - id
# - username
#
# SELECT points.* from points p
# LEFT JOIN drawings d ON p.drawing_id = d.id
# LEFT JOIN users u ON d.user_id = u.id
# WHERE u.username = 'alexey'



