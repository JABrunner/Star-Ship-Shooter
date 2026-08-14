import pygame

from main import Ship

_DUMMY_LASER_IMG = pygame.Surface((10, 10))


def make_ship():
    ship = Ship(x=0, y=0)
    ship.laser_img = _DUMMY_LASER_IMG
    return ship


def test_shoot_appends_a_laser_and_starts_cooldown():
    ship = make_ship()

    ship.shoot()

    assert len(ship.lasers) == 1
    assert ship.cool_down_counter == 1


def test_shoot_again_before_cooldown_elapses_is_ignored():
    ship = make_ship()

    ship.shoot()
    ship.shoot()
    ship.shoot()

    assert len(ship.lasers) == 1


def test_cooldown_resets_to_zero_after_full_cycle():
    ship = make_ship()
    ship.shoot()

    for _ in range(Ship.COOLDOWN - 1):
        ship.cooldown()
    assert ship.cool_down_counter != 0

    ship.cooldown()
    assert ship.cool_down_counter == 0


def test_shoot_fires_again_once_cooldown_has_reset():
    ship = make_ship()
    ship.shoot()

    for _ in range(Ship.COOLDOWN):
        ship.cooldown()
    assert ship.cool_down_counter == 0

    ship.shoot()
    assert len(ship.lasers) == 2
