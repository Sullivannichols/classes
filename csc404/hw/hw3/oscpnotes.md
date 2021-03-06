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
* Day 1 of materials and lab access
* Spent 4.5 hours in study: 1hr 52 min on videos, the rest on the written
materials and working exercises. 
* Managed to get through 33% of the written materials.
* Been using VLC to directly view materials instead of their web interface.
  * VLC allows him to set playback speed (he uses 1.33) for 33% overdrive so
it's faster than standard delivery speed.
* Even with the speed up, he spends a lot of time with the videos paused, 
meaning he's doing a lot of hands-on work with the exercises in the middle of
the videos. 
* The material starts out pretty basic and moves up to more difficult things
quickly.
* When asked to cut down a tree, spend the majority of your time sharpening
the axe.
* Managed to find one of the quite difficult machines (Sufference) 
* Spent a lot of time on lab recon
* Learned intel that has helped him in the real world
* JW's a bit overwhelmed by how much information is being presented
* Decided to go with Keepnote for work-in-progress things and then document the
information officially in a report once done with the machine

# Part 6
* Days 2 and 3
* Spent 8 hours of study, progressing 1hr40m in video material and 50 more
pages of the book. Spent a lot of time running scans.
* Continuing to use KeepNote for raw report data, and using excel for recon 
data. 
* The first reverse shell was guided step-by-step by the materials.
* The next exercise the materials were hands-off and made you do it yourself. 
* JW spent a lot of time doing something then discovered a significantly
easier way to do it. A hard lesson learned.
* Important to read through things intentionally and think through stuff in
order to avoid doing stupid things and wasting time.
* Learned how to resume nmap scans if paused.
  * This only works if you don't suspend the VM in the background.
```bash
nmap -oN your-results.nmap $HOST
Ctrl-C^ here
# then later
nmap --resume your-results.nmap
```
* There's tons of versions of windows out there - know them well. 

# Part 7
* Days 4 and 5
* Started getting some realworld exploits from offsec's exploit database 
* you should always verify the contents of an exploit to be sure it contains
what it's supposed to. And if you don't verify the contents, don't run it on 
anything except a snapshotted vm. The contents could be dangerous.
* Learned about different ways to do file transfer other than ftp and ssh.
The course material teaches various ways to do such file transfer.
* JW noticed that there's not much difference between the videos and the
exercises, so he's stopped watching the videos and has focused on reading the
pdf alone. 
* Java applets tend to be vulnerable and insecure in general.
* JW breezed through the chapter on web app security since he's spent a lot of
time in the field already. 
* JW is currently 75% through the material in the first five days.
* JW figured out he should be running long-running nmap scans in the 
background while he's working on other material. This will allow him to hit
the ground running once he has the exercises complete as it will have much of
the data collection done.

# Part 8
* Day 6
* Succeeded today in getting his first shell on a machine and getting the
proof.txt file that verified his access.
* On page 300 of the material, less than 100 pages left. 
* Next step in the material is metasploit. 
* "Just relying on automation is not good."

# Part 9
* Days 7 and 8
* Finished the materials between days 6 and 7.
* Was able to get into his first windows and linux boxes.
* At the end of the materials, you're left all alone in a forest of unknown 
machines without any idea of where to go. Suddenly progress is completely
dependent upon you and not upon the materials guiding you.
* Gather information, enumerate, and try harder.
* nmap is a very powerful tool - learn it well.
* nmap with metasploit stores the info in a relational db.
* JW reccommends checking out Metasploit Unleashed before beginning PWK.

# Part 10
* Days 9, 10, and 11
* Successfully pivoted into a subnet.
* Noticed that mindset is beginning to change. Moving from defender/blue
mindset to attacker/red mindset. 
* Whereas metasploit is limited in the exam, offsec states that the labs are
for learning, so metasploit is OK, especially in situations where it will
help you learn more.
* Posted a link for a video about metasploit, very enlightening, good to watch 
* Security misconfigurations are the biggest threat to anything. Such things
require knowledgeable sysadmins.
* Beta sites / demo sites shouldn't be tied to the data from the production
site.
* Don't assume anything. Always poke for holes in security.

# Part 11
* Days 12, 13, and 14
* Halfway point of the course.
* Big tip: start scanning from the first day with the tools that are taught and
then document the results of the scans in an organized manner.
* The paradox of choice - the more choices, the less choices you have. Watch
the Ted talk to explore the concept further.
* Beginning to feel that KeepNote is not doing the job for him. It's clunky
and rigid he feels.
 
