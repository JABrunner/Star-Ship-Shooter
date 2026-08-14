import pygame

from main import Laser

HEIGHT = 950
_DUMMY_IMG = pygame.Surface((10, 10))


def make_laser(y):
    return Laser(x=100, y=y, img=_DUMMY_IMG)


def test_laser_above_screen_is_off_screen():
    assert make_laser(-1).off_screen(HEIGHT) is True


def test_laser_below_screen_is_off_screen():
    assert make_laser(HEIGHT + 1).off_screen(HEIGHT) is True


def test_laser_at_top_boundary_is_on_screen():
    assert make_laser(0).off_screen(HEIGHT) is False


def test_laser_at_bottom_boundary_is_on_screen():
    assert make_laser(HEIGHT).off_screen(HEIGHT) is False


def test_laser_mid_screen_is_on_screen():
    assert make_laser(HEIGHT // 2).off_screen(HEIGHT) is False
