# What's this?

This is a Utility for Planning a Double Slot Goodness Exchange in an Archipelago Multiworld Randomizer

# How do you use this?

It currently Has No commandline options, so you only Ned to Call the Main file and it will Read the `DSG-data.yaml` file, whereupon it will Spit out either a 'No' or a 'Yes' to let you Know if it Found a Valid Cycle

If it found a valid Cycle, it will give you the Name of the Slots in order, such that the First one on the list will give a slot to the Second, the Second to the Third and so on. The last Slot Name on the cycle will then Give a Slot to the First one in the Cycle

## YAML options

The Basic Structure of the YAML file needed is as follows
```yaml
SlotName: ['FirstPlayer', 'SecondPlayer', 'ThirdPlayer']
Worlds:
    FirstWorld: ['FirstPlayer','SecondPlayer']
    SecondWorld: ['ThirdPlayer','SecondPlayer']
    ThirdWorld: ['FirstPlayer','ThirdPlayer']
```
Alternatively instead of using Flow Collection you could Write it out as

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

Any name not listed in `SlotName` Shall be ignored for the Cycle creation

You May add Any Arbitrary Number of Slots and Worlds, but keep in Mind Large Numbers might take a While, Specially since this is Implemented on Python

# Requirements

- pyyaml, If you have the Archipelago launcher you may already have this installed

# FAQ

## okay... What is Double Slot Goodness?

It is a Very silly idea to share your YAML(Settings for a Randomizer) with another Person in the Same Multiworld Randomizer

You Submit a YAML for a Game, then everybody also Gives their YAML to somebody Else, or alternatively Submit the Same Yaml twice, then give somebody else the Other slot.

This Means that Everybody Plays 2 Slots, Their Original slot, and one That Somebody else made for them, With the Knowledge that the person that is giving the slot is also playing with the Exact Same Settings as them.

### What if i can't play the Same game that Somebody else is Playing?

This is What this utility intends to Solve. You Share which games you are able or willing to play so that you don't give out or Receive a Game that you are unable to play.

Keep in Mind The list of game which you are able to PLAY might be Different from the list of games that you will be Able to SUBMIT, since the list of Games you will be able to submit will be the intersection between your own Games and the Games that Somebody else is Able to play. This also Means that More popular Games also have a higher chance of being able to be played.

### This just Sounds like the Secret Yaml Exchange with Extra Steps.

You are Right, this is essentially the Secret Yaml Exchange idea.

What makes it different (Not Better) are 2 things:

1.- The Player that Gives you the YAML Must also play a Game with the Exact same Settings.

2.- The exchange of YAMLs goes in a big loop, so there are no Isolated group that Give eachother a Game and Receive a Game from the One they gave it to.

The first point is more a Stylistic Choice, In theory you could just Ignore the Part where you Also need to play with the Same settings as you give out, in which case, everybody would play 1 singular slot, given to them by someone else, however if you did that you would also remove some of the Benefits of doing this way. 
You won't suffer alone if your Settings turn out to be Horrible, and for the same reason (Assuming the players are of similar skill) you won't receive Settings which Are unnecesarilly Hard.

The second is more of a Limitation of my Implementation. You could In theory Remove it and the Idea would work just fine, if a bit more Simple and less "Grandiose". however, this also makes it harder to calculate on the fly. it would Certainly be Easier to calculate it by hand in some cases. This tool Considers both of these things when Deciding the Order of Slot Giving.

## What if i was not included in the Cycle?

This too, is Accounted For. This tool will only Work when Everyone can share and receive to at least one other person. This tool will Tell you Exactly Who to give your YAML to, and who wil give YOU your new YAML. Unless you only Share a Game with one Other Person, you will be Able to Try and Participate.

## Does this tool Include Everyone?

this tool Currently Accounts for Everyone you submit to it. If it Cannot Include Everyone EXACTLY ONCE while trying to find a Cycle, then it Will fail.

I have plans to Add a Way to Try and Make Multiple Cycles instead of Only one Big one, however that is currently not implemented.

## How can i guarantee that This tool will have a Solution?

the short answer to this is you can't do it easily. thus why i built the tool in the first place.

technical answer:The problem is NP-complete, so there are very Few ways you could GUARANTEE it.

Technically Correct Solution 0: You may only Submit ONE game, For example "You may only submit Hollow Knight". Since Everybody Has to share 

Technically Correct Solution 0.a: Have everybody be able to play the SAME game, for example, Everybody can Play APQuest, so if you make everyone Say they are ABLE to play it, then you could then Just randomize the Names in any Arbitrary order and it would make a valid Cycle. This differs from the first solution, because while technically You'd Be Able to Submit games other than APquest, There is a high Chance that the person You give your YAML to doesn't Share any games with you, and the Person you Receive a YAML from also doesn't share games with you. This would SUCK. It would Limit a LOT of people, and thus would not be Very fun or Interesting.

Technically Correct Solution 0.b: Make sure Everybody can play a Set of Games(Ideally some of the Many Free games able to be played with archipelago). this is the Same as the Previous 2 Solution, but instead of being Locked into 1 Game, You'd be locked into a Selection of Games. Slightly Better, and Allows more freedom on the players, but it's still Lame and Not Very interesting.

Technically Correct Solution 1: 

For this we need a bit of Maths

Represent Each Player as a Vertex in a Graph.

Connect them to eachother such that if 2 Players have at least 1 Game in common, they have a line connnecting them to eachother

If they have a Hamiltonian Cycle in the Graph