# Part 12 
* Days 15, 16, and 17
* Everyone's different in terms of how they'll progress.
* Again, pay lots of attention to the manual and the notes one takes, and think
through things. This'll save lots of time and frustration.
* Again, study and learn Metasploit Unleashed. It really helps teach what is 
all possible and the various tools you can use.
* Do capture-the-flag contests and work with vulnerable VMs to practice using
the various tools and get comfortable with them. 
* Prepare scripts to make more things automated to save time, especially in
case of situations where shell access may be short-lived.
* Check out ctftime.org to get into CTFs

# Part 13
* Days 18 - 21
* "Work smart. Not hard. Try Harder just means Try More, not More Complex."
* Oftentimes, a difficult box will not necessarily be difficult to break, it
just has a vulnerability that one has not discovered yet. Keep enumerating.
* "This course is boot camp." This is basicallly bootcamp for infosec.

# Part 14
* Days 22 - 25
* Can use BITS for downloading on windows command line (kinda like wget)
* Don't allow elation from success to cloud your judgment and focus. Act
professionally and stick to the plan. Act slowly and with purpose.
* Don't allow the same elation to slow down the post-exploitation process.
Quickly get the post-exploit tasks complete.  

# Part 15
* Days 26 - 30
* Upset at himself for slacking on his documentation
* He forgot to take screenshots in some instances on account of his elation
* Always have logs of your sessions. LOG EVERYTHING.
* Plough through all of Metasploit Unleashed BEFORE the course.
* Start recon on the network ASAP.
* Planning to have scripts together to automate the post-exploitation process
by creating him a new account with a predefined password that has root access,
sudo access, and is in every group on the system.

# Part 16
* Day before the exam
* Made a plan for the day of the exam to help keep focused during the exam
* Planning what sorts of payloads to be delivered to exploited systems
* Has a set of nmap scripts prepared with bash profile
* Is planning to have a while loop that takes a screenshot every five seconds
* Has a list of things to do every time when approaching a system
* Intends to have all recon complete within first hour
* Has a very intentional plan for how to spend his time, both working, breaks,
and sleep.
* Has a handful of exploits prepared for various systems

# Part 17
* Hasn't finished recon by 3 hour mark
* 30 days of lab is really rushed. 200-300 hours is a baseline.
* Just remembered a note from Dr. O - need around 40-50 compromised machines
in the labs in order to really be prepared for the exam.
* It's exceedingly important to have a very high level of attention to detail.
Missing one small piece of information can make one waste hours and hours of
time.
* Ensure that recon plans are comprehensive.
* Don't get tunnelvision.
  
# Part 18  
* The main thing JW thinks he was lacking is SOP or TTP - Standard Operating
Procedures or Tools, Tactics, and Procedures. Adhoc is not the way to go
about this sort of thing. All basic things should be easily mapped out to some
sort of SOP.
* One example: Have a standard nmap script to scan all 65000 ports on a system
to identify anything unusual. Unknown services running on nonstandard ports?
Flag it to check it out.
* Don't rush things. Take your time to do things correctly and in an
organized matter.
* If you face an inexplicable problem, first, explain the situation to yourself
out-loud as if you were a novice, then give yourself suggestions as if you were
the senior. Explain all of the potential things they could be doing wrong and
then check your things again. Essentially the idea is to get out of your own
head and objectify the process.
* Again, have all of the basic, standard tasks automated and standardized.

# Appendix A
* How to ask questions and how to receive help
* Outside of OSCP things, be as specific as possible, ie, what you're trying to
do, why you're trying to do it, etc.
* For OSCP, don't be specific at all. Be super vague and nondescriptive so as
to not give anything away. Ask generic questions to get generic answers.    
* Assume that everyone that asks you a question is from offsec and is looking
to make you slip information.
* Basic OpSec: don't reveal anything to anyone without a super good reason.

# Part 19
* A note for the lab report: you only need ten machines well-documented. More
will not add more points to the score, though documenting more will provide 
more practice in documentation.
* Getting back into the saddle after not touching the tools for some time
leaves one a bit rusty.

# Part 20 
* Rereading lab reports can be helpful to re-establish one's mindset and 
approach
* Reviewing the lab material is helpful as well
* Check out the linked pentest cheatsheet that details all of the various
tools and such that are good resources for pentesting 

# Part 21
*  
