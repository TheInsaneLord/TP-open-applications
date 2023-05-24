
# TP Open Applications

This consists of two scripts the applacations script and the web script both of wich work difrently for each other as the web script will only be able to open web pages using a URL to the needed page and the applacation script will open the apps that you want it to

this script was inspiered by one found the linux alpha but using Python instead as it is a langage that most users can be easly understand this was also created as a few users were having the issue with opening app on the linux vertion of Touch Portal and noticing that the bash scripts worked I felt that i should share the script I use to open apps an web pages

## Acknowledgements

 - Touchportal Team and the users on the linux alpha build
 - @Pro-tato#9999 who inspiered thsi script and made a vertion of the script in java
## How to install it and set it up

to install this script run the following commands in a terminal
```shell
git clone https://github.com/TheInsaneLord/TP-open-applications.git
cd TP-open-applications
```
it is recomended puting the tp-scripts folder some ware handay such as the documents folder

```shell
mv tp-scripts/ ~/Documents
cd ~/Documents/tp-scripts/

```
### Setting up custom apps
- the next step is adding your own apps to the script as evryone will be using difrent apps you need to find out the command that opens the spesific app you are wanting to open this comand can be found from the desktop shortcut right click the desktop shortcut and open with your favorit text edditor then look for something like this
```shell
Exec=/usr/bin/discord
```
- now that you have the command that opens the app run it in a terminal to confirm that it works right if it desent you will need to find another way to open the app using a command. 

- Now the you have the command edit the `launch_apps.py` **don't eddit the script files all they do is runn the command need to make this work** the only section in `launch_apps.py` you should need to eddit in in the commands list to do theis add the filowing to the list for this example discord will be used.
``` python
'discord' : '/usr/bin/discord'
```
- the cammands list should now look something like this:
``` python
commands = {
    'a': 'echo test works', # test if it works
    'discord' : '/usr/bin/discord'
}
```
- you can test if the script works by running the following command:
```shell
bash touchportal-app-launch.sh discord #this will open discord 
bash touchportal-app-launch.sh a #this will run the test command
```
### Setting up the web launch
this script works the same as the as the app one however you will only need to set the browser if you dont use firefox or chrome to do so addit the same way you would an applacation

```python
`browser` : `<command to open it>`
```

to use this script to open a page all that is need is to run the following command:
```shell
bash touchportal-web-launch.sh <browser> <URL>
```

### Setting up the Touch Portal side
Now the scripts are in an easy to get to directoty and you have added your apps and configure the web script now you can manage all of them using short and easy to remember commands such as:

```shell
bash touchportal-app-launch.sh discord
bash touchportal-web-launch.sh 1 https://github.com/TheInsaneLord/TP-open-applications
```
if you know how to use scripts with touch portal all you don't need to follow thses steps as you alredy know what to do
- add yout button
- select the run & open drop down
- select the script you want to use 
- the scrip will need the arguments you want to use the  short name for the app you added to the python file
- thats it the scrip will open the app or web page you want 

## My Socials

- Github [TheInsaneLord](https://github.com/TheInsaneLord)
- Twitch [the_insane_lord](https://www.twitch.tv/the_insane_lord)
- Twitter [@TheInsane_L](https://twitter.com/TheInsane_L)

## FAQ

#### Can I modify the code to fit my needs?
Yes, you can modify it as needed. However, if you plan to redistribute it, please provide credit where it is due.

#### Will this script work without Touch Portal?
Yes, since it is a bash script, it can work outside of Touch Portal.

#### Will I have to modify the web script to make it work?
This depends on your system. For example, if you don't have Firefox installed, you will need to modify the section of the script related to Firefox and set it to use your browser.

#### How do I know if there is an error?
You can check for errors in the script by using the built-in debugging feature in Touch Portal. Alternatively, if you run the script outside of Touch Portal in a terminal, any errors will be displayed there.
