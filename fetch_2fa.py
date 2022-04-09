"""Find sites with 2fa from https://github.com/2factorauth/twofactorauth and populate checkpasswords/mfa_sites.txt
"""

from glob import glob
from pathlib import Path

import git.exc
from git import Repo

try:
	Repo.clone_from("https://github.com/2factorauth/twofactorauth", "twofactorauth")
except git.exc.GitCommandError as e:
	print("clone failed")
	print(e)
mfaSites = [
	Path(path).name.removesuffix(".json")
	for path in glob("twofactorauth/entries/**/**.json", recursive=True)
	if '"tfa":' in Path(path).read_text(encoding="utf-8")
]
Path("checkpasswords/mfa_sites.txt").write_text("\n".join(mfaSites), encoding="utf-8")
