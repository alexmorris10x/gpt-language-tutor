# GPT Language Tutor

GPT Language Tutor turns Codex and ChatGPT Voice into one structured language-learning system.

Codex prepares each lesson, opens the lesson in ChatGPT through the Codex browser, and keeps a durable progress record. ChatGPT Voice conducts the live speaking practice. The first curriculum is beginner Mandarin.

## Why this exists

A general voice chatbot tends to talk too much, explain the entire lesson, repeat easy material, and drift into unstructured conversation. This skill gives it a specific scenario, a small productive target, strict turn-taking rules, a help ladder, and an evidence report.

The learner gets:

- a clear real-world goal for every lesson;
- short teacher turns and more speaking time;
- 8-12 useful words and phrases for exposure;
- 3-5 phrases to actively produce;
- corrections that preserve conversation flow;
- progress based on observed evidence rather than generic scores.

## How it works

1. Install the Codex skill from `skill/gpt-language-tutor`.
2. Ask Codex to set up a Mandarin study in a durable personal folder.
3. Ask Codex to prepare and start the next lesson.
4. Codex creates the prompt and sends it to the intended ChatGPT lesson chat through the in-app browser.
5. Start Voice and complete the lesson.
6. Ask Codex to capture the written lesson report and prepare the next lesson.

Personal progress stays in the learner's own study folder. It is never stored in this repository.

## Install

Clone the repository, then copy or symlink `skill/gpt-language-tutor` into your Codex skills directory.

```bash
git clone https://github.com/alexmorris10x/gpt-language-tutor.git
cp -R gpt-language-tutor/skill/gpt-language-tutor ~/.codex/skills/
```

Restart or refresh Codex so it discovers the skill. Then try:

> Use $gpt-language-tutor to set up a beginner Mandarin study.

Or:

> Use $gpt-language-tutor to prepare and start my next Mandarin Voice lesson in ChatGPT.

## Repository map

- `skill/gpt-language-tutor/SKILL.md` — the Codex workflow
- `skill/gpt-language-tutor/references/voice-lesson-contract.md` — exact Voice interaction policy
- `skill/gpt-language-tutor/references/mandarin/` — curriculum and lesson plans
- `skill/gpt-language-tutor/assets/study-template/` — private study-file templates
- `skill/gpt-language-tutor/references/testing.md` — behavioral acceptance criteria
- `tests/` — automated repository checks

## Scope

Version 1 supports beginner Modern Standard Mandarin with simplified Chinese, pinyin, and English scaffolding. The operating model is designed so additional languages can be added later without weakening the Mandarin course.

## Development

Run all local checks:

```bash
python3 skill/gpt-language-tutor/scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

See `CONTRIBUTING.md` before changing tutor behavior or adding lessons.

## License

MIT. See `LICENSE`.
