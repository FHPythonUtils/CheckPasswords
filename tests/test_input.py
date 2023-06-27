from checkpasswords import credentials
from checkpasswords.io import input

passData = [
	{
		"password": "UuQHzvv6IHRIJGjwKru7",
		"login": "lnqYm3ZWtm",
		"url": "https://twitter.com",
		"website": "https://pujol.io",
		"uuid": "44jle5q3fdvrprmaahozexy2pi",
		"otpauth": "otpauth://totp/totp-secret?secret=JBSWY3DPEHPK3PXP&"
		"issuer=alice@google.com&algorithm=SHA1&digits=6&per"
		"iod=30",
		"group": "Test",
		"title": "test1",
	},
	{"group": "Test", "title": "test2"},
]


def test_transformPass():
	assert input.transformPass(passData) == [
		credentials.Credentials(
			name="test1",
			urls=["https://twitter.com"],
			username="lnqYm3ZWtm",
			password="UuQHzvv6IHRIJGjwKru7",
			notes="",
			otpauth="otpauth://totp/totp-secret?secret=JBSWY3DPEHPK3PXP&"
			"issuer=alice@google.com&algorithm=SHA1&digits=6&per"
			"iod=30",
		),
		credentials.Credentials(
			name="test2",
			urls=[],
			username="",
			password="",
			notes="",
			otpauth="",
		),
	]
