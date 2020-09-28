# BookDown Limitations and Future Plans

## TODO'S BEFORE PUBLISHING

- check out pdf and latex export
- write something about Literal Programming. If I'm seperating the code and the document, I'm sort of going away from Literal Programming. Perhaps if Jupter Book has really good caching, it may also understand that not all results have to be re-run? Hmm...
- suggestions about the workflow in a project. Multiple documents, literal programming, git repos, etc.
- something about other solutions to make notebooks actually nice (and perhaps are also better at literal programming)

## Literal Programming

Literal Programming (sometimes also known as Literal Statistical Programming) is the principle that your code and your documentation are in the same place. Yes, notebooks (mathematica and jupyter) are examples of this. 

I am a big fan of this principle, but in practice jupyter notebooks are just not that great as soon as either the code or the document becomes large. 

## Slides and presentations

Your results don't just end up in report, you also want to put them in slides. I'm not sure to what degree it will be possible to create slides with Jupyter Book. Perhaps LaTeX Beamer slides might work, and I might look into that at some point. Powerpoint I don't know if I even want to think about. 

Some of the existing tools to convert jupyter notebooks to slides may help, but whatever it is it must pass through Jupyter Book *first*. That's where the glueing of the variables, figures and other references happens. 

## Collaborating with Overleaf

Apparently since I left academia lots of people started using overleaf to collaborate on their LaTeX documents. I've read you can sync overleaf with github repo's, so there might be a way to do this. Updating towards overleaf will be easier than getting the changing from overleaf into the source, since the latex files are *created* by Jupyter Book. It will probably require some work to figure this out as well.