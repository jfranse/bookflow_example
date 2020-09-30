# BookDown Limitations and Future Plans

## TODO'S BEFORE PUBLISHING

- check out pdf and latex export
- write something about Literal Programming. If I'm seperating the code and the document, I'm sort of going away from Literal Programming. Perhaps if Jupter Book has really good caching, it may also understand that not all results have to be re-run? Hmm...
- suggestions about the workflow in a project. Multiple documents, literal programming, git repos, etc.
- something about other solutions to make notebooks actually nice (and perhaps are also better at literal programming)

## Literal Programming

Literal Programming (sometimes also known as Literal Statistical Programming) is the principle that your code and documentation are the same file, and specifically that the document is written in natural language following human logical flow, interspersed with the code. Yes, notebooks (mathematica and jupyter) are examples of this. 

The principle is very elegant and makes a lot of sense. It forces one to think and reason 'out-loud' about their code, and produces the best possible documentation pretty much by definition. However in practice jupyter notebooks are just not that great as soon as either the code or the document become large.

It therefore pains me a little bit that BookFlow very deliberately separates the code and the document, ironically using a literal programming tool to move even further away from it. But it does provide some clear advantages, and most people don't practice literal programming anyway. This is a subject, however, that I might return to. 

## Slides and presentations

Your results don't just end up in report, you also want to put them in slides. I'm not sure to what degree it will be possible to create slides with Jupyter Book. Perhaps LaTeX Beamer slides might work, and I might look into that at some point. Powerpoint I don't know if I even want to think about. 

Some of the existing tools to convert jupyter notebooks to slides may help, but whatever it is it must pass through Jupyter Book *first*. That's where the glueing of the variables, figures and other references happens. 

## Collaborating with Overleaf

Apparently since I left academia lots of people started using overleaf to collaborate on their LaTeX documents. I've read you can sync overleaf with github repo's, so there might be a way to do this. Updating towards overleaf will be easier than getting the changing from overleaf into the source, since the latex files are *created* by Jupyter Book. It will probably require some work to figure this out as well.