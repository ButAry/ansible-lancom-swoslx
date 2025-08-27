# Ansible documentation style guide

## Linguistic guidelines

We want the Ansible documentation to be:
- clear
- direct
- conversational
- easy to translate 

We want reading the docs to feel like having an experienced, friendly colleague explain how Ansible works.

### Stylistic cheat-sheet

This cheat-sheet illustrates a few rules that help achieve the “Ansible tone”:

| Rule | Good example | Bad example |
| --- | --- | --- |
| Use active voice | You can run a task by | A task can be run by |
| Use the present tense | This command creates a | This command will create a |
| Address the reader | As you expand your inventory | When the number of managed nodes grows |
| Use standard English | Return to this page | Hop back to this page |
| Use American English | The color of the output | The colour of the output |

### Title and heading case

Titles and headings should be written in sentence case.  
For example, this section’s title is `Title and heading case`, not `Title and Heading Case` or `TITLE AND HEADING CASE`.

### Avoid using Latin phrases

Latin words and phrases like `e.g.` or `etc.` are easily understood by English speakers.  
They may be harder to understand for others and are also tricky for automated translation.

Use the following English terms in place of Latin terms or abbreviations:

| Latin | English |
| --- | --- |
| i.e | in other words |
| e.g. | for example |
| etc | and so on |
| via | by/ through |
| vs./versus | rather than/against |

## reStructuredText guidelines

The Ansible documentation is written in reStructuredText and processed by Sphinx. We follow these technical or mechanical guidelines on all rST pages:

### Heading notation

Section headings in `reStructuredText` can use a variety of notations. Sphinx will ‘learn on the fly’ when creating a hierarchy of headings.  
To make our documents easy to read and to edit, we follow a standard set of heading notations.  
We use:

- `###` with overline, for parts:
  ```
  ###############
  Developer guide
  ###############
  ```

- `***` with overline, for chapters:
  ```
  *******************
  Ansible style guide
  *******************
  ```

- `===` for sections:
  ```
  Mechanical guidelines
  =====================
  ```

- `---` for subsections:
  ```
  Internal navigation
  -------------------
  ```

- `^^^` for sub-subsections:
  ```
  Adding anchors
  ^^^^^^^^^^^^^^
  ```

- `"""` for paragraphs:
  ```
  Paragraph that needs a title
  """"""""""""""""""""""""""""
  ```

### Syntax highlighting - Pygments

The Ansible documentation supports a range of Pygments lexers for syntax highlighting to make our code examples look good.  
Each code-block must be correctly indented and surrounded by blank lines. 
The Ansible documentation allows the following values:

- none (no highlighting)
- ansible-output (a custom lexer for Ansible output)
- bash
- console
- csharp
- diff
- ini
- jinja
- json
- md
- powershell
- python
- rst
- sh
- shell
- shell-session
- text
- yaml
- yaml+jinja

For example, you can highlight Python code using following syntax:

``` python
.. code-block:: python

  def my_beautiful_python_code():
      pass
```

### Internal navigation

Anchors (also called labels) and links work together to help users find related content.  
Local tables of contents also help users navigate quickly to the information they need. All internal links should use the `:ref:` syntax.  
Every page should have at least one anchor to support internal `:ref:` links. Long pages, or pages with multiple levels of headings, can also include a local TOC.

