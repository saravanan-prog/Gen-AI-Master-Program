# Module 2: Prompt Engineering Using ChatGPT & Gemini

## 1. Learning Objectives

By the end of this module, students should be able to:

-   Understand what a prompt is.
-   Identify the important parts of a good prompt.
-   Write clear and specific prompts.
-   Use zero-shot, one-shot, and few-shot prompting.
-   Use roles/personas effectively.
-   Control the output format.
-   Improve prompts for accuracy, creativity, and consistency.
-   Understand Chain-of-Thought (CoT), Tree of Thoughts (ToT), and
    directional stimulus prompting at a practical level.
-   Build simple prompt workflows.
-   Apply prompt engineering to business, creative, and coding tasks.

------------------------------------------------------------------------

# 2. What is Prompt Engineering?

## Simple Definition

**Prompt Engineering** is the process of designing and refining
instructions given to an AI model to get a useful and reliable response.

### Simple Example

Bad prompt:

``` text
Tell me about JavaScript.
```

Better prompt:

``` text
Explain JavaScript functions to a beginner.
Use simple English.
Give one real-world example and one small code example.
Keep the explanation within 300 words.
```

### Key Idea

> Better instructions usually produce more useful and predictable
> results.

Prompt engineering is not about finding one "magic prompt".

It is an iterative process:

``` text
Write Prompt
     ↓
Get Response
     ↓
Check Response
     ↓
Improve Prompt
     ↓
Test Again
```

------------------------------------------------------------------------

# 3. Anatomy of a Prompt

A useful prompt commonly contains three important parts:

``` text
Instruction + Context + Constraints
```

It can also specify:

``` text
Role + Input + Output Format
```

------------------------------------------------------------------------

## 3.1 Instruction

### What does it mean?

The **instruction** tells the AI what you want it to do.

Example:

``` text
Explain JavaScript functions.
```

Other examples:

``` text
Summarize this document.
Translate this paragraph into Tamil.
Create a Python program.
Generate interview questions.
```

------------------------------------------------------------------------

## 3.2 Context

### What does it mean?

Context gives the AI additional information needed to understand the
task.

Example:

``` text
I am teaching JavaScript to college students who know basic HTML and CSS.

Explain JavaScript functions.
```

Without context:

``` text
Explain functions.
```

With context:

``` text
I am teaching JavaScript to beginners.
Explain JavaScript functions using simple examples.
```

The second prompt gives the model a clearer target audience.

------------------------------------------------------------------------

## 3.3 Constraints

Constraints define limitations or rules for the response.

Examples:

``` text
Use simple English.
```

``` text
Give only 5 points.
```

``` text
Keep the answer below 200 words.
```

``` text
Do not use advanced terminology.
```

``` text
Return the answer as a table.
```

------------------------------------------------------------------------

# 4. Basic Prompt Structure

A practical template:

``` text
Role:
[Who should the AI behave like?]

Task:
[What should the AI do?]

Context:
[Important background information]

Input:
[Data provided to the AI]

Constraints:
[Rules or limitations]

Output Format:
[How the answer should be presented]
```

### Example

``` text
Role:
You are a JavaScript trainer.

Task:
Explain JavaScript functions.

Context:
The students are beginners and know basic HTML and CSS.

Constraints:
Use simple English.
Avoid advanced concepts.

Output Format:
1. Definition
2. Syntax
3. Example
4. Real-world example
5. Practice question
```

------------------------------------------------------------------------

# 5. Prompt Elements

## 5.1 Role

A role tells the AI what perspective or expertise to use.

Example:

``` text
You are a JavaScript trainer.
```

``` text
You are a technical interviewer.
```

``` text
You are a customer support assistant.
```

``` text
You are a marketing copywriter.
```

### Practical Demo

Prompt:

``` text
You are a JavaScript trainer.
Explain closures to a beginner.
Use one simple example.
```

------------------------------------------------------------------------

