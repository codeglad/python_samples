
# maintain max_ending_here, min_ending_here and max_so_far
# if the current elem is 0: max_ending_here = min_ending_here = 0
# if the current elem is positive: max_ending_here = max(last_elem, max_ending_here*last_elem)
#                                  min_ending_here = min(last_elem, min_ending_here*last_elem)

# if the current elem is negative: max_ending_here = max(last_elem, min_ending_here*last_elem)
# ============================================================================================
# consider max as an alias for max_ending_here and min as an alias for min_ending_here

# max +ve - definitely new max not max*last_elem
# max 0 - min_ending_here * last_elem
# max -ve - min_ending_here * last_elem

# if min_ending_here > 0:
#    max_ending_here = last_elem
# else:
#    max_ending_here = min_ending_here * last_elem

# if the current elem is negative: min_ending_here = min(last_elem, max_ending_here*last_elem)
# ============================================================================================
# consider max as an alias for max_ending_here and min as an alias for min_ending_here

# min 0 - so max is either 0 or positive - new min is min(last_elem, max*last_elem)
# min +ve - so max is more +ve - new min is max*last_elem
# min -ve - max is -ve : -5 -1 => 10, 2 => last_elem
# min -ve - max is 0 : -5 0 => 10, 0 => last_elem
# min -ve - max is +ve: =>max * last_elem

# Finally, max_so_far can be updated to max_ending_here if max_ending_here > max_so_far


def max_subarr_pdt(input):
    max_ending_here = min_ending_here = max_so_far = input[0]
    for i in range(1, len(input)):
        current_elem = input[i]
        if current_elem == 0:
            max_ending_here = min_ending_here = 0
        elif current_elem > 0:
            max_ending_here = max(current_elem, max_ending_here*current_elem)
            min_ending_here = min(current_elem, min_ending_here*current_elem)
        else:
            temp = max_ending_here
            max_ending_here = max(current_elem, min_ending_here*current_elem)
            min_ending_here = min(current_elem, temp*current_elem)
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far


def main():
    a1 = [6, -3, -10, 0, 2]
    a2 = [-1, -3, -10, 0, 60]
    a3 = [-2, -3, 0, -2, -40]
    print max_subarr_pdt(a1) # 180
    print max_subarr_pdt(a2) # 60
    print max_subarr_pdt(a3) # 80

if __name__ == '__main__':
    main()
