




def ex2A(mat):
    #move of the byte for place -> /n -> /n -> /n (/n new line from start)
    player1=0
    player2=0
    #max value 511 (not valid in game)

    masks=[448,56,7,273,84,73,146,292]

    for i in range(3):
        for j in range(3):
            if(mat[i][j] & 1):
                player1=player1 | 1
            player1=player1<<1
    player1=player1>>1

    for i in range(3):
        for j in range(3):
            if(mat[i][j] & 2):
                player2=player2 | 1
            player2=player2<<1
    player2=player2>>1

    x=0
    for i in range(len(masks)):
        if(player1 & masks[i]==masks[i]):
            x=1
            print("player 1 won")

        if(player2 & masks[i]==masks[i]):
            x=1
            print("player 2 won")
    if((x==0) and (player1+player2==511)):
        print("tie")



game = [[1, 2, 1],
        [2, 1, 2],
        [2, 1, 2]]
ex2A(game)
