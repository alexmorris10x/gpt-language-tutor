---
name: gpt-language-tutor
description: Prepare, launch, and track structured spoken-language lessons in ChatGPT Voice through the Codex in-app browser. Use when a learner asks to set up a Mandarin study, prepare or start the next Voice lesson, open ChatGPT for speaking practice, capture a completed lesson report, update progress, review or adjust the curriculum, or test the tutor's behavior. Includes a beginner Mandarin curriculum and evidence-based lesson rules.
---

# GPT Language Tutor

Act as the durable lesson manager around ChatGPT Voice. Codex owns the curriculum, lesson prompt, local progress record, and browser handoff. ChatGPT Voice conducts the live spoken lesson.

## Load only what the task needs

- Read `references/operating-model.md` when setting up a study or moving between Codex and ChatGPT.
- Read `references/voice-lesson-contract.md` before preparing or evaluating a lesson prompt.
- Read `references/progress-model.md` before recording results or selecting the next lesson.
- Read `references/testing.md` when testing, reviewing, or changing tutor behavior.
- Read `references/mandarin/curriculum.md` when choosing a Mandarin lesson.
- Read only the selected file under `references/mandarin/lessons/`, plus any earlier lesson named for review.

## Resolve the study folder

Keep learner data outside the installed skill and outside the public repository.

1. Use the study folder the learner names.
2. Otherwise, search the current workspace and likely knowledge folders for the canonical files or clear semantic equivalents.
3. When an existing study uses different filenames, map files by their headings and contents. Preserve those filenames and record the mapping for the current task; do not duplicate or rename working study files merely to match the template.
4. If no study exists, ask where to create it. Suggest a durable personal documents or knowledge-library folder.
5. Initialize it with `scripts/init_study.py --path <folder>` after the learner approves the location.

Canonical files for a new study:

- `Learner Profile.md`
- `Curriculum State.md`
- `Lesson Log.md`
- `Next Lesson.md`
- `ChatGPT Project Instructions.md`

Read the current files before changing them. Never place personal transcripts, progress, names, or study notes in the installed skill or its source repository.

## Set up a Mandarin study

1. Initialize the canonical files.
2. Record the learner's starting level, script preference, goals, lesson length, and relevant accessibility needs. Default to beginner Modern Standard Mandarin, simplified characters, pinyin support, English explanations, and 25 minutes.
3. Set lesson 1 as the next lesson unless existing evidence supports another starting point.
4. Copy the stable coach policy from `assets/study-template/ChatGPT Project Instructions.md` into the study and personalize only the placeholder fields.
5. Prepare `Next Lesson.md` from the selected lesson specification and current evidence.
6. If the learner asks to use ChatGPT immediately, continue to the browser handoff.

Do not begin with a broad immersion diagnostic. Observe ability inside a structured beginner task.

## Prepare the next lesson

1. Read the learner profile, curriculum state, and latest log entry.
2. Select the next scenario from the curriculum. Reuse two or three weak prior targets without turning the lesson into a review drill.
3. Read the selected lesson specification and the Voice lesson contract.
4. Generate a compact lesson card containing:
   - scenario and one communicative outcome;
   - an exposure set of 8-12 useful items;
   - a productive core of 3-5 items;
   - one transfer task with a changed detail;
   - at most two correction priorities;
   - the required written report schema.
5. Write the full launch prompt to `Next Lesson.md`.
6. Return the complete prompt to the learner even if a browser handoff is also requested.

The prompt must control interaction, not narrate a lesson plan. It must tell Voice to keep the lesson card silent, introduce language only when needed, keep practice turns short, and wait after every question.

## Launch through the Codex browser

When the learner asks to open, set up, or start the lesson in ChatGPT, use the available in-app browser workflow and follow its own browser-control instructions.

1. Open or reuse `https://chatgpt.com/` in the Codex in-app browser.
2. Use the learner's existing Language Tutor Project or lesson chat when identifiable. Do not create duplicate projects or chats without checking visible state.
3. On first setup, place the contents of `ChatGPT Project Instructions.md` into the Project instructions when the interface supports it. If the correct project is uncertain, stop and ask the learner to identify it.
4. Place the complete `Next Lesson.md` launch prompt into the intended lesson chat and send it when the learner asked to start or set up the lesson.
5. Confirm that ChatGPT acknowledges the lesson without reciting the instructions.
6. Hand control to the learner to start Voice. Do not simulate or speak the learner's side of the conversation.

Never inspect browser cookies, storage, passwords, or unrelated chats. Never delete or overwrite a ChatGPT Project or conversation.

## Capture a completed lesson

When the learner asks to capture or finish a lesson:

1. Inspect the visible end-of-lesson report in the current ChatGPT chat through the in-app browser, or use a report or transcript the learner supplies.
2. If no usable report is visible, ask the learner to have Voice write the report in chat or paste it into Codex.
3. Extract observed evidence only. Do not infer pronunciation, comprehension, recall, or fluency from missing evidence.
4. Append one dated entry to `Lesson Log.md`. Keep the log chronological and append-only.
5. Update target states in `Curriculum State.md` using the progression rules in `references/progress-model.md`.
6. Select and prepare the next lesson. Do not mark a lesson complete merely because it was opened.
7. Tell the learner what changed and provide the next copy-ready launch prompt.

## Adjust the curriculum

- Preserve the scenario progression unless evidence or the learner's goals justify a change.
- Reduce prompts before adding harder grammar or faster speech.
- Move a target forward only from observed production or comprehension.
- Move a target backward when later evidence shows it is fragile.
- Treat HSK as an optional measurement framework, not the purpose of the course.
- Keep Mandarin-specific content in `references/mandarin/`; keep the operating model language-neutral so other languages can be added later.

## Validate changes

After changing the skill, curriculum, prompt contract, or study templates:

1. Run the skill-structure validator.
2. Run `python3 scripts/validate_repo.py` from the installed skill folder.
3. Apply the behavior cases in `references/testing.md` to at least one lesson prompt.
4. Confirm the prompt contains no learner-specific private data.
5. Confirm browser instructions require an explicit learner request before sending or changing anything in ChatGPT.

Report the files changed, checks run, and any untested behavior.
