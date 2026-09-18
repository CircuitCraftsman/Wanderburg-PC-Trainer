# Build: 00ce90a475bccbd00174d8ef087c1bbb

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
