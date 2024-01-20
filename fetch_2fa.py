"""Find sites with 2fa from https://github.com/2factorauth/twofactorauth and
populate checkpasswords/mfa_sites.txt.
"""

import contextlib
from glob import glob
from pathlib import Path

import git.exc
from git import Repo

with contextlib.suppress(git.exc.GitCommandError):
	Repo.clone_from("https://github.com/2factorauth/twofactorauth", "twofactorauth")
mfaSites = [
	Path(path).name.removesuffix(".json")
	for path in glob("twofactorauth/entries/**/**.json", recursive=True)
	if '"tfa":' in Path(path).read_text(encoding="utf-8")
]
Path("checkpasswords/mfa_sites.txt").write_text("\n".join(mfaSites), encoding="utf-8")
