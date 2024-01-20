"""CheckPasswords Utility.

Uses pass_import to read password manager source files, detecting duplicates, weak passwords,
HTTP sites, and providing 2FA options.

Details:
The "checkpasswords" tool leverages pass_import to extract information from password manager source
files. It automatically deduces various data points such as zxcvbnScore, password duplicity, HTTP
site identification, and the availability/enabled status of multi-factor authentication (MFA).

Functionality:

- Duplicate Password Check: Identify and flag duplicate passwords within the source file.
- Weak Password Detection: Evaluate password strength using the zxcvbnScore algorithm.
- HTTP Site Identification: Detect and list sites using HTTP.
- 2FA Options Listing: Use data from https://2fa.directory/ to present available multi-factor
  authentication options.
- Emails for Security Checks: Compile a list of emails for submission to services like HIBP
  (Have I Been Pwned) for security validation.
"""

import argparse
from sys import stdout

from pass_import.__main__ import MANAGERS

from checkpasswords.io import input as input_
from checkpasswords.io import output


def main() -> None:
	"""Establish the main entry point."""
	outputMap = {
		"ansi": output.ansi,
		"plain": output.plainText,
		"markdown": output.markdown,
		"json": output.jsonF,
		"raw": output.raw,
		"raw-csv": output.rawCsv,
	}
	parser = argparse.ArgumentParser(
		description=__doc__, formatter_class=argparse.RawTextHelpFormatter
	)
	parser.add_argument(
		"credentials",
		help="Credentials/ passwords file to check",
	)
	parser.add_argument(
		"--output-format",
		"-o",
		help=f"""
Output format. One of {list(outputMap)}. default=ansi""".replace(
			"\n", ""
		),
	)
	parser.add_argument(
		"--input-format",
		"-i",
		help=f"""
Input format. One of {MANAGERS.names()}""".replace(
			"\n", ""
		),
	)
	parser.add_argument(
		"--file",
		"-f",
		help="Filename to write to (omit for stdout)",
	)
	parser.add_argument(
		"--no-colour",
		"-z",
		help="No ANSI colours",
		action="store_true",
	)

	args = parser.parse_args()
	# File
	filename = stdout if args.file is None else open(args.file, "w", encoding="utf-8")

	outputFunction = outputMap.get(args.output_format, output.ansi)
	# no_colour
	if outputFunction == output.ansi and args.no_colour:
		outputFunction = output.plainText

	print(
		outputFunction(input_.passImport(args.credentials, args.input_format)),
		file=filename,
	)


if __name__ == "__main__":
	main()
