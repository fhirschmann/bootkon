<walkthrough-metadata>
  <meta name="title" content="Data & AI Bootkon" />
  <meta name="description" content="These labs include detailed step-by-step instructions to guide you. In addition to the labs, you’ll face several challenges that you’ll need to solve on your own or with your group. Groups will be assigned by the event organizers at the start of the event." />
  <meta name="keywords" content="data, ai, bigquery, vertexai, genai, notebook" />
  <meta name="component_id" content="1734803" />
</walkthrough-metadata>


# Data and AI Bootkon

## Introduction

{% if MY_NAME %}Hi **{{ MY_NAME }}!** {% endif %}Welcome to Data & AI Bootkon. We're delighted to have you! This sidebar contains parts of the labs you will work through. Before we get started, let's set up a few things:

### Working with labs

You can insert commands into the terminal using the following button on top of each code line in the tutorial:
<walkthrough-cloud-shell-icon></walkthrough-cloud-shell-icon>. The button will automatically open the terminal.
Please make sure you are using the terminal of the IDE.

Let's try:

```bash
echo "I'm ready to get started."
```

Execute by pressing the return key in the terminal that has been opened in the lower part of your screen.

### Setting environment variables
You can open files directly from this tutorial.
Open `vars.sh` <walkthrough-editor-open-file filePath="vars.sh">by clicking here</walkthrough-editor-open-file>
and set `GCP_USERNAME`, `PROJECT_ID` according to the piece of paper you received. Also let us know your (first?) name in `MY_NAME`. Don't forget to save it.

Please reload bootkon:

```bash
. bk
```


And restart the tutorial using the next command. You can also use the next command to continue bootkon in case you accidentally close the tutorial or the editor:

```bash
bk-start
```

Now, your

* `PROJECT_ID` is `{% if PROJECT_ID == "" %}None{% else %}{{ PROJECT_ID }}{% endif %}`

* `GCP_USERNAME` is `{% if GCP_USERNAME == "" %}None{% else %}{{ GCP_USERNAME }}{% endif %}`.


If neither is `None`, press the `START` button below to get started!

{% include 'labs/1_environment_setup.md' %}

{% include 'labs/2_data_ingestion.md' %}

{% include 'labs/3_dataform.md' %}

{% include 'labs/4_ml.md' %}

{% include 'labs/5_dataplex.md' %}
