from main import next_wave


def test_next_wave_increments_level_by_one():
    level, _ = next_wave(level=0, wave_length=5)
    assert level == 1


def test_next_wave_increases_wave_length_by_five():
    _, wave_length = next_wave(level=0, wave_length=5)
    assert wave_length == 10


def test_next_wave_compounds_across_multiple_calls():
    level, wave_length = 0, 5
    for _ in range(3):
        level, wave_length = next_wave(level, wave_length)

    assert level == 3
    assert wave_length == 20
