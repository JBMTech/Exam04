

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    result = []

    if not lists:
        return result

    for number in lists[0]:
        found = True

        for current_list in lists:
            if number not in current_list:
                found = False
                break

        if found and number not in result:
            result = result + [number]

    return result
