# Testing criteria

Test the system at three levels: package integrity, lesson-card structure, and live tutor behavior.

## Automated package checks

The repository validator must confirm:

- valid skill frontmatter and matching skill name;
- required references, templates, curriculum, and 12 lesson files exist;
- each lesson has one scenario and outcome;
- each lesson contains 8-12 exposure items and 3-5 productive items;
- every productive item appears in the exposure set;
- each lesson defines a main task, changed retry, and no more than two correction priorities;
- stable Project instructions contain the mandatory short-turn, wait, correction, help-ladder, and silent-report rules;
- templates contain no real learner data.

## Prompt inspection

Before sending a generated prompt, verify:

- it identifies the learner as a beginner unless evidence says otherwise;
- it distinguishes exposure from required production;
- it does not tell Voice to read or preview the full vocabulary list;
- it contains the hard turn-length and wait rules;
- it contains one concrete task and a changed retry;
- it embeds the complete report schema;
- it contains no private data beyond what the learner intentionally uses in the lesson.

## Live behavior cases

Run these cases against a fresh ChatGPT lesson chat when tutor behavior changes. Save the raw transcript or output for review, with personal data removed.

### Case 1 — Opening restraint

Start a lesson. Pass when the tutor gives only a short scenario/outcome orientation and a first prompt. Fail when it reads the plan, lists the vocabulary, or explains the teaching method.

### Case 2 — Wait discipline

Remain silent for several seconds after a question. Pass when the tutor waits. Fail when it answers for the learner, adds a second question, or fills the silence with a lecture.

### Case 3 — Turn length

Complete five ordinary exchanges. Pass when each practice turn is one short sentence or one question. Fail when the tutor repeatedly combines explanation, model, question, and answer in one turn.

### Case 4 — Clear first attempt

Produce a target intelligibly on the first attempt. Pass when the tutor moves on and later recycles it naturally. Fail when it demands multiple identical repetitions.

### Case 5 — Help ladder

Say `I don't know`. Pass when the tutor gives only one appropriate support level. Fail when it immediately gives the translation, pinyin, full answer, and extended explanation together.

### Case 6 — Correction restraint

Make two errors in one response, including one error in the productive core. Pass when the tutor waits until the response ends and addresses at most one high-value issue. Fail when it interrupts or corrects everything.

### Case 7 — Changed retry

Complete the main task. Pass when the tutor changes one meaningful detail and asks the learner to achieve the same goal again. Fail when it restarts the identical script.

### Case 8 — Silent report

Finish the lesson. Pass when the tutor says only that the lesson is complete, then writes the full report. Fail when it reads the analytics or report aloud.

### Case 9 — Evidence integrity

Omit any pronunciation task. Pass when the report says pronunciation was not observed or limits the claim. Fail when it invents tone or sound-quality evidence.

### Case 10 — Browser handoff

Ask Codex to start the next lesson. Pass when it checks the visible ChatGPT destination, sends the current prompt, and hands Voice control to the learner. Fail when it uses the wrong chat, duplicates a Project without checking, or changes unrelated browser state.

## Release threshold

A release candidate passes when automated checks are green and cases 1-9 pass on two different lesson scenarios. Case 10 must pass once in the supported Codex browser. Record known model-dependent limitations rather than weakening the criteria.
