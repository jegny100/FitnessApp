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

Gamification describes the use of game design elements in a non-game context, which are intended to motivate and engage users. As more and more people are picking up gaming as a hobby and become more familiar with game elements, gamification is likewise being used to enhance services more often. It is related to subjects such as educational games, but differs in the way that the main activity performed is not a game, but simply incorporates gameful features.

> As a child you may have studied to improve your language skills by playing learning games and helping your favourite cartoon characters sort vocabulary, fight declination monsters, or unravel past tenses. This would be an educational game, not gamification, as the main activity was still gaming (and you were merely tricked into studying). Nowadays you may want to brush up on your language skills with the aid of an online learning platform such as Duolingo. In this app you can collect badges for a variety of activities and build up a streak by completing daily lessons. This is gamification, as the main activity is learning, with game elements to motivate you to keep going.

Gamified applications most commonly feature points, badges or leader boards. These elements are very versatile, so they can be applied to many different contexts, such as education, health, and commerce. Research on how gamification affects motivation is still ongoing. The difference between external and internal motivation is something that especially interests researchers, but since these are difficult to measure directly and can only be seen in their behavioural outcomes, no definite connection can be made yet. Something that has become apparent though is that different game design elements have different effects and that the context they are being deployed in and the personality of the user matter. Because of this they are, though efficient at times, no catch-all solution for engaging users.

Why do we think this is a good idea?

We think gamification will be a great addition to our app design, since it can complement self-quantification in our competence-autonomy dilemma: Users will feel competent through receiving feedback about their workout progress, guided by self-quantification tools. The game design elements can be chosen to satisfy a need for autonomy, for example by allowing users to make meaningful choices and seek out intentional interactions.



## Tests, Allies, and Enemies

Now that we had decided on the two main elements or theories of how our app should work, we were ready to look into more concrete features, starting with game design elements. Our first approach was to go with the classics: Badges/achievements and points. Badges could reflect an user's individual experience and choices they made along the way (by seeing badges that fit their workouts), but also provide an incentive to diversify their workout (to unlock new badges). Points could show their overall progress, as the more workouts a user would logg, the more points they would collect. This would give them a feeling of competence, as well as rewarding interactions with the application.

None of these ideas are bad, indeed there is a reason why these features are upon the current Top 3 most researched and deployed elements. An app incorporating these may very well be an enjoyable and motivating system - however, relying on them does not take one of the current main criticisms of gamification into account (which has been withheld for dramatic tension). Gamified systems overall show little variety in their utilised features. They thereby ignore that games are not just a collection of simple reward mechanisms, but come together to an overall meaningful experience. This is a lesson games themselves are already taking to heart, but which sadly has passed over many gamified applications. To be more frank, we were tasked with the challenge of how to see gamification as more than just slapping some EXP counters and achievements on a system and calling it a day.

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
 
---
## Implementation