## 5.2 Input

Input is the information the AI needs to process.

Example:

``` text
Summarize the following text:

"Generative AI can create text, images, audio, video and code."
```

Here, the sentence is the **input**.

------------------------------------------------------------------------

## 5.3 Output Format

Tell the AI exactly how you want the result.

Example:

``` text
Explain REST API.

Return the answer in this format:

Definition:
Example:
HTTP Methods:
Real-world Use:
```

Another example:

``` text
Return the result as JSON with these fields:

{
  "name": "",
  "email": "",
  "skills": []
}
```

### Why Output Format Matters

Instead of:

``` text
Tell me about this candidate.
```

Use:

``` text
Extract the candidate information.

Return:

Name:
Experience:
Skills:
Location:
Notice Period:
```

This makes the response easier to read and process.

------------------------------------------------------------------------

# 6. Zero-Shot Prompting

## Definition

**Zero-shot prompting** means asking the model to perform a task without
providing an example.

### Example

``` text
Classify the following review as Positive, Negative, or Neutral.

Review:
"The product arrived on time and works perfectly."
```

Expected result:

``` text
Positive
```

No example was provided.

------------------------------------------------------------------------

## When to Use Zero-Shot

Use zero-shot prompting when:

-   The task is simple.
-   The expected output is obvious.
-   The model already understands the task.

Examples:

``` text
Translate this sentence into Tamil.
```

``` text
Summarize this paragraph.
```

``` text
Generate 5 Java interview questions.
```

------------------------------------------------------------------------

# 7. One-Shot Prompting

## Definition

**One-shot prompting** provides one example before asking the model to
perform the task.

### Example

``` text
Classify reviews as Positive or Negative.

Example:
Review: "The phone battery is excellent."
Answer: Positive

Now classify:

Review:
"The phone gets very hot and the battery drains quickly."
```

Expected:

``` text
Negative
```

### Why Use One-Shot?

One example helps the model understand the expected pattern.

------------------------------------------------------------------------

# 8. Few-Shot Prompting

## Definition

**Few-shot prompting** provides multiple examples.

### Example

``` text
Classify the sentiment.

Example 1:
Review: "Excellent product. I love it."
Answer: Positive

Example 2:
Review: "Very poor quality."
Answer: Negative

Example 3:
Review: "It is okay, nothing special."
Answer: Neutral

Now classify:

Review:
"The quality is good and delivery was fast."
```

Expected:

``` text
Positive
```

------------------------------------------------------------------------

# 9. Zero-Shot vs One-Shot vs Few-Shot

  Technique     Examples Provided Best For
  ----------- ------------------- --------------------------------------
  Zero-shot                     0 Simple and common tasks
  One-shot                      1 Showing the expected pattern
  Few-shot              2 or more Complex formatting or classification

### Easy Memory Trick

``` text
Zero-shot  → No example
One-shot   → One example
Few-shot   → Multiple examples
```

------------------------------------------------------------------------

# 10. Structured vs Unstructured Prompts

## Unstructured Prompt

``` text
Tell me about React and explain hooks and give examples and make it easy.
```

The request is understandable, but the requirements are mixed together.

## Structured Prompt

``` text
Role:
You are a React trainer.

Task:
Explain React Hooks.

Audience:
Beginners.

Topics:
- What is a Hook?
- useState
- useEffect

Requirements:
- Use simple English.
- Give one code example for each Hook.
- Explain the code line by line.

Output:
Use headings and code blocks.
```

### Key Difference

``` text
Unstructured → Natural request

Structured → Clearly organized instructions
```

Structured prompts are especially useful for:

-   Training
-   Business workflows
-   Repeated tasks
-   Automation
-   API-based applications

------------------------------------------------------------------------

# 11. Prompt Engineering Formula

A useful practical formula:

``` text
ROLE
  +
TASK
  +
CONTEXT
  +
CONSTRAINTS
  +
OUTPUT FORMAT
```

