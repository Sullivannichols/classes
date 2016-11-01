## Brandon Randle | 2016 November 1 | HW3 - OSCP: Prelim

# Part 1
* Speaker is JW
* Preparing for 30 days of labs and the final cert examination.
* First tip: For data processing on text files (such as .csv), import them
into an SQLite database.

```bash
sqlite databasename.db
sqlite> .mode csv
sqlite> .import yourfile.csv yourtable
sqlite> .schema yourtable
sqlite> select count(*) from yourtable;
```

# Part 2
* In preparation for getting in the proper mindset, download and try to break
vulnerable virutal machines.
* JW says he tends to think either too narrowly or too deeply. One needs
to keep one's mind open to the possibilities. 
* JW dislikes the idea of bruteforcing, saying that it lacks skill and
finesse.
* JW read through a bunch of walkthroughs for the vulnerable VMs to get
into the mindset necessary to crack them and to make his attacks on the VMs to
be more constructive.
* Learned how to spawn a TTY shell with python.
```python
python -c 'import pty;pty.spawn("/bin/bash")'
```
* Learned that one can override binary paths on linux with function name
masking
* He says walking through dozens and dozens of walkthroughs to get acquainted
with the tools is how he should have spent his time previously.

# Part 3
* JW read a lot of OSCP reviews online.
* What stood out about the reviews is that people who had no plan and were not
very organized tended to fail the OSCP the first time through. Having a plan
for each kind of host and for how one will spend their time will increase the
rate of success significantly.
* One of the main things people said they did for prep work for the course and
exam is that they tried to make everything as organized as possible. Having a
plan for which exploits to use for which vulnerabilities will save a 
significant amount of time.
* JW provides a number of links with various cheatsheets and other information
to help with preparation.
* Thinking of using omnigraphal for mac. Would use visio for Window, both for
graphing the network.
* Seems like JW supports the idea of trying to crack the VMs first, then 
reading through walkthroughs during/after to compare what he's doing with
what others have tried/have succeeded with.

# Part 4
* Last VLog before access to labs.
* Spent most of the past few days prepping mentally and considering what tools
he would need to 'hit the ground running' once he gains lab access.  
* One of the criteria to pass the OSCP is to document the entire process you
take for the penetration test. Thus, JW has spent some time considering what
tools he will use for documentation.
  * KeepNote - opensource, crossplatform, python-based, gui editor
    * JW says it feels a bit clunky.
  * Dropbox Paper - rich text editor for web, can use screenshots from dropbox
    * these articles tend to get quick long
  * Github w/ Markdown
  * Word with the Offsec pentest template
* This documentation should detail how someone can reproduce the actions you 
have taken and get the same results.
* Been thinking about using something like excel or some sort of network 
diagram to document recon findings. Go graphical or line based?
* One of the basic things he noticed from looking at documentation is that one
should try to create an account for oneself on systems one gains access to in
order to allow future access. This should be done everytime one gains access.
* JW has been looking at PowerShell and netsh which are windows tools.
* Learned about getting a Windows VM and injecting vulnerabilities for
practice.
* Always do UDP scans and not just TCP scans as you could/will miss stuff.
Don't artificially limit yourself.
* Read a walkthrough on how to encode a raw payload to get a reverse shell. 
* In the exam, you are not allowed to use Metasploit to the fullest.
  * Post exploit and exploit modules are generally not allowed, things that
allow automatic exploitation.
  * You can use the utilities, like meterpreter and utility handler.
  * JW wants to do as many things as possible manually in order to learn the
most.
  * Plan when starting is to first get a successful connection to the labs,
get a snapshot of Kali linux and make it ready for exploitation with his
plugins, etc. Then he'll dive into the materials provided, the video course
and the book, before starting to attack the lab machines.

# Part 5
