# TODO list

- [ ] Find a method to do *continuous* Docker builds.

- [ ] Observe (and mabe fix) /lineplot_today, as it continues (for how many
  hours into the night?) showing the last day after midnight.

- [ ] Set up Travis.

- [ ] Assure this runs on all targeted 3.x versions.

- [ ] Review/ complete test cases.

- [ ] Terminology cleanup in doc and docstrings.

- [ ] Heatmap: hover texts should include hour

- [ ] Reduce *image size* (python:3.7 alone is > 900MB). If falling back to
  python:3.7-slim, a build toolchain for regex package would be required.

- [ ] Introduce speedtest_lab style comparisons with 2nd sensor