# Automated Python Wrapper for Lynda-Decryptor
This tool is the easiest way to bulk decrypt all offline Lynda videos to .mp4 format with a proper folder structure and naming.

The original tool was made by h4ck-rOOt this slight rework adds an interactive Python wrapper and automation for getting many courses' videos with one click.

## Usage
- Clone or download the repository and run lynda_decryptor.py from a command prompt
- Input the pathes to your course directory and db.sqlite (can be found from the options menu of the Lynda desktop app)
- Select "A" to decrypt all downloaded courses, this also removes the encrypted files once done.

\*\*Alternatively select "D" to individually decrypt courses by ID\*\*

[Check out the video tutorial for a step by step guide.](https://youtu.be/9cZegRRVPiU)

## Limitations
This program is **windows only** at the time of this writing. You can compile it under Linux and Mac using [Mono](http://www.mono-project.com/) or [DotNetCore](https://www.microsoft.com/net/core), with some changes due to the sqlite platform binding.