### Example

``` text
Role:
You are a senior Java trainer.

Task:
Create 10 interview questions about Java Collections.

Context:
The candidates have 2 years of experience.

Constraints:
Include beginner and intermediate questions.

Output:
Return a table with:
Question | Difficulty | Expected Answer
```

------------------------------------------------------------------------

# 12. Role Prompting / Persona-Based Prompting

## Definition

Role prompting tells the AI to respond from a specific role or
perspective.

### Example 1 --- Trainer

``` text
You are a JavaScript trainer.
Explain promises to beginners.
```

### Example 2 --- Interviewer

``` text
You are a technical interviewer.
Ask me React interview questions one at a time.
Wait for my answer before asking the next question.
```

### Example 3 --- Customer Support

``` text
You are a customer support assistant.
Respond politely and clearly.
Do not make promises about refunds unless the policy confirms it.
```

### Important Note

A role does not magically give the model new knowledge.

It mainly helps establish:

-   Perspective
-   Tone
-   Audience
-   Style
-   Task expectations

------------------------------------------------------------------------

# 13. Chain-of-Thought (CoT) Prompting

## What is it?

Chain-of-Thought refers to solving a problem through a sequence of
intermediate reasoning steps.

Simple idea:

``` text
Problem
  ↓
Step 1
  ↓
Step 2
  ↓
Step 3
  ↓
Answer
```

### Example

Instead of:

``` text
Solve this problem.
```

Use:

``` text
Solve this problem carefully.
Identify the important information first.
Break the solution into logical steps.
Then provide the final answer.
```

### Practical Example

``` text
A shop gives a 20% discount on a ₹2,000 product.
Calculate the final price.

First identify:
1. Original price
2. Discount amount
3. Final price

Then provide the answer.
```

Expected:

``` text
Original price = ₹2,000
Discount = ₹400
Final price = ₹1,600
```

### Trainer Note

For modern AI systems, you do not need to ask the model to expose
private/internal chain-of-thought. For teaching, focus on asking for:

-   A concise explanation
-   Key steps
-   Checks
-   Assumptions
-   Final answer

Example:

``` text
Solve the problem and provide a concise explanation of the key steps.
```

------------------------------------------------------------------------

# 14. Tree of Thoughts (ToT)

## Definition

Tree of Thoughts is an advanced reasoning approach where multiple
possible solution paths are considered instead of following only one
path.

### Simple Diagram

``` text
                 Problem
                    |
        -------------------------
        |           |           |
     Approach A  Approach B  Approach C
        |           |           |
      Check       Check       Check
        |           |           |
        -------- Best Path ------
                    |
                 Answer
```

### Example

Task:

``` text
Suggest a solution for improving an online shopping website.
```

Possible approaches:

``` text
Approach A → Improve UI
Approach B → Improve performance
Approach C → Improve search
```

The approaches can then be compared against criteria such as:

``` text
Cost
Implementation time
Expected impact
Technical complexity
```

### Important

ToT is mainly an advanced reasoning concept. A normal ChatGPT or Gemini
conversation does not necessarily expose a literal "Tree of Thoughts"
mode.

------------------------------------------------------------------------

# 15. Directional Stimulus Prompting

## Definition

Directional stimulus prompting gives the model a hint or direction about
how it should approach the task.

Instead of only saying:

``` text
Write a product description.
```

Give a direction:

``` text
Write a product description.
Focus on benefits, target customers, and practical use.
Use a professional but simple tone.
```

The additional direction guides the response.

### Example

``` text
Create a project plan.

Focus on:
- reducing development risk
- identifying dependencies
- defining milestones
- testing before release
```

The bullet points act as directional guidance.

------------------------------------------------------------------------

# 16. System Prompt vs User Prompt

## System Prompt

A system instruction establishes high-level behavior, rules, or context
for the AI.

Conceptually:

``` text
System:
You are a helpful coding assistant.
Always explain code clearly.
```

