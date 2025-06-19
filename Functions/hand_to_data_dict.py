def hand_to_data_dict(hand: list):
    values = []
    for i in range(len(hand)):
        values.append(hand[i].get_value())

    total_sum = sum(values)
    dictionary = {
            "Card_1": values.pop(),
            "Card_2": values.pop() if values else 0,
            "Card_3": values.pop() if values else 0,
            "Card_4": values.pop() if values else 0,
            "Total_val": total_sum ,
        }
    
    return dictionary