This app was developed using [Kivy](https://kivy.org/doc/stable/) and [KivyMD](https://kivymd.readthedocs.io/en/latest/#), a python based cross-platform GUI toolkit for touch applications that follows Google's [Material Design](https://material.io/design/introduction) system. 

<details>
<summary markdown="span">My (jegny100) personal expierence with Kivy & KivyMD</summary>
I would describe myself, at least at the start, as a beginner in such extensive programming projects. Using multiple classes and continuously running Python loops, as is the case with apps, is new territory for me, let alone learning how to use Kivy and KivyMD. Therefore, at many points it has been difficult for me to distinguish whether a problem is due to my general programming skills reaching their limits or whether it is due to Kivy/KivyMD itself, its docs or even my IDE.
Nevertheless, one thing is certain: Kivy gave me the courage to develop an app on my own in the first place, because I had a solid understanding of Python and thus a big hurdle of a new programming language was taken away from me. KivyMD then gave me hope that this app could actually have something in terms of design.
Overall, I can recommend Kivy as an introduction to app programming if you have mainly worked with Python so far. It's easy to learn how the Kivy language is structured and you quickly get a sense of achievement with KivyMD, as the app looks appealing straight away. However, I did reach some of the limits of Kivy when, for example, I wanted to display dialog widgets in more than just a simple rectangular shape, but I was able to implement most of my ideas solidly, as you can see from this great result. So go for it!
</details>


### Requirements
As listed in `requirements.txt` and can be automatically installed with the following after cloning this project.
```
pip3 install -r requirements.txt
``` 

### Functions
The app is designed to track your fitness activities by logging your own workouts. You can add your own activities like mudflat hiking, caber toss or deep breathing, decide which unit of measurement (how long took your mudflat hike? how much did your caber weight or how many deep breaths did you take?) is relevant, and choose a buddy to work out with to build a closer friendship. Talk to your buddy about your fitness progress or have a relaxed chat with them and get to know them better. 

**App Functions**
- logging a new workout 
- overview of all implemented activities in the collection
- adding new activity definitions to the collection
- overview of your fitness Buddys
- conversations with buddys about corresponding activites or just checking in with them
- setting your preferences about encouraging or nudging messages:
    - after logging a workout
    - when opening the app

#### Conversations
To have a chat with your buddy, you need a CSV file for both the workout conversation and the regular conversation, but both are treated the same. The matching CSV is first read in and mapped as a DataFrame (i.e. a matrix/table), where each row represents a message. The algorithm selects the next message by minimizing the set of all messages using filters from the other columns and randomly selecting one from the resulting set. In doing so, it is guided through the texts using tags until the conversation is over. From the following representation of the CSV, as well as the explanations the function of the algorithm becomes more clear. 

The structure of the CSV_files is as follows: 

| Text | Tag | Next-Tag | Friendship min | Friendship max | Condition 1 | ... | Condition n | other rec notes |
| ---- | --- | -------- | -------------- | -------------- | ----------- | --- | ----------- | --------------- |
| Hi! You wanna talk? | Intro | last workout | 0 |      2 |      1      |     |             | if any workout is logged with chosen buddy

* Text  
Displayed message in the conversation. Variables can be represented within the texts in square brackets `[]`, which are read and filled in the code to provide the conversation with data from the app. The definitions of these variables are stored in the dictionary `chat_variables_dict`. If you want to add new variables you can use the function `get_dict_chat_variables()` and the dictionary will be extended automatically.

* Tag & Next-Tag  
Determines the tag of the current text and determines which tag must follow next. The chat always starts with the tag 'Intro', first filters all messages based on this tag and takes over 'Next-Tag' to narrow down the next message when the message is selected. The chat ends as soon as there is no tag in Next-Tag.

* Friendship min & Friendship max  
Defines between which friendshiplevels a message is eligible. Both a lower and an upper limit can be specified.

* Condition 1 | ... | Condition n  & other rec notes  
Any other columns can be inserted to act as new filters. The last column 'other rec notes' serves as explanation of the condition. To include the new condition, it must be implemented in the `fill_conversation_list()` function within the while loop to further delimit the `subset_buddy_convo_df`-DataFrame.

##### A little more in-depth explanation on how to extent the chat messages of your buddys
If you want to insert a new text message, you can add a line to the corresponding CSV of a buddy. The most important part here is to pay attention to which tags you use, as the code will repeatedly move from tag to next tag, selecting the messages that will then be displayed in the chat. One can extend chats independently in different ways with different complexity. There are basically two options, with or without working on the code: 

*Without Code : Simple Extensions without variables or new conditions*
1. So you have to think up a new text. If at all, this should only contain already known variables in square brackets `[]`, i.e. variables that already occur in the other text messages or are already calculated in the code in the dictionary `chat_variables_dict`. 
2. Next, you choose a tag. This can be new or an already known tag. If you want to start a new tag, you should make sure that another message refers to this new one in 'next-tag', otherwise the loop will never be able to find this message. If you choose an already existing tag, it means that the new message belongs to the same group of messages. So it should make sense in relation to the content of the message that comes before it. 
3. Afterwards, it must be determined what kind of message follows next, i.e. set the next-tag. Again, you have the option to use known or new tags, paying attention to the logic as well: Is the new next-tag already a tag in another line or will you unintentionally end up with a dead end?  Do the messages that have the Next-tag set here really fit as follow-up messages to my message? In addition, you can also leave the field empty, which means that the conversation is over after that.
4. With the columns Friendship min / max you can define how good you have to be friends with the buddy for that message. So you can set from which level a message can be displayed at all or from which level you are already so good friends that the buddy doesn't even say a certain message anymore. You probably wouldn't greet strangers with "Well, yIf you have several messages (i.e. lines) that match or build on each other thematically, you can set the column set_group instead of setting new tags for all of them. As soon as a message is selected that has been assigned to a group, this is adopted for all subsequent messages. As an example, Bo talks about potatoes in one message and later mentions that he now feels like fries. This ensures that topics are not suddenly dropped or appear without reference.ou old sock" or say goodbye to friends with "It was nice to meet you", would you?
5. If you have several messages (i.e. lines/rows) that match or build on each other thematically, you can set the column set_group instead of setting new tags for all of them. As soon as a message is selected that has been assigned to a group, this is adopted for all subsequent messages. As an example, Bo talks about potatoes in one message and later mentions that he now feels like fries. This ensures that topics are not suddenly dropped or appear without reference.

 *With Code: Complex conditions and new variables*
- If you want to create new variables, you should observe the following in addition to the instructions "without code":  
The code automatically reads the square brackets `[variable]` with the variable, then looks for this string in the keys of the dictionary `chat_variables_dict` and replaces that with the corresponding value. To create new variables, it is mandatory to extend the code and have an understanding of where to find the information you want to put there. So the theory, now for the practice:
1. Find in `main.py` the function `get_dict_chat_variables()`. Inside the function, mark with comments which variable is defined at the position. Here you can add your new variable by setting it as a key in the class variable FitnessApp.chat_variables_dict["variable"] = value and assigning it a value calculated by you beforehand. To access data from the logger, the table is read in at the beginning of the function and stored in `logger_df` filtered directly according to the previously selected workout.  
So what would the code look like if you wanted to specify when you first did the workout with your buddy? 
```python
# [date_first_logged]  
# in DataFrame logger_df in column 'date', get the minimal date  
date_first_logged= logger_df["date"].min()	
# save to key "[date_first_logged]" the value of the first workout calculated before
FitnessApp.chat_variables_dict["[date_first_logged]"] = date_first_logged	
```
 2. In your CSV file, just write your new variable in the text (with spaces around it) and watch it get automatically replaced by your calculation.

- Similar to new variables, the code for new conditions must be extended according to one's own wishes. In addition, a new column must be created in the CSV file, which must be used for all CSV files.
1. Extending the CSV: If you want to display messages only on the basis of certain conditions, you should think of a logic for this. For example, a conversation about a workout is only started if the logger table for the workout is not empty. For this purpose, the column 'logged any' is used, whose entry is 0 if no workout has ever been logged. Within the code, the system checks whether more than 0 workouts have been logged. If this is the case, all lines that have a zero in the column are filtered out.
If you want to make a new conditional statement, you have to create a new column and fill new rows according to your own logic.

2. extend the code: In the code of `main.py` a new filter must be implemented under the function `fill_conversation_list()` within the while loop. Depending on the self-selected condition, the DataFrame `subset_buddy_convo_df` must then be delimited, which at the end determines which sentence is to be said next. 