## User Prompt

The user gives the actual task.

``` text
User:
Explain JavaScript promises with an example.
```

### Simple Diagram

``` text
System Instructions
        ↓
User Request
        ↓
AI Response
```

### Important Practical Note

In ChatGPT or Gemini, users may see different prompt controls depending
on the product, account, and interface.

In API-based applications, developers can explicitly define higher-level
instructions and user input separately.

------------------------------------------------------------------------

# 17. Refining Prompts

A first prompt is often not the final prompt.

### Version 1

``` text
Explain React.
```

### Version 2

``` text
Explain React to a beginner.
```

### Version 3

``` text
You are a React trainer.

Explain React to a beginner who knows JavaScript.

Cover:
- What React is
- Why React is used
- Components
- Props
- State

Use simple English and small examples.
```

### Version 4

``` text
You are a React trainer.

Audience:
Students with basic JavaScript knowledge.

Task:
Explain React fundamentals.

Requirements:
- Start with a simple definition.
- Use real-world analogies.
- Explain Components, Props, and State.
- Give one small code example.
- Explain the code line by line.
- Mention common beginner mistakes.

Output:
Use headings, bullet points, and code blocks.
Keep the lesson within 800 words.
```

### Lesson

``` text
Vague Prompt
    ↓
Add Audience
    ↓
Add Context
    ↓
Add Constraints
    ↓
Add Output Format
    ↓
Better Response
```

------------------------------------------------------------------------

# 18. Improving Accuracy

AI can sometimes produce incorrect information.

Instead of:

``` text
Tell me everything about Java.
```

Use:

``` text
Explain Java exception handling.

Requirements:
- Use standard Java concepts.
- Provide a small compilable example.
- Distinguish checked and unchecked exceptions.
- If something is uncertain, clearly say so.
- Do not invent API names.
```

### Useful Accuracy Techniques

-   Give relevant context.
-   Provide the source data when possible.
-   Ask the model to state assumptions.
-   Ask for validation/checks.
-   Break complex tasks into smaller tasks.
-   Verify important facts independently.

------------------------------------------------------------------------

# 19. Improving Creativity

For creative tasks, give freedom while defining the style.

Example:

``` text
Write a short story about an AI assistant helping a software developer.

Style:
- Funny
- Positive
- Suitable for college students

Length:
500 words
```

For more creativity:

``` text
Create 5 different story ideas.
Make each idea different in setting and conflict.
```

------------------------------------------------------------------------

# 20. Improving Consistency

If the same task is repeated, use a fixed structure.

Example:

``` text
For every Java topic, use this format:

1. Definition
2. Why it is used
3. Syntax
4. Simple example
5. Real-world example
6. Common mistakes
7. Interview question
8. Practice task
```

This makes responses more consistent.

------------------------------------------------------------------------

# 21. Evaluating Prompt Effectiveness

A prompt is effective when the output satisfies the required goal.

Use this checklist:

``` text
✓ Is the task clear?
✓ Is the audience clear?
✓ Is enough context provided?
✓ Are constraints clear?
✓ Is the output format clear?
✓ Is the answer accurate?
✓ Is the answer relevant?
✓ Is the answer consistent?
```

------------------------------------------------------------------------

# 22. Practical Prompt Evaluation Exercise

### Prompt A

``` text
Tell me about Python.
```

### Prompt B

``` text
You are a Python trainer.

Explain Python lists to beginners.

Include:
- Definition
- Creating a list
- Adding elements
- Removing elements
- Searching elements
- Modifying elements

Give simple code examples.

Output:
Use headings and code blocks.
```

### Ask Students

Which prompt gives more control?

Why?

### Expected Discussion

Prompt B provides:

-   Role
-   Audience
-   Topic
-   Required subtopics
-   Output format

------------------------------------------------------------------------

# 23. Business Use Case --- Email Writing

## Basic Prompt

