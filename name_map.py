#!/usr/bin/python3

print("Write something about:\n")

name_map = {
    "Oksana"        : "whats your fav place to visit in bc and also whats a cool hospital statistic (answer both or else)",
    "Cody"          : "favourite kush based product to consume and why",
    "Aviana"        : "convince me to finish arcane (no jinx armpits is not a valid reason)",
    "Simon"         : "are the falls still falling",
    "Christian"     : "what is your favourite coop game and give me 2-3 reasons why it has merit",
    "Brandon"       : "favourite mixed drink",
    "Liam"          : "what is the root definition of schmoly",
    "DizzyDwarf"    : "haha u broke stankles arm you get a free nickbuck for having big arms",
    "Paul"          : "what wouldnt i expect to be difficult about writing low effort music that sounds good",
    "Jaylen"        : "why is hoi4 the best sim",
    "Elena"         : "haha u live in quebec tell me how to make your fav drink but in french",
    "Maurice"       : "ay show me ya tits (up to interpretation)",
    "Aidan"         : "which new york quisine is your favourite and why should I try it when we do the ny trip",
    "Kurtis"        : "what is your favourite item of star wars media and why",
    "Jacob"         : "why forza motorsport is better than forza horizon",
}

padding = max(len(name) for name in name_map)

print('\n'.join(['{:<{width}}   {}'.format(*item, width=padding) for item in sorted(name_map.items())]))
