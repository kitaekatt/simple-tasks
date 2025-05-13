Below is the system prompt sent to gpt4.1-mini to create this system. While you can use this git repository, consider modifying this prompt and doing it with your favorite agent to create your own!
---
## **Required Documents**
Create the following documents and place them in your project’s document folder, e.g., `./docs`. You are responsible for authoring these documents.

1. *`task.md`*: The main guide for the task management system. It outlines common task operations, task types, and, for each task type, the corresponding task template. It includes instructions on how new tasks are generated from templates. It includes your tips for template design, or you can start with mine.
2. *`task-type-template.md`*: A template for each task type, like “repeatable” or “one-shot,” with a structured layout for the info needed to work on the task. It can include instructions for the AI. Start with a *`task-general-template.md`* to test the system or to customize.

## **Common Operations**
Start with these:
  * Create a Task(template, context): Produces a unique task document based on the provided template and context. This task document must stand alone as the basis for the Work on a Task operation defined below.
  * Update a Task(task file): Updates a task to the latest template format.
  * Work on a Task(task file): Executing the instructions in the task until the task is completed.

## **Template Design**
I’ve found these sections generally useful in task templates but make it your own!
* **Version Number**: {#.##} Update this with each template revision. Helps the AI upgrade tasks to newer versions.
* **Document Update Workflow**: Instruct the AI to update the document only when you say, e.g., “save this task.” Creates a resumable record of the task’s current state.
* **Critical Documents**: {list of document references} List required documents to be fully read for this task type or specific task. Requires tool calls but ensures a single source of truth.
* **Useful Documentations**: {list of {document reference, context summary, for more info}} List optional documents with a short summary tailored to the task and guidance on when to read the full document. Reduces tool calls and context window size.
  * Example document reference: `./docs/terminal_best_practices.md`
  * Example context: Use Unix-style shell commands; create support scripts when many commands are necessary.
  * Example for more info: Read the full document for tips on grep, git, or script creation.
* **Objective**: {description} The goal the AI is working toward.
* **Project Status**: {description} Updated with each document revision to reflect the task’s current state and context for a new AI to pick up where the last one left off.
* **Retro Notes**: {instruction} Tell the AI to log non-essential notes, like tool errors and how they were resolved, to improve future work.
