# Contributing to Countdown Timer

Thanks for your interest in improving this project! Everyone is welcome to contribute, whether you fix a bug, add a feature, or improve the documentation.

## Ways to contribute

- **Report a bug:** Open an issue and describe what happened, what you expected, and how to reproduce it. Please include your Python version and operating system.
- **Suggest a feature:** Open an issue and explain the idea and why it would be useful.
- **Improve the docs:** Fix typos or unclear explanations in the README or in code comments.
- **Write code:** Pick an open issue (look for the `good first issue` label if you are new) and send a pull request.

## Getting started

1. **Fork** the repository using the button at the top right of the GitHub page.
2. **Clone** your fork:

   ```bash
   git clone https://github.com/YOUR-NAME/countdown-timer.git
   cd countdown-timer
   ```

3. **Create a branch** for your change:

   ```bash
   git checkout -b my-feature
   ```

4. **Run the app** to make sure everything works:

   ```bash
   python countdown_timer.py
   ```

   You need Python 3.10 or newer. Tkinter is included in most Python installations (on Linux: `sudo apt install python3-tk`).

## Making changes

- Keep each pull request focused on **one thing**. Several small pull requests are easier to review than one big one.
- Follow [PEP 8](https://peps.python.org/pep-0008/) and use clear names for variables and functions.
- Add short docstrings or comments where the code is not self-explanatory.
- Stick to the Python standard library unless there is a strong reason to add a dependency.
- Test your change manually, for example:
  - Start a timer in **Dauer** mode and in **Zieldatum** mode
  - Pause, resume, and reset
  - Enter invalid values and check that an error message appears

## Submitting a pull request

1. Commit your changes with a clear message:

   ```bash
   git add .
   git commit -m "Add alarm sound option"
   ```

2. Push your branch to your fork:

   ```bash
   git push origin my-feature
   ```

3. Open a **pull request** on GitHub against the `main` branch.
4. Describe what you changed and why. If your change affects the interface, add a screenshot.
5. Wait for feedback. You may be asked to make adjustments before the change is merged.

## Code of conduct

Be respectful and constructive. Disagreements are fine, personal attacks are not. Everyone here is learning, so please be patient with beginners.

## Questions?

If something is unclear, open an issue and ask. No question is too small.
