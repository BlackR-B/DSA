import json
"""Lab 01.02 - Max…Min…Avg"""
def main():
    """Lab 01.02 - Max…Min…Avg"""
    scores = json.loads(input())
    avg = sum(scores) / len(scores)
    big_value = scores[0]
    small_value = scores[0]
    for score in scores:
        if score > big_value:
            big_value = score
        elif score < small_value:
            small_value = score
    print(f"{(big_value), (small_value), round(avg, 2)}")
main()
