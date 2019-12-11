# foconnect
foconnect codebase

### Setup
___

Open a Terminal
    
    =========
    On MacOS
    =========
    1. Press: Command + Space
    2. Type: Terminal
    3. Double Click: Icon 
    
    ===========
    On Windows:
    =========== 
    1. Press: Win + R
    2. Type: cmd
    3. Press: Enter
    
Create Sandbox

    $ mkdir sandbox
    $ cd sandbox
    
Clone the codebase

    $ git clone https://github.com/sgpy/foconnect.git
    $ cd foconnect
    $ git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
    $ git fetch --all
    $ git pull --all
    
Checkout the resources for your region (Singapore/HongKong/Tokyo)
    
    $ git checkout Singapore
    
