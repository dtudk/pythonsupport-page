# Scuffed Scraper of DTU Courses
This script helps interpret and reason about DTU courses.

Concretely, it:
- Downloads DTU course pages (as the relevant `robots.txt` encourages), scrapes it to generate a search URL for all courses, then scrapes that to determine all DTU courses.
- Downloads a course `.html` file from `kurser.dtu.dk/course/<course_id>`, one for `en`, one for `dk` - only what is missing.
- Scrapes each course HTML pair into an accessible, convenient TOML file.

To use the output of this script, see "Using the Course TOMLs".

**Please be respectful of external servers when using this script**.

## Dependencies
This script requires `python` version `3.11+`.

Additionally, you'll need to install all packages in `requirements.txt` to a virtual environment.

## Usage
Using `python` version `3.11+`, after installing from `requirements.txt`, run the following:
```bash
python main.py
```

With `podman`, all environmental concerns can be made very simple:
```bash
podman run --rm -it -v .:/app-src -w /app-src docker.io/python:3.11-slim-bookworm bash
>>> pip install -r requirements.txt
>>> python main.py
```

Scraping requires many downloads, and may thus take awhile.

## Caching
**HTML is not downloaded if found in the cache**.
To re-scrape an HTML file, delete it and re-run.

The following are the local caches produced/used by the script, and are not checked into `git` (see `.gitignore`):
- `course-scrapes/<lang>`: Course HTMLs for all DTU courses, in all languages.
- `search-scrapes`: HTML for the DTU course search page.
- `courses`: Course TOMLs for all DTU courses.

## Why is the Course TOML Incomplete?
Not every course page parameter is scraped into the TOML. You are, however, free to modify the script under the terms of the license to scrape extra course data.




# Using the Course TOMLs
This section describes some common things you might want to do using the Course TOMLs.

## Keyword Search w/`grep`
The `<course_id>.toml` files are 

To search the courses for a keyword, including the line of the match (for context), use:
```bash
grep -rn 'Python'
```

To just get the list of courses with any match, use:
```bash
grep -rl 'Python'
```

You can use the usual `grep` regex:
```bash
grep -rn '[pP]ython'
```

## Ingesting into Python
In `python` version `3.11+`, TOML is very easy to work with.
Here's a small example.

```python
from pathlib import Path
import tomllib

SCRIPT_PATH = Path(__file__).parent
for path_course in SCRIPT_PATH / "courses").glob("*.toml"):
    with path_course_config.open() as f:
        course = tomllib.loads(f.read())
    
    ## Use "course" to do whatever you'd like.
    print(course)
```

See `tomllib` (https://docs.python.org/3/library/tomllib.html) for more details.



# Code Quality / Style
No. Good luck!



# License
This software protects your rights as a user.
For details, see `LICENSE` and/or the header of all `.py` files.
