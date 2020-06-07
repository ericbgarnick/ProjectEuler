
def mults_of_3_5(limit: int):
    threes_total = val_total(3, limit)
    fives_total = val_total(5, limit)
    fifteens_total = val_total(15, limit) if limit > 15 else 0
    return threes_total + fives_total - fifteens_total


def val_total(val: int, limit: int) -> int:
    num_vals = (limit - 1) // val
    if num_vals % 2:
        pair_total = (num_vals + 1) * val
        num_pairs = num_vals // 2
        non_pair = ((num_vals + 1) // 2) * val
        vals_total = pair_total * num_pairs + non_pair
    else:
        pair_total = (num_vals + 1) * val
        num_pairs = num_vals / 2
        vals_total = pair_total * num_pairs
    print(f"TOTAL OF {vals_total} FOR {val} AT {num_vals} VALS")
    return int(vals_total)


if __name__ == '__main__':
    print(mults_of_3_5(1000))
