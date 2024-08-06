# Android-Cached-Sensitives

android-cached-sensitives is a tool for mobile application pentesters, checking for the sensitive data being leaked in the /data/data/com.example.app directory/files.

# Installation:

- You need to install python3 (Any Version) im using 3.10 currently :D

```
git clone https://github.com/SirBugs/android-cached-sensitives.git
```

- Add the following line into your ~/.profile ```alias android-cached-sensitives="python3.10 /Users/xXxXx/Tools/android-cached-sensitives/main.py"```
- Don't forget to run: ```source ~/.profile```
- Now call ```android-cached-sensitives```, It shoudl be called normally :D

# How To Use?

- First of all, we need to pull the data/data/com.example.app of the targetted application via running: ```adb pull /data/data/com.example.app ./```
- Now cd com.example.app, run ```android-cached-sensitives```

```
usage: main.py [-h] (-c CONFIG | -t TEXT)
main.py: error: one of the arguments -c/--config -t/--text is required
```

- We can use -t to search for single, specific text
- Using -c --config needs submission of a ```.json``` file contains the patterns like:

```
{
    "phone": "010x0x0x4x9",
    "balance": "4,250",
    "PIN": "151515"
}
```

- The output will be something like this:

   ![Output](images/output.png)

Made with love in Egypt, By @SirBugs :D

Best Regards.
