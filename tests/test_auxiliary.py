from pathlib import Path

from checkpasswords import auxiliary

THISDIR = str(Path(__file__).resolve().parent)


def test_isMfaEnabled_top20():
	assert all(
		auxiliary.isMfaEnabled(x)
		for x in Path(f"{THISDIR}/data/mfa.txt").read_text("utf-8").strip().splitlines()
	)


def test_isMfaEnabled_10k():
	# Note 4 words removed such as duopoly
	assert not any(
		auxiliary.isMfaEnabled(x)
		for x in Path(f"{THISDIR}/data/10k.txt").read_text("utf-8").strip().splitlines()
	)


def test_isHttp_true():
	assert auxiliary.isHttp("http://example.com")


def test_isHttp_false():
	assert not auxiliary.isHttp("https://example.com")


def test_entropyLen_0():
	assert auxiliary.entropyLen("a" * 8) == 0


def test_entropyLen_8():
	assert auxiliary.entropyLen("ab" * 4) == 8


def test_entropyLen_16():
	assert auxiliary.entropyLen("abcd" * 2) == 16


def test_entropyLen_24():
	assert auxiliary.entropyLen("abcdefgh") == 24


def test_entropyLen_64():
	assert auxiliary.entropyLen("abcdefghijklmnop") == 64


def test_passwordPrint_6():
	assert auxiliary.passwordPrint("a" * 6) == "*" * 6


def test_passwordPrint_7():
	assert auxiliary.passwordPrint("a" * 7) == "a" * 2 + "*" * 3 + "a" * 2


def test_passwordPrint_8():
	assert auxiliary.passwordPrint("a" * 8) == "a" * 2 + "*" * 4 + "a" * 2


def test_passwordPrint_99():
	assert auxiliary.passwordPrint("a" * 99) == "a" * 2 + "*" * 95 + "a" * 2


def test_isMfaAvailable_true():
	assert auxiliary.isMfaAvailable("https://mail.google.com")


def test_isMfaAvailable_false():
	assert not auxiliary.isMfaAvailable("https://this_site_does_not_exist.this_site_does_not_exist")
