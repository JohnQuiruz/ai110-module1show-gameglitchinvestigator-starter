# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  * it looked like a number guessing game.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  * the attempts allowed in the sidebar says 8, while the attempts left in the UI says 7
  * normal is more difficult that hard due to its wider range, effectively lowering the chances of guessing the right number
  * once you win, you cannot play a new game without refreshing the page (new game button does not work)
  * the hint tells you to go lower when the secret number is higher
  * game ends in 7 failed attempts rather than what is promised, which is 8
  * the first guess saves the number but doesn't display it until your next guess. then the 3rd guess
  * the game information always states that the number is between 1 and 100, regardless of which difficulty is selected
  * the game allows strings or empty strings to be accepted, and can be spammed indefinitely, growing the history



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  * Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  * the AI suggested that i move certain codeblocks to adhere to the behavior of streamlit's
  top-to-bottom render engine. one example was moving the expander beneath the logic that updates the attempt count after every submittal. this prevented the issue where the attempt counter in the debugging window was always 1 number behind, effectively ending the game on the attempt counter still displaying the user has 1 more attempt to use.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  * Claude stated that the st.success and st.error messages show for every guess, but they don't actually show when show_hint is toggled off.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  * by hand-tracing through the logic, getting familiar with the code, or using pytest.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  * tested the form submittal and observed the different behavior between loading the memory with the input by pressing [enter] and clicking the submit button. the submit button didn't load the input into memory until after the streamlit reload (on-interaction), which caused the input to always be 1 value behind. 
- Did AI help you design or understand any tests? How?
  * Yes, prior to Claude showing me, I was unsure about how try/catch blocks and assertions work in Python. Also learned the behavior of Streamlit.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Two characteristics about Streamlit that I learned was how it kept track of state by using dictionaries and also how it rendered the page from top to bottom, frequently. I would just explain to them to pay attention to the order of your code logic because it could make or break the code that doesn't adhere to Streamlit's rendering order.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  * prompting an llm to help understand the codebase. find the bugs myself and validate it using an llm. address bugs in separate sessions to keep the objective clear and unambiguous. prompt llm for commit message suggestions or use it to write tests. i like writing the bugs that i see in a separate document that an agent could read. maybe creating an agent that reasons about the bugs that i list in the appropriate document could be a good strategy. a debugging expert agent.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  * i mentioned these exact points above.
- What is one thing you would do differently next time you work with AI on a coding task?
  * maybe prompt the llm more about the framework that i am using to get familiar with the code behavior. i didn't know about the renderign behavior until about halfway through the project. i also want the llm to produce more diagrams for me to get better familiarized with the code. try more experimental ideas to get the llm to help me understand the code better.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  * i used to think that amateurs were truly one-shotting their applications into production but seeing how prone AI is to producing errors in its current state, there is just no way. it's first and foremost an educative tool and boilerplate generator. it will predict correctly the next code that it has seen in its training but it cannot create anything interesting unless it is able to iterate on a problem at an unaffordable rate and while being highly scrutinized by other agents. so it makes sense that a human with much more creativity and better judgment on whether the code is right/wrong, will remain the shepherd and advisor for code production.