``` text
Write an email requesting project status.
```

## Better Prompt

``` text
You are a professional software project coordinator.

Write an email requesting an update on a development task.

Context:
The task is delayed by two days.

Tone:
Professional and polite.

Requirements:
- Ask for the current status.
- Ask for the expected completion date.
- Avoid blaming the developer.

Output:
Provide a concise email.
```

------------------------------------------------------------------------

# 24. Business Use Case --- Marketing Copy

``` text
You are a marketing copywriter.

Create marketing content for an online JavaScript course.

Target audience:
College students and fresh graduates.

Highlight:
- Hands-on projects
- Beginner-friendly teaching
- Interview preparation

Tone:
Professional and engaging.

Output:
- Headline
- Short description
- 5 benefits
- Call to action
```

------------------------------------------------------------------------

# 25. Business Use Case --- Brainstorming

``` text
You are a product strategist.

Generate 10 ideas for an AI-powered learning application.

Target users:
College students.

For each idea provide:

Idea:
Problem solved:
Main AI feature:
Potential benefit:
```

------------------------------------------------------------------------

# 26. Creative Use Case --- Storytelling

``` text
Create a short story about a software developer
who accidentally creates an AI assistant.

Audience:
College students.

Style:
Funny and inspirational.

Length:
600 words.

Include:
- A problem
- A surprising event
- A solution
- A positive ending
```

------------------------------------------------------------------------

# 27. Creative Use Case --- Poetry

``` text
Write a short poem about learning programming.

Style:
Simple and motivational.

Audience:
Beginner programmers.

Length:
12 lines.
```

------------------------------------------------------------------------

# 28. Creative Use Case --- Art Description

``` text
Create a detailed image description for:

"A futuristic AI classroom."

Include:
- Classroom environment
- Students
- AI assistant
- Holographic displays
- Lighting
- Camera perspective
- Overall mood
```

This description can then be used with an image-generation system.

------------------------------------------------------------------------

# 29. Code Generation Use Case

## Weak Prompt

``` text
Create a calculator in JavaScript.
```

## Better Prompt

``` text
You are a JavaScript trainer.

Create a simple calculator using:
- HTML
- CSS
- JavaScript

Requirements:
- Addition
- Subtraction
- Multiplication
- Division
- Clear button
- Basic input validation

Audience:
Beginners.

Output:
Provide complete HTML, CSS, and JavaScript.
Explain how the code works.
```

------------------------------------------------------------------------

# 30. Code Review Prompt

``` text
You are a senior JavaScript developer.

Review the following code:

```javascript
function add(a, b) {
    return a + b;
}
```

Check: 1. Correctness 2. Readability 3. Edge cases 4. Improvements

Output: Issue \| Explanation \| Suggested Improvement


    ---

    # 31. Prompt Chaining

    ## What is Prompt Chaining?

    Prompt chaining means breaking a large task into multiple smaller AI tasks.

    Instead of:

    ```text
    Create a complete training course.

Use:

``` text
Step 1 → Generate course topics
        ↓
Step 2 → Create content for each topic
        ↓
Step 3 → Generate practical examples
        ↓
Step 4 → Generate exercises
        ↓
Step 5 → Generate quiz questions
        ↓
Step 6 → Review the final content
```

### Example

### Prompt 1

``` text
Create 10 topics for a beginner Python course.
```

### Prompt 2

``` text
For each topic, create a simple explanation and one example.
```

### Prompt 3

``` text
For each topic, create one hands-on exercise.
```

### Prompt 4

``` text
Create 20 multiple-choice questions based on these topics.
```

### Why Prompt Chaining?

Large tasks can become easier to control when divided into smaller
steps.

------------------------------------------------------------------------

# 32. Practical Exercise --- Zero-Shot vs Few-Shot

## Task

Ask students to classify customer feedback.

### Zero-Shot

``` text
Classify this feedback as Positive, Negative, or Neutral:

"The application is slow but the design is good."
```

