# School — project page content

**Source of truth for** [`school.html`](school.html), the page that opens from the **School** row of the landing's work list (first build 2026-10-10).
Layout follows [`book.md`](book.md) and [`styupan.md`](styupan.md): the header (back link, eyebrow, headline, meta row), a large first image, then About and the work. The photo and screen rhythm (a photo, a short text, two screens, zigzagging left and right) follows her reference, Reino Studio's Bright Flag case (reinostudio.com.br/works/bright-flag), sent 2026-10-10.

---

## Facts
| | |
|---|---|
| What it is | An iOS app concept for remote learning and good habits, for pupils and teachers |
| Type | Personal project, UI/UX design concept |
| Her role | Research, UX, UI (the whole project) |
| Year | 2020 *(estimate from the screens: the calendars show September 2020 and the school year 2019/2020; to confirm with her)* |
| Platform | iOS (screens drawn at 375 × 667, iPhone 8 size) |
| Tool | Sketch |
| Language of the UI | Ukrainian |
| Colours | Yellow #FFD60A, Navy #001059 (from her logo SVG) |

Sources: her Behance case [IOS App_School](https://www.behance.net/gallery/150359877/IOS-App_School) (problem, goal, solution, process, personas, customer journey map), read 2026-10-10; her Google Drive folder for the project (screens for pupil and teacher, logo, `UX reserch.png` with the proto-personas and the journey map in Ukrainian), read 2026-10-10; her Figma file MY-PROJECTS, frame 913:70584 (the first block).

## Page copy
- **Eyebrow:** iOS app
- **Headline:** Remote learning that works like a social feed, for pupils and their teachers.
- **Meta row:** Role — Research, UX, UI · Year — 2020 · Platform — iOS · Tool — Sketch
- **About:** School is an iOS app concept for remote learning. Pupils and teachers share one space: lessons and homework come from the teacher, and challenges, small goals that run for a set time, can come from anyone in the class.
- **Problem:** Wars and pandemics took away children's chance to learn in an interesting way. During the quarantine, lessons moved to Viber and Zoom, and young pupils quickly lost interest.
- **Goal:** Make distance learning interesting.
- **Solution:** An app that works like a social network. Pupils create challenges that last for a while and help them build good habits; teachers control the content and organise the learning.
- **Process:** Research · Prototyping · Testing · UI and interactions.

## Sections, in order
1. **First block** — rebuilt in HTML and CSS after her Figma frame 913:70584: a yellow band, a large navy circle at the top right, a half navy, half yellow circle on the left edge, "UI/UX design concept", the "iOS App" pill, "School" and "Mobile service for remote learning and development of good habits". The old iPhone Xs mockup is replaced by a modern phone frame (her request, 2026-10-10: "not a mockup but a frame"), built in CSS: a thin black bezel, a light titanium rim, side buttons, a Dynamic Island and a new status bar (9:41). The frame shows the onboarding screen ("Я вчитель" / "Я учень"). The phone rises in once when the page opens.
2. **About / Problem / Goal / Solution / Process.**
3. **In use** — five groups, each a photo, a short text and two screens; groups alternate left and right. The photos are AI images generated with Figma AI (gpt-image-2.5, her Pro plan, 2026-10-10), not real people, in the project's warm yellow and navy. The screens are her Sketch exports from Drive, the old 2020 status bar cropped off and shown at 2× in the modern frame. Phones rise in as they scroll into view; the two long screens (home feed, lesson) scroll slowly inside the frame while visible. With reduced motion there is no movement.
   1. *Photo:* two children at home on the floor with books, laughing at a phone (wide, 1536 × 864, `kids-home`). *Text:* **Challenges, not another video call.** Pupils open a feed of challenges from classmates and teachers, sorted by sport, travel, creativity and study. Each one runs for a set time, like "English every day", and turns a small task into a habit. *Screens:* home feed (scrolls), challenge.
   2. *Photo:* a teacher at her kitchen table in the evening, preparing a lesson with books and a phone (square, 1024, `teacher-prep`). *Text:* **A lesson in three steps.** The teacher picks a date, adds photos, video and files, and publishes. The class was chosen at sign-up, so the lesson reaches the right pupils, and the homework sits right under it. *Screens:* new lesson, lesson (scrolls).
   3. *Photo:* a boy running down the hallway to show his mother something on a phone (portrait, 960 × 1280, `kid-runs`). *Text:* **Homework that answers back.** Pupils send homework with a comment and files. A notification tells them when the teacher has commented on it or graded it, so nobody waits for a parent to forward a message. *Screens:* homework, notifications.
   4. *Photo:* two teachers on a sofa with books, laughing at something on a phone (wide, 1536 × 864, `teachers-laugh`). *Text:* **Challenges between teachers, with moderation.** Teachers start challenges for their class, for other teachers or for everyone. Challenges created by pupils wait for the teacher, who allows or declines them. *Screens:* new challenge with its audience, challenge waiting for moderation.
   5. *Photo:* a girl proudly showing her parents a paper sunflower and her notebook (portrait, 960 × 1280, `kid-crafts`). *Text:* **Progress you can see.** Every homework has a status: done, being checked or not done. The teacher grades it out of 100, and the pupil sees the result in the profile. *Screens:* grading a homework, the pupil's homework list.
4. **Target audience** — two cards, Teacher (yellow) and Pupil (navy), from the Behance case and the proto-personas in `UX reserch.png` (translated from Ukrainian):
   - *Teacher.* Persona: people aged 21 to 60 with a university degree, with or without a family, working as teachers. Proto-persona: Tetiana, 35, a primary-school teacher; in the long quarantine she had to teach online over Viber and Zoom and could not find a free service that pupils could reach. Goal: carry out the school curriculum with the pupils. User story: as a teacher I want to publish material for the children, check how they do it and keep their attention on learning. Needs: one service for pupils and teachers; give material to study; set and check homework; extra features that make learning interesting.
   - *Pupil.* Persona: pupils aged 6 to 18, with or without a family, with different abilities. Proto-persona: Maksym, 9, in year 3; he spent part of the quarantine at his grandmother's, with no computer, and his learning stopped. Online lessons felt boring, and he kept waiting for his parents to send him the homework. Goal: learning, and keeping in touch with classmates. User story: as a pupil I want to spend enough time with my classmates and study. Needs: something interesting, not only lessons; see what classmates do; go back to a lesson he missed; know about homework at once and get reminders.
5. **Customer journey map** — subtitle: "Teacher and pupil, four stages". Intro: "The journey map showed the gaps I had missed and helped me fix them in the first stage." Two tables (stages Attraction, Activation, Involvement, Retention; rows Goal, Thoughts and feelings, Problem, Solution), problem cells marked; on narrow screens each table scrolls sideways. Text from the Behance case, edited for grammar:
   - *Teacher.* Goal: find an interesting tool for teaching remotely · create lessons · grade homework and make something interesting for the children · create challenges between teachers. Thoughts: had to register right after installing, did not like it · not clear how the children would find the lessons · liked watching the children's activity in a challenge, but not clear who can take part · children create many events, and some are not safe. Problem: people want to look around before signing up · no way to see lessons and tasks for one class · a challenge has no defined audience · no control. Solution: let people browse first and ask them to sign up only when they act · choose the school and class at sign-up · choose a category and an audience when creating a challenge · more filters when creating, and moderation.
   - *Pupil.* Goal: distance learning is boring, spend the time in an interesting way · create a challenge or join one · finish the challenge and send the homework · create more challenges. Thoughts: had to register right after installing, did not like it · made a mistake while creating and could not edit it · fun to take part, but how do I know the teacher has seen my homework? · cannot create more than one challenge a month. Problem: people want to look around before signing up · a challenge cannot be edited · the teacher cannot grade · limited options. Solution: let people browse first and ask them to sign up only when they act · allow editing · the teacher gives homework a status and a grade · more options for a fee.
   - *From the map to the screens:* two screens after the tables, sign-in (Google, Facebook or email) and choosing the school, year and class.

## Accessibility
- Each photo and each screen has a text alternative; the first block is a figure with its text as real text.
- Navy #001059 on Yellow #FFD60A: 12.2 : 1 (the same pair both ways); Navy on white: 17.2 : 1. Yellow on white fails (1.4 : 1), so yellow is used only as a ground, never as text on white.
- The journey map is a real table with row and column headers; its scroll box can be reached with the keyboard.
- Motion (the phones rising in, the long screens scrolling) stops with `prefers-reduced-motion`.
