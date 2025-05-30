# Development Workflow
{% if MDBOOK_VIEW %}
First, start bootkon as if you were a participant (see [Labs](../labs/main.md)). Next, open this file in Cloud Shell:

```
bk-tutorial docs/book/contributing.md
```

Continue the next sections in the Cloud Shell tutorial.

{% else %}
## Continue in Cloud Shell

Hi, press `START`.

{% endif %}

## Authenticate to GitHub

Cloud Shell editor supports authentication to GitHub via an interactive authentication flow.
In this case, you just push your changes and a notification appears to guide you through this process. If you go this route, please continue with **Set up git**.

If, for some reason, this doesn't work for you, you can use the following method:

Create SSH keys if they don't exist yet (just hit return when it asks for passphrases):
```bash
test -f ~/.ssh/id_rsa.pub || ssh-keygen -t rsa
```

Display your newly created SSH key and [add it to your GitHub account](https://github.com/settings/keys):
```bash
cat ~/.ssh/id_rsa.pub
```

Overwrite the remote URL to use the SSH protocol insead of HTTPS. Adjust the command in case you are working on your personal fork:
```bash
git remote set-url origin git@github.com:fhirschmann/bootkon.git
```

## Set up git

```bash
git config --global user.name "John Doe"
```
```bash
git config --global user.email johndoe@example.com  
```

Check your git config:
```bash
cat ~/.gitconfig
```

## Pushing to GitHub

You can now commit changes and push them to GitHub. You can either use the version control of the Cloud Shell IDE (tree icon on the left hand side) or the command line:

```bash
git status
```

## Set up your development environment

During the first lab, participants are asked to edit `vars.sh`. It is suggested to make a copy of this file and not touch the original in order not to accidently commit it to git.

First, make a copy:
```bash
cp vars.sh vars.local.sh
```

And <walkthrough-editor-open-file filePath="vars.local.sh">edit it</walkthrough-editor-open-file>. It also runs on Argolis (for Google employees).

Next, source it:
```bash
. vars.local.sh
```

Note that the init script (`bk`) automatically loads `vars.local.sh` the next time and `vars.local.sh` takes presendence over `vars.sh`.

## Reloading the tutorial

You can reload a lab on-the-fly by typing `bk-tutorial` followed by the lab markdown file into the terminal and pressing return. Let's reload
this tutorial:
```bash
bk-tutorial docs/book/contributing.md
```

## Working with mdbook

You can run mdbook and compile the book in Cloud Shell directly. First, install dependencies:
```bash
pip install jinja2 nbformat nbconvert
```

Next, run mdbook:
```bash
bk-mdbook
```

You can now read the book using Cloud Shell's web preview by pressing the ![](https://cloud.google.com/static/shell/docs/images/web_preview.svg) button in Cloud Shell. Select **Preview on port 8080**. As soon as you change any of the markdown source files, mdbook will automatically reload it.