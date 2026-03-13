# What's this?

This is a utility for planning a "Double Slot Goodness" exchange in an [Archipelago Multiworld Randomizer](archipelago.gg)

# How do you use this?

It currently has no commandline options, so you only ned to call the main file and it will read the `DSG-data.yaml` file, whereupon it will spit out either a 'no' or a 'yes' to let you know if it found a valid cycle

If it found a valid cycle, it will give you the name of the slots in order, such that the first one on the list will give a slot to the second, the second to the third and so on. The last slot name on the cycle will then give a slot to the first one in the cycle

## YAML options

The basic structure of the YAML file needed is as follows
```yaml
SlotName: ['FirstPlayer', 'SecondPlayer', 'ThirdPlayer']
Worlds:
    FirstWorld: ['FirstPlayer','SecondPlayer']
    SecondWorld: ['ThirdPlayer','SecondPlayer']
    ThirdWorld: ['FirstPlayer','ThirdPlayer']
```
Alternatively instead of using flow collections you could write it out as

```yaml
SlotName: 
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
Worlds:
    FirstWorld: 
        - 'FirstPlayer'
        - 'SecondPlayer'
    SecondWorld:
        - 'SecondPlayer'
        - 'ThirdPlayer'
    ThirdWorld: 
        - 'FirstPlayer'
        - 'ThirdPlayer'
```

Any name not listed in `SlotName` shall be ignored. 

You may add any arbitrary number of slots and worlds, but keep in mind large numbers might take a while, specially since this is implemented on python

# Requirements

- pyyaml, If you have the [Archipelago launcher](https://github.com/ArchipelagoMW/Archipelago/) you may already have this installed

# FAQ

## okay... What is Double Slot Goodness?

It is a very silly idea to share your yaml(settings for a randomizer) with another person in the same multiworld randomizer

You submit a yaml for a game, then everybody also gives their yaml to somebody else, or alternatively submit the same yaml twice, then give somebody else the other slot.

This means that everybody plays 2 slots, their original slot, and one that somebody else made for them, with the knowledge that the person that is giving the slot is also playing with the exact same settings as them.

## What if i can't play the game that somebody else gives me?

This is what this utility intends to solve. You share which games you are able or willing to play so that you don't give out or receive a game that you are unable to play.

Keep in mind the list of game which you are able to **play** might be different from the list of games that you will be able to **submit**, since the list of games you will be able to submit will be the intersection between your own games and the games that somebody else is able to play. This also means that more popular games also have a higher chance of being able to be played.

## This just sounds like the Secret Yaml Exchange with extra steps!

To those who don't know what the Secret Yaml Exchange is, just skip to the next point.

You are right, this is essentially the secret yaml exchange idea.

What makes it slightly different are 2 things:

1.- the player that gives you the yaml must also play a game with the exact same settings.

2.- the exchange of YAMLs goes in a big loop, so there are no isolated group that give eachother a game and receive a game from the one they gave it to.

The first point is more a stylistic choice, in theory you could just ignore the part where you also need to play with the same settings as you give out, in which case, everybody would play 1 singular slot, given to them by someone else, however if you did that you would also remove some of the benefits of doing this way. 
You won't suffer alone if your settings turn out to be horrible, and for the same reason (assuming the players are of similar skill) you won't receive settings which are unnecesarilly hard.

The second is more of a limitation of my implementation. You could in theory remove it and the idea would work just fine, if a bit more simple and less "Grandiose". However, this also makes it harder to calculate on the fly. It would certainly be easier to calculate it by hand in some cases. This tool considers both of these things when deciding the order of slot giving.

Remove both of these changes and you get the Secret Yaml Exchange.

## What if i was not included in the cycle?

This too, is accounted For. This tool will only work when everyone can share and receive to at least one other person. This tool will tell you exactly who to give your YAML to, and who wil give YOU your new YAML. Unless you only share a game with one other person, you should be able to try and participate.

If the tool does not include everybody, then it fails outright.

## Does this tool include everyone?

This tool currently accounts for everyone you submit to it. If it cannot include everyone ***exactly once*** while trying to find a cycle, then it will fail.

I have plans to add a way to try and make multiple cycles instead of only one big one, however that is currently not implemented.

## How can i guarantee that this tool will have a solution?

The short answer to this is you can't do it easily. Thus why I built the tool in the first place.

Technical answer:the problem is np-complete, and is solved using what's essentially trial and error, so there are very few ways you could *guarantee* it.

Technically correct solution 0: you may only submit ***one*** game, for example "You may only submit hollow knight". Since everybody has to share 

Technically correct solution 0.A: have everybody be able to play the same game, for example, everybody can play apquest, so if you make everyone say they are able to play it, then you could then just randomize the names in any arbitrary order and it would make a valid cycle. This differs from the first solution, because while technically you'd be able to submit games other than apquest, there is a high chance that the person you give your yaml to doesn't share any games with you, and the person you receive a yaml from also doesn't share games with you. This would suck. It would limit a lot of people, and thus would not be very fun or interesting.

Technically correct solution 0.B: make sure everybody can play a set of games(ideally some of the many free games able to be played with archipelago). This is the same as the previous 2 solution, but instead of being locked into 1 game, you'd be locked into a selection of games. Slightly better, and allows more freedom on the players, but it's still limiting and not very interesting.

Technically correct solution 1: Hamiltonian cycles

For this we need a bit of maths

- Represent each player as a vertex in a graph.

- Connect them to eachother such that if 2 players have at least 1 game in common, they have a line connnecting them to eachother

- If they have a hamiltonian cycle in the graph, then this tool will be able to find a solution.

This is how the tool works internally, so you won't be much faster than it by hand.

Technically correct solution 1.A:4-connected planar graphs and planar triangulations

- There exists a graph representing the players and their compatibility
- assume the graph is planar. if it is not, remove the connection between nodes that make the graph non-planar.
- if you are now able to remove ***any*** 3 players without disconnecting the graph (Meaning you can move from one vertex to another following a path) then the graph is 4-connected
- thanks to William Thomas Tutte, we know that 4-connected planar graphs have a hamiltonian cycle
I am not personally able to prove the existence of a hamiltonian cycle for a 4-connected planar graph, but somebody else already did, so i don't have to

For more accurate information see the wikipedia article on [finding hamiltonian cycles](https://en.wikipedia.org/wiki/Hamiltonian_path_problem)
