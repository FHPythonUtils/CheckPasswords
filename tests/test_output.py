from __future__ import annotations

from pathlib import Path

from checkpasswords import credentials
from checkpasswords.io import output

# ruff: noqa: S106

THISDIR = str(Path(__file__).resolve().parent)


creds: list[credentials.Credentials] = [
	credentials.Credentials(
		name="Example",
		urls=[
			"https://example.com",
		],
		username="example@example.com",
		password="supersecret",
		notes="This is a note",
		otpauth="otpauth://something_something",
	)
]

advancedCreds: list[credentials.Credentials] = [
	credentials.Credentials(
		name="Example",
		urls=[
			"http://example.com",
		],
		username="example@example.com",
		password="supersecret",
		notes="This is a note",
		otpauth="",
	),
	credentials.Credentials(
		name="Example2",
		urls=[
			"https://example2.com",
		],
		username="example2@example2.com",
		password="password123",
		notes="This is another note",
		otpauth="",
	),
	credentials.Credentials(
		name="Example3",
		urls=[
			"https://example3.com",
		],
		username="example3@example3.com",
		password="2346ad27d7568ba9896f1b7da6b5991251debdf2",
		notes="mfa enabled",
		otpauth="",
	),
	credentials.Credentials(
		name="Aegis",
		urls=[
			"https://example3.com",
		],
		username="example3@example3.com",
		password="2346ad27d7568ba9896f1b7da6b5991251debdf2",
		notes="in Aegis",
		otpauth="",
	),
]


def test_simpleMarkdown() -> None:
	fmt = output.markdown(creds)
	Path(f"{THISDIR}/data/simple.md").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/simple.md").read_text("utf-8")


def test_simpleAnsi() -> None:
	fmt = output.ansi(creds)
	Path(f"{THISDIR}/data/simple.ansi").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/simple.ansi").read_text("utf-8")


def test_simplePlainText() -> None:
	fmt = output.plainText(creds)
	Path(f"{THISDIR}/data/simple.txt").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/simple.txt").read_text("utf-8")


def test_simpleJsonF() -> None:
	fmt = output.jsonF(creds)
	Path(f"{THISDIR}/data/simple.json").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/simple.json").read_text("utf-8")


def test_simpleRaw() -> None:
	fmt = output.raw(creds)
	Path(f"{THISDIR}/data/simple.raw.json").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/simple.raw.json").read_text("utf-8")


def test_simpleRawCsv() -> None:
	fmt = output.rawCsv(creds)
	Path(f"{THISDIR}/data/simple.csv").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/simple.csv").read_text("utf-8")


def test_advancedMarkdown() -> None:
	fmt = output.markdown(advancedCreds)
	Path(f"{THISDIR}/data/advanced.md").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/advanced.md").read_text("utf-8")


def test_advancedAnsi() -> None:
	fmt = output.ansi(advancedCreds)
	Path(f"{THISDIR}/data/advanced.ansi").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/advanced.ansi").read_text("utf-8")


def test_advancedPlainText() -> None:
	fmt = output.plainText(advancedCreds)
	Path(f"{THISDIR}/data/advanced.txt").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/advanced.txt").read_text("utf-8")


def test_advancedJsonF() -> None:
	fmt = output.jsonF(advancedCreds)
	Path(f"{THISDIR}/data/advanced.json").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/advanced.json").read_text("utf-8")


def test_advancedRaw() -> None:
	fmt = output.raw(advancedCreds)
	Path(f"{THISDIR}/data/advanced.raw.json").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/advanced.raw.json").read_text("utf-8")


def test_advancedRawCsv() -> None:
	fmt = output.rawCsv(advancedCreds)
	Path(f"{THISDIR}/data/advanced.csv").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/data/advanced.csv").read_text("utf-8")