### Few-Shot

``` text
Classify customer feedback.

Example 1:
"The application is very fast and easy to use."
Answer: Positive

Example 2:
"The application crashes frequently."
Answer: Negative

Example 3:
"The application works, but it is average."
Answer: Neutral

Now classify:

"The application is slow but the design is good."
```

### Student Task

Compare both responses.

Discuss:

-   Did examples change the response?
-   Did the output become more consistent?
-   When would few-shot prompting be useful?

------------------------------------------------------------------------

# 33. Practical Exercise --- Role-Based Chatbot

## Student Task

Create a technical interview chatbot.

### Prompt

``` text
You are a JavaScript technical interviewer.

Rules:
- Ask one question at a time.
- Start with beginner questions.
- Gradually increase difficulty.
- Wait for the candidate's answer.
- After each answer, provide brief feedback.
- Then ask the next question.

Start the interview.
```

### Expected Flow

``` text
AI → Question
 ↓
Student → Answer
 ↓
AI → Feedback
 ↓
AI → Next Question
```

------------------------------------------------------------------------

# 34. Practical Exercise --- Prompt Chaining Workflow

## Task

Create a mini workflow to generate a technical training lesson.

### Step 1 --- Topic

``` text
Generate 5 beginner-level JavaScript topics.
```

### Step 2 --- Explanation

``` text
For each topic, provide:
- Definition
- Why it is used
- Simple example
```

### Step 3 --- Practical Exercise

``` text
Create one hands-on exercise for each topic.
```

### Step 4 --- Quiz

``` text
Create 2 multiple-choice questions for each topic.
```

### Step 5 --- Review

``` text
Review the complete lesson.

Check:
- Technical correctness
- Beginner friendliness
- Duplicate content
- Missing explanations

Suggest improvements.
```

------------------------------------------------------------------------

# 35. ChatGPT vs Gemini --- Practical Classroom Activity

The same prompt can be tested in both tools.

### Prompt

``` text
You are a JavaScript trainer.

Explain JavaScript closures to a beginner.

Requirements:
- Simple definition
- Real-world analogy
- Small code example
- Explain the code
- One interview question

Keep the answer beginner-friendly.
```

### Student Activity

Run the same prompt in:

``` text
ChatGPT
   vs
Gemini
```

Compare:

  Area                    ChatGPT   Gemini
  ----------------------- --------- --------
  Explanation clarity               
  Code quality                      
  Examples                          
  Output format                     
  Accuracy                          
  Beginner friendliness             

### Important

The purpose is not to declare one model universally better.

Different models and versions can produce different results depending on
the task, prompt, settings, and date.

------------------------------------------------------------------------

# 36. Prompt Engineering Mini Project

## Project: AI Training Assistant

Create a prompt-based assistant for software students.

### Requirements

The assistant should:

1.  Explain programming concepts.
2.  Give code examples.
3.  Ask interview questions.
4.  Create exercises.
5.  Review student answers.
6.  Generate quizzes.

### Base Prompt

``` text
You are an AI programming trainer.

Audience:
Software students and beginners.

Your responsibilities:
- Explain programming concepts simply.
- Give practical examples.
- Provide beginner-friendly code.
- Ask practice questions.
- Create interview questions.
- Review student answers.

Rules:
- Use simple English.
- Avoid unnecessary complexity.
- Explain concepts before advanced implementation.
- Use code blocks for code.
- Give practical examples whenever possible.

When the student asks for a topic, use:

1. Definition
2. Why it is used
3. Simple example
4. Code example
5. Common mistakes
6. Practice question
```

------------------------------------------------------------------------

# 37. Common Prompt Engineering Mistakes

## Mistake 1 --- Very vague prompt

``` text
Explain AI.
```

### Better

``` text
Explain Generative AI to a beginner.
Use simple English and give 3 real-world examples.
```

------------------------------------------------------------------------

