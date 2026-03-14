from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- check_guess ---
# Bug: check_guess returns a (outcome, message) tuple, not a bare string.
# Old tests compared result == "Win" which always failed silently (tuple != str).

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_returns_tuple():
    # Regression: result must be a 2-tuple, not a bare string
    result = check_guess(50, 50)
    assert isinstance(result, tuple) and len(result) == 2


# --- get_range_for_difficulty ---
# Bug: Normal and Hard ranges were swapped (Normal=1–100, Hard=1–50).

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    # Was (1, 100) before fix — must be (1, 50)
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    # Was (1, 50) before fix — must be (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_unknown_difficulty_defaults_to_hard_range():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess ---
# Bug: secret value alternated between str and int types depending on input path,
# causing TypeError when comparing guess (int) to secret (str).

def test_parse_valid_integer_string():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert isinstance(value, int)  # must be int, not str

def test_parse_float_string_converts_to_int():
    # Covers the alternating type bug: "3.0" should yield int 3, not str "3.0"
    ok, value, err = parse_guess("3.0")
    assert ok is True
    assert value == 3
    assert isinstance(value, int)

def test_parse_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_non_numeric_string():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None


# --- update_score ---
# Bug: attempts counter was initialised to 1 instead of 0, so attempt_number
# was off by one, making the first-attempt win worth 80 pts instead of 90.

def test_win_on_first_attempt_scores_90():
    # attempt_number=0 → 100 - 10*(0+1) = 90
    new_score = update_score(0, "Win", 0)
    assert new_score == 90

def test_win_score_decreases_with_more_attempts():
    score_early = update_score(0, "Win", 0)   # 90
    score_later = update_score(0, "Win", 5)   # 100 - 60 = 40
    assert score_early > score_later

def test_win_score_floor_is_10():
    # attempt_number=9 → 100 - 100 = 0, clamped to 10
    new_score = update_score(0, "Win", 9)
    assert new_score == 10

def test_too_low_deducts_score():
    new_score = update_score(100, "Too Low", 0)
    assert new_score == 95

def test_too_high_even_attempt_adds_score():
    new_score = update_score(100, "Too High", 0)  # even attempt
    assert new_score == 105

def test_too_high_odd_attempt_deducts_score():
    new_score = update_score(100, "Too High", 1)  # odd attempt
    assert new_score == 95
