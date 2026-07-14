# Operating model

## Responsibility boundary

Codex is the lesson manager. It reads local progress, chooses the next target, produces the launch prompt, operates the ChatGPT interface when requested, and records evidence afterward.

ChatGPT Voice is the live tutor. It follows one lesson card, listens, prompts, corrects selectively, and writes the final report in the ChatGPT chat.

The learner controls the live Voice session and decides when Codex may create or change browser state.

## First setup

1. Create the five canonical study files outside the skill repository.
2. Personalize the learner profile.
3. Put the stable Project instructions into one dedicated ChatGPT Project.
4. Use one continuing chat when continuity is useful, or one chat per lesson when the learner prefers cleaner transcripts.
5. Record the chosen ChatGPT organization in the learner profile as a human-readable note. Do not store cookies, tokens, or internal browser identifiers.

## Lesson loop

```text
local evidence -> Codex lesson card -> ChatGPT text prompt -> Voice practice
      ^                                                  |
      |------------- written evidence report ------------|
```

### Before Voice

- Codex reads the latest evidence.
- Codex writes `Next Lesson.md`.
- When asked, Codex opens the intended ChatGPT chat and sends the prompt.
- The lesson card stays visible as text; Voice must not read it aloud.

### During Voice

- The tutor states only the scenario and goal.
- The tutor introduces language inside short exchanges.
- The learner completes one communicative task and one changed retry.
- Codex does not attempt to participate in the real-time spoken exchange.

### After Voice

- ChatGPT writes the report as visible text and does not read it aloud.
- Codex captures the report from the visible chat or from learner-supplied text.
- Codex appends the lesson log and updates only evidence-supported target states.
- Codex prepares the next lesson.

## Browser safety

- Use only the browser surface the learner requested.
- Reuse visible signed-in state without inspecting its storage.
- Check the current Project and chat before creating anything.
- Sending the lesson prompt is authorized when the learner asks to start or set up the lesson.
- Capturing a report is read-only until the learner asks Codex to update progress.
- Never delete conversations, change account settings, or inspect unrelated chats.

## Failure recovery

- If the wrong ChatGPT Project or chat is possible, ask the learner to identify it.
- If Project instructions cannot be edited safely, return them as copy-ready text.
- If the final report is missing, ask ChatGPT in the same lesson chat to write the required report, or ask the learner to paste the transcript into Codex.
- If Voice deviates, stop the lesson and send a compact reset prompt containing only the violated interaction rules and current task.
