# Automated Python Wrapper for Lynda-Decryptor
This tool is the easiest way to bulk decrypt all offline Lynda videos to .mp4 format with a proper folder structure and naming.

The original tool was made by h4ck-rOOt this slight rework adds an interactive Python wrapper and automation for getting many courses' videos with one click.

## Usage
### Arguments
**--all**: (recommended option) automatically decrypts all courses that were downloaded  
**--list**: list the course IDs of all downloaded Lynda courses that have not previously been decrypted
**--id**: (takes one or more arguments) provide ID(s) of courses to individually decrpyt and output their videos
**--cached**: the first time you run the script you'll have to set up paths, this option can be used any time after the first to skip this step

## Limitations
This program is **windows only** at the time of this writing. You can compile it under Linux and Mac using [Mono](http://www.mono-project.com/) or [DotNetCore](https://www.microsoft.com/net/core), with some changes due to the sqlite platform binding.
