Brandon Randle
2016 November 1
HW3 - OSCP: Prelim

## Part 1
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

## Part 2
* In preparation for getting in the proper mindset, download and try to break
vulnerable virutal machines.
* Speaker says he tends to think either too narrowly or too deeply. One needs
to keep one's mind open to the possibilities. 
* Speaker dislikes the idea of bruteforcing, saying that it lacks skill and
finesse.
