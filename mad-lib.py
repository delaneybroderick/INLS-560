#Mad lib example for fucntions. 

def madlib(verb_1, verb_2, verb_3, noun_1, noun_2, noun_3, adjective_1, adjective_2, Name) :
    '''Mad lib function'''
    story =f'''
When {Name} got their new glasses, they were thrilled. The optometrist handed over the glasses and said, These will help you see {adjective_1}! As soon as {Name} put them on, the world looked completely different. Trees outside seemed so {adjective_2}, and even the tiny {noun_1} on the windowsill became more visible. At first, {Name} had trouble adjusting to the new glasses. They felt like their {noun_2} was too close to their face, but they soon got used to it. Every day, they enjoyed {verb_1} their new-found clarity. Reading, watching TV, and even doing everyday tasks became much easier. By the end of the week, {Name} couldnt believe how they ever managed without them. The glasses had truly {verb_2} their life. Now, whenever they {verb_3}, they are grateful for the gift of better sight and the new {noun_3} that come with it.
'''     
    return story
output_story = madlib('dance', 'laugh', 'snort', 'tree', 'skateboard', 'phone', 'green', 'gorgeous', 'Stacy')
print(output_story)