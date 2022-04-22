## Call to adventure/ Introduction
This is what we’re doing and how this supposedly works
Why are we doing this?

## Meeting the Mentor(s) & Crossing the Threshold 
Self-Quantification

Self-Quantification is described by the Quantified Self movement as “self-knowledge through numbers”. Users collect data about themselves and use them to gain insights into their behaviours and habits. The process of collecting data is often called self-tracking, which becomes self-quantification only after this data is put into a quantitative or qualitative context. 

> You might self-track your sleeping schedule by writing down the times you go to bed and wake up each night. If you compare these data points to each other, to see whether going to bed early means you also wake up earlier or how your sleeping schedule differs on weekends, that’s self-quantification. 

Self-quantification itself can also be split up into sub-activities: First the collected data is managed, which includes digital or analog storage as well as organising it in a manner that makes it understandable for the user (and/or any self-quantification systems that interact with it). Then, users can reflect on data, by which they derive meaning from it.

> For sake of convenience, you may write down your sleeping schedule on a notepad next to your bed. Since these notes are very cluttered, you decide to copy them into a table in a separate notepad, in chronological order. This is managing your data. Once you have collected a sufficient amount of data points, you sit down with your notes, think of any questions you have, and see how your notes can answer them. By this you are reflecting on your data.
<details>
<summary markdown="span">Why go into so much detail?</summary>
Splitting self-quantification (and later topics that will be brought up) into all these sub-tasks might seem nitpicky at first. It is however very useful when trying to incorporate it into another service, such as we will be doing shortly. By looking at the process in detail, we can ensure that we do not miss any important components and really understand how the whole concept is supposed to function.
</details>
Self-quantification can be applied to many aspects of life, such as nutrition, health, or exercise. Apps can be quite helpful with this, as they organise and sometimes track relevant data for the user. Some examples that you might already be using are FitBit or Google Fit, which both track various exercise related data, organise them into daily, weekly, and monthly overviews, and assist in self-reflection, by pointing out increases and decreases. 

Overall, self-quantification is meant to increase awareness, curiosity, and consciousness. It can show problematic behaviour that users may not have noticed otherwise and inspire to improve oneself by comparing data to others’ or the former self’s. But of course it also has some disadvantages and weaknesses. Continuously striving to best one self or others can turn into unhealthy behaviour, if it disregards other needs. When using tools such as apps, these apps often assume that users are already motivated to quantify themselves and offer little motivational affordances outside of self-quantification. This is a weak point especially since people can perceive feedback quite differently, based on how control or autonomy oriented they are. Control oriented users may feel controlled by receiving feedback, while autonomy oriented users will see it as informational and feel more competent. These last two points (lack of motivational affordances and differences in perception) made us look for another motivational factor, which might mitigate these effects.


Gamification
What is gamification?
Use of game design elements in non-game contexts – intended to motivate and engage users – different to educational games, as the main activity is not gaming – EXAMPLE
How is it used?
Often used features are points, badges, and leader boards – very versatile, so they can be applied to different contexts, such as education, health, and commerce – research on how it affects motivation still ongoing – different features have different effects – no catch-all solution for engaging users – user personality and context also matters
Why do we think this is a good idea?
Need for competence: feedback, through self-quantification – Need for autonomy: Choices and intentional and meaningful interactions, through gamification


## Tests, Allies, and Enemies
start looking for concrete gamification features and how they could help – first thought: badges/achievements – reflect users individual experiences (through unlocking different kinds of badges) and motivate to diversify workouts (to unlock new badges) – also, points to show progress – the more workouts a user has logged, the more points they collect, which gives them a feeling of competence
none of these ideas are bad and an app incorporating them may very well be an enjoyable and motivating system – however, does not take one of main criticisms of gamification into account (which has been withheld for dramatic tension): – little variety of features utilised – should not just be about implementing a few reward mechanics, but  building meaningful experiences – maybe gamification is more than just slapping EXP and achievements on things?
How do Games work? – Rapp (2018) examined how WoW engages players and drivers their behaviour – his paper was our main reason to rethink choice of game elements – main lesson we concentrated on: turn data into dynamic digital objects – these objects should tie into the mechanics of other features, provide information, and grow with the players
How can we interweave game elements and self-quantification/data visualisation?
Different ideas and why we decided against them:
RPG with class system? Very complex, might distract from core functions
Dress up game? Difficult to implement quantification in a meaningful manner and make objects dynamic
What makes game items interesting? – look into what makes players purchase items in games – thought: in our app users should “purchase” items with the time they put into workouts – avatars: non-functional items are only interesting if they are aesthetically pleasant – lesson: objects should have graphical representation – motivations to purchase items can be differentiated by object or payment orientation and utilitarian, social, or hedonic motivation – since we do not plan to include social features and want to keep overall features simple, focus on hedonic and item oriented – aesthetic appeal still important, but also novelty, celebration of individual achievements, and showing devotion to in-game characters (NPCs) – novelty first sounded difficult, since we do not want to continuously keep adding new items, but having objects grow with users might fulfil same need – had not considered NPCs yet, idea to turn workouts into in-game characters
Gatcha game? What are items/characters collected for? Random chance does mean users have little control over their rewards, thwarting need for autonomy
What makes users like characters? – uncovering “hidden aspects” of characters – system that engages user by growing closer to characters the more work outs they log – this also fits the requirement to make objects grow along with the users

## The Ultimate Boon
Buddy System! – Users can choose an NPC to accompany them on their workouts – the more they work out together, the more dialogue options they unlock
How it works
When users register a new activity, they choose a buddy – whenever a new workout with this activity is logged, friendship stat with this character is increased – friendship stat influences dialogue with buddies – users can “talk” to the characters, either to just chat or find out about their past workouts – when chatting, random lines are selected, but more options become available depending on friendship stat – characters will also recap past workout achievements to give users feedback 

## Master of two Worlds
Why we think it solves all our problems
Recap of all the requirements we have collected through research so far – Users need feedback to support their need for competence, buddies give feedback in workout recap – need for autonomy through choices and intentional interactions, users have choice of buddies (though this aspect could be improved) and can seek out interactions themselves – meaningful experiences, of course subjective, but we hope the conversations with characters will be meaningful to some users – turn data into dynamic digital objects, that tie into other features, provide information, and grow with the user, buddies themselves are digital objects that reference the workout feature in conversation, which also provides information. They grow with the user through unlocking more conversation pieces and getting to know their character – objects should have graphical representation, buddies have avatars – items become interesting through novelty, celebration of users’ achievements, and devotion to in-game characters, novelty through new conversation pieces, celebrates users’ achievements through workout recap and users can spend their time on fostering relationship with buddies – npcs become likable when users can uncover hidden aspects of their character, which will be utilised to motivate them to log more activities
All in all, all the lessons we learned through our research have been incorporated, but we know we barely scratched the surface of possibilities with some 

here’s how it’s all coming together
flowchart of everything

## Sequel Bait
What else could be added to this concept?
Regarding workout tracking: more trackable data, such as trained body region – wider selection in measurement units (such as distance) and possibility to track multiple units per activity – more research to be put into data visualisation, feedback via conversation fits gamification elements, but also has disadvantages – graphs can provide more information at a glance – workout recaps could also go more into details, for example by celebrating whenever a personal best has been beaten – dialogues, which are actually monologues as of the current version, could be designed more interactively by giving user opportunities to reply – this would also support need for autonomy, through being able to make choices – avatar of buddies could change based on friendship, to represent growth – the underlying algorithm on how friendship increases could be improved, since it simply increases by one every time a workout is logged, making the phrase “algorithm” a bit of an understatement