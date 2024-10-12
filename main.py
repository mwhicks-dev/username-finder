from IAvailabile import IAvailable
from IScoreComponent import IScoreComponent
from TwitchScrapeAvailable import TwitchScrapeAvailable
from LengthScoreComponent import LengthScoreComponent
from NumberScoreComponent import NumberScoreComponent
from TokenScoreComponent import TokenScoreComponent

import re

available: IAvailable = TwitchScrapeAvailable()
scores: list[IScoreComponent] = [LengthScoreComponent(25), 
                                 NumberScoreComponent(), 
                                 TokenScoreComponent()]

pattern = re.compile("^[a-z][a-z0-9_]{,24}$")
def valid_username(name: str) -> bool:
    return pattern.match(name) is not None

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

(minimum_length, maximum_length) = (4, 25)

def score(username: str) -> float:
    global scores

    res = [x.score_username(username) for x in scores]
    return sum(res) / len(res)

fp = open("output.csv", "w")

def dfs(username: str = "") -> None:
    print(f"-> dfs({username})")
    if not valid_username(username) or len(username) > maximum_length:
        return
    if len(username) >= minimum_length and available.is_username_available(username):
        fp.write(f"{username},{score(username)}\n")
        fp.flush()
    
    for c in characters:
        dfs(f"{username}{c}")

def bfs() -> None:
    global characters 

    queue = [c for c in characters]

    while len(queue) > 0:
        curr = queue[0]
        del queue[0]

        print(f"-> bfs({curr})")

        if not valid_username(curr) or len(curr) > maximum_length:
            continue
        if len(curr) >= minimum_length and available.is_username_available(curr):
            fp.write(f"{curr},{score(curr)}\n")
            fp.flush()

        for c in characters:
            queue.append(f"{curr}{c}")

#for c in characters:
#    dfs(c)
bfs()

fp.close()