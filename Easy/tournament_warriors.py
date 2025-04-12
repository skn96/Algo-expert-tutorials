def determine_winner(competitions, results):
    current_winner = ""
    winners = {current_winner:0}
    for idx, competition in enumerate(competitions):
        print(f"idx: {idx}, competition: {competition}")
        winner_id = 1 - results[idx]
        if competition[winner_id] not in winners:
            winners[competition[winner_id]] = 3
        else:
            winners[competition[winner_id]] += 3
        if winners[competition[winner_id]] > winners[current_winner]:
            current_winner = competition[winner_id]

    print(f"The scores: {winners}\n")
    print(f"The final winner of the competition is: {current_winner}\n")
    return current_winner

competitions = [["HTML", "C#"], 
                ["C#", "python"],
                ["python", "HTML"]]

results = [0,0,1]

determine_winner(competitions, results)