Note:
```
Avoid raw URLs. RST and sphinx allow `https://myw.example.com`, but this is unhelpful for those using screen readers.  
`:ref:` links automatically pick up the heading from the anchor, but for external links, always use the `link title <link-url>`_ format.
```

#### Adding anchors

- Include at least one anchor on every page
- Place the main anchor above the main heading
- If the file has a unique title, use that for the main page anchor `.. \_unique_page::`
- You may also add anchors elsewhere on the page

#### Adding internal links

- All internal links must use `:ref:` syntax. These links both point to the anchor defined above:
  ```
  :ref:`unique_page`
  :ref:`this page <unique_page&gt>`
  ```

The second example adds custom text for the link.

#### Adding links to modules and plugins

Use the `:ansplugin:` RST role to link to modules and plugins using their Fully Qualified Collection Name (FQCN):

The ansible.builtin.copy module can be linked with:
```
:ansplugin:`ansible.builtin.copy#module`
```

If you want to specify an explicit type, use:
```
:ansplugin:`the copy module <ansible.builtin.copy#module>`
```

This displays as “The ansible.builtin.copy module can be linked with `ansible.builtin.copy`" and 
“If you want to specify an explicit type, use: `the copy module`".

Instead of `#module`, you can also specify `#<plugin_type>` to reference to a plugin of type `<plugin_type>`:
```
:ansplugin:`arista.eos.eos_config <arista.eos.eos_config#module>`
:ansplugin:`kubernetes.core.kubectl connection plugin <kubernetes.core.kubectl#connection>`
:ansplugin:`ansible.builtin.file lookup plugin <ansible.builtin.file#lookup>`
```
Note

`ansible.builtin` is the FQCN for modules included in ansible-core.

#### Adding links to module and plugin options and return values

Use the `:ansopt:` and `:ansretval:` roles to reference options and return values of modules and plugins:
- ``` :ansopt:`ansible.builtin.file#module:path` ``` references the ``` ``path`` ``` parameter of the ``` ``ansible.builtin.file`` ``` module.  
- ``` :ansopt:`ansible.builtin.file#module:path=/root/.ssh/known_hosts` ``` shows the assignment ``` ``path=/root/.ssh/known_hosts`` ``` as a clickable link.
- ``` :ansretval:`ansible.builtin.stat#module:stat.exists` ``` references the ``` ``stat.exists`` ``` return value of the ``` ``ansible.builtin.stat`` ``` module.  
- You can also use ``` ``=`` ``` as for option values: ```:ansretval:`ansible.builtin.stat#module:stat.exists=true` ``` shows ``` ``stat.exists=true`` ```.
- ``` :ansopt:`foo` ``` and ```:ansopt:`foo=bar` ``` use the same markup for an option and an option assignment without a link; the same is true for return values: ```:ansretval:`foo` ``` and ```:ansretval:`foo=bar` ```.

This displays as:
- "`path` references the `path` parameter of the `ansible.builtin.file` module; `path=/root/.ssh/known_hosts` shows the assignment `path=/root/.ssh/known_hosts` as a clickable link."
- "`stat.exists` references the `stat.exists` return value of the `ansible.builtin.stat` module. You can also use `=` as for option values: `stat.exists=true` shows `stat.exists=true`."
- "`foo` and `foo=bar` use the same markup for an option and an option assignment without a link; the same is true for return values: `foo` and `foo=bar`."

For both option and return values, `.` is used to reference suboptions and contained return values. Array stubs (`[...]`) can be used to indicate that something is a list.  
For example the `:retval:` argument ```ansible.builtin.service_facts#module:ansible_facts.services['systemd'].state``` references the `ansible_facts.services.state` return value of the `ansible.builtin.service_facts` module ```(ansible_facts.services['systemd'].state])```

#### Adding local TOCs

The page you’re reading includes a local TOC. If you include a local TOC:
- place it below, not above, the main heading and (optionally) introductory text
- use the `:local:` directive so the page’s main heading is not included
- do not include a title

The syntax is:
```
.. contents::
   :local:
```

## Markdown guidelines

Some Ansible ecosystem documentation is written in markdown and processed by mkdocs. We follow these technical or mechanical guidelines on all .md pages:

### Heading notation

Section headings in markdown can use a variety of notations. To make our documents easy to read and to edit, we follow a standard set of heading notations. We use:

- `#` for page titles:
  ```    
  # Installation
  ```
  
- `##` for section headings:
  ```
  ## Installing on Linux
  ```

Subsections add an additional `#` for each subsection. We recommend not going beyond `####` as that suggests a deeply nested document that could present better as multiple pages.

### Linking in Markdown

Using Mkdocs, you can format internal links <https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown> using the file name of the local file instead of an external URL.
`[configuration](/configuration)`

You can also link directly to a heading within a file Use the lower-case form of the heading.
`[dependency](/configuration/#dependency)`

External links use a similar format with the external URL.
`[Ansible Documentation](https://docs.ansible.com)`

### Code blocks

Markdown supports code blocks in the following format.
````
```text
docs/
    index.md
    user-guide/getting-started.md
    user-guide/configuration-options.md
    license.md
```
````

## Accessibility guidelines

Ansible documentation has a goal to be more accessible. Use the following guidelines to help us reach this goal.

### Images and alternative text

Ensure all icons, images, diagrams, and non text elements have a meaningful alternative-text description. Do not include screen captures of CLI output. Use a code block instead.

To add alt text in rst:
```
.. image:: path/networkdiag.png
   :width: 400
   :alt: SpiffyCorp network diagram
```

To add alt text in md:
```
![SpiffyCorp network diagram](path/networkdiag.png)
```

### Links and hypertext

URLs and cross-reference links have descriptive text that conveys information about the content of the linked target.  
See `Internal navigation` for how to format links in RST and see `Linking in Markdown` for Markdown.

### Tables

Tables have a simple, logical reading order from left to right, and top to bottom. Tables include a heading row and avoid empty or blank table cells.  
Label tables with a descriptive title.

For RST:
```
.. table:: File descriptions
  +----------+----------------------------+
  |File      |Purpose                     |
  +==========+============================+
  |foo.txt   |foo configuration settings  |
  +----------+----------------------------+
  |bar.txt   |bar configuration settings  |
  +----------+----------------------------+
```

For Markdown:
```
#### File descriptions
  |File       |Purpose                     |
  |---------- | -------------------------- |
  |foo.txt    | foo configuration settings |
  |bar.txt    | bar configuration settings |
```

### Colors and other visual information

- Avoid instructions that rely solely on sensory characteristics. For example, do not use `Click the square, blue button to continue.`
- Convey information by methods and not by color alone.
- Ensure there is sufficient contrast between foreground and background text or graphical elements in images and diagrams.
- Instructions for navigating through an interface make sense without directional indicators such as left, right, above, and below.