## Mistake 2 --- Too many requirements without structure

Instead of putting everything into one paragraph, organize it:

``` text
Task:
...

Context:
...

Requirements:
...

Output:
...
```

------------------------------------------------------------------------

## Mistake 3 --- Not specifying the audience

Compare:

``` text
Explain APIs.
```

with:

``` text
Explain REST APIs to a beginner who knows basic JavaScript.
```

------------------------------------------------------------------------

## Mistake 4 --- Not specifying output format

Instead of:

``` text
Give me interview questions.
```

Use:

``` text
Create 10 React interview questions.

Return:
Question | Difficulty | Expected Answer
```

------------------------------------------------------------------------

## Mistake 5 --- Trusting AI without verification

AI output should be reviewed, especially for:

-   Programming code
-   Financial information
-   Medical information
-   Legal information
-   Current information
-   Important business decisions

------------------------------------------------------------------------

# 38. Golden Rules of Prompt Engineering

Remember:

``` text
1. Be clear.
2. Give context.
3. Define the audience.
4. Give the AI a specific task.
5. Add useful constraints.
6. Specify the output format.
7. Give examples when needed.
8. Break large tasks into smaller tasks.
9. Test and refine the prompt.
10. Verify important results.
```

------------------------------------------------------------------------

# 39. Quick Revision

## Prompt

Instruction given to an AI model.

## Prompt Engineering

Designing and refining prompts to get useful, relevant, and consistent
results.

## Zero-Shot

``` text
0 examples
```

## One-Shot

``` text
1 example
```

## Few-Shot

``` text
Multiple examples
```

## Role Prompting

``` text
Tell the AI what role or perspective to use.
```

## Structured Prompt

``` text
Organized instructions with clear sections.
```

## Chain-of-Thought

``` text
Encourages solving through logical intermediate steps.
```

## Tree of Thoughts

``` text
Considers multiple possible solution paths.
```

## Directional Stimulus

``` text
Provides hints or direction for how to approach the task.
```

## Prompt Chaining

``` text
Large task → Multiple smaller prompts/tasks.
```

------------------------------------------------------------------------

# 40. Final Student Challenge

Create a prompt for this requirement:

> You are teaching React to students who know JavaScript basics. Explain
> `useState` with a real-world analogy, simple code, line-by-line
> explanation, common mistakes, and a hands-on exercise.

### Expected Student Prompt

``` text
Role:
You are a React trainer.

Audience:
Students who know basic JavaScript.

Task:
Explain the React useState Hook.

Requirements:
- Start with a simple definition.
- Give a real-world analogy.
- Provide a small code example.
- Explain the code line by line.
- Explain common beginner mistakes.
- Give one hands-on exercise.

Constraints:
Use simple English.
Avoid advanced React concepts.

Output:
Use headings, bullet points, and code blocks.
```

------------------------------------------------------------------------

# 41. Trainer Demonstration Flow

For a 2--3 hour practical class, use this order:

``` text
1. What is Prompt Engineering?
        ↓
2. Anatomy of a Prompt
        ↓
3. Basic Prompt Structure
        ↓
4. Zero-Shot
        ↓
5. One-Shot
        ↓
6. Few-Shot
        ↓
7. Structured Prompts
        ↓
8. Role Prompting
        ↓
9. Output Formatting
        ↓
10. Prompt Refinement
        ↓
11. CoT Concept
        ↓
12. ToT Concept
        ↓
13. Directional Stimulus
        ↓
14. Prompt Chaining
        ↓
15. Business Use Cases
        ↓
16. Creative Use Cases
        ↓
17. Code Generation
        ↓
18. Student Exercises
        ↓
19. Mini Project
```

------------------------------------------------------------------------

# 42. One-Sentence Takeaway

> **Prompt Engineering is the skill of giving AI clear instructions,
> useful context, appropriate constraints, examples when needed, and a
> desired output format---and then refining the prompt based on the
> result.**