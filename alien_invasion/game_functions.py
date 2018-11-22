# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 02:40:10 2018

@author: Think
"""

import sys

import pygame
from ship import Ship
def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
                
            
def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()