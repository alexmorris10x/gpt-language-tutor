# Contributing

Contributions should improve meaningful learner interaction, not make the coach more verbose.

## Change process

1. Describe the learner problem the change addresses.
2. Update the smallest owning file: operating workflow, Voice contract, progress model, or one lesson specification.
3. Keep the installable `SKILL.md` concise and move detailed rules into a directly linked reference.
4. Add or update an automated check when the rule is mechanically testable.
5. Run the automated suite and the relevant manual behavior cases.
6. Include raw prompt/output evidence when proposing a behavior change.

## Lesson requirements

Every lesson must define one real-world scenario, one communicative outcome, 8-12 exposure items, 3-5 productive items, a meaningful task, a changed retry, and at most two correction priorities.

Do not add unsupported claims about proficiency, universal teacher-talk ratios, speech recognition accuracy, or learning outcomes.

## Privacy

Never commit learner names, transcripts, browser state, progress logs, credentials, or private study folders. Use fictional examples in tests and documentation.
