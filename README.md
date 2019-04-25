# A simple script to get your TODO list from Trello in Conky
1. Install the requirements:
    ```bash
    sudo python3 -m pip install -r requirements.txt
    ```
2. Run the script, it will generate a template config file in `~/.config/tonk`. Edit this file to fill out the `api_key` and `token` which you can get from [Trello](https://trello.com/app-key).
3. Fill in the board and list ID's which you can get by going to your Trello board and appending `".json"` to the end of the URL (Hit the collapse all button and look at the `board` and `lists` attributes)
4. Edit your `~/.conkyrc` to contain the following:
```
${execpi 300 path/to/tonk.py}
```
> The script relies on conky parsing it's output, hence the `execpi`. I would recommend leaving the interval high as it's quite intensive.
5. Pray to Linus that it all works. If stuff breaks try the following (In order):
   * Run conky from a terminal and check that it doesn't fail to run the script - if it does check that the       script file is in your $PATH.
   * Run the script in a terminal. It should print the data from the lists you supplied, check the [issues](#issues) to see if your crash is mentioned.
   * If all else fails create an issue, try to include as much useful information as you can so that I can try to help.
## Usage
```ruby
tonk.py [end]

end - The final string to print, by default this is "${color white}"
to reset the formatting used by the script
```
## Notes/TODO
* Implement proper argparse
* Support for multiple boards? Did not think it was worth implementing.

## Issues
* Will throw exception if api_key is not filled in and `api.toml` doesn't exist in $PWD, make sure you've filled out the config file if this occurs.