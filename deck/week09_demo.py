"""Small deterministic ranking example; invented scores, not a trained model."""
from decimal import Decimal

ITEMS = (
    ('A', 'Motion workshop', 9, 1),
    ('B', 'Drawing workshop', 8, 3),
    ('C', 'Sound workshop', 5, 8),
    ('D', 'Type workshop', 4, 9),
)


def rank(relevance_weight):
    """Return (id, title, score), with stable ID tie-breaking and no randomness."""
    w = Decimal(str(relevance_weight))
    if not w.is_finite() or not Decimal(0) <= w <= Decimal(1):
        raise ValueError('weight must be finite and between 0 and 1')
    scored = [(key, label, w * relevance + (1 - w) * novelty)
              for key, label, relevance, novelty in ITEMS]
    return sorted(scored, key=lambda row: (-row[2], row[0]))


if __name__ == '__main__':
    for weight in ('0.8', '0.3'):
        print('relevance weight =', weight)
        for key, label, score in rank(weight):
            print(f'{key}  {label:<20} {score:.1f}')
