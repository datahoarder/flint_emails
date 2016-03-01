# Flint Emails

A repository collecting, transcribing, and maybe parsing the publicly-released emails in the Flint water scandal.

Currently, Governor Rick Snyder is releasing the emails and other documents here:

[http://www.michigan.gov/snyder](http://www.michigan.gov/snyder)

Here's the [Wikipedia entry on the Flint crisis](https://en.wikipedia.org/wiki/Flint_water_crisis).

A [Virginia Tech-based research group](https://www.washingtonpost.com/news/inspired-life/wp/2016/01/26/meet-the-heroic-professor-who-helped-uncover-the-flint-lead-water-crisis/) has been doing fantastic work in exposing Flint's poisoned water: [they have a great list of press coverage](http://flintwaterstudy.org/articles-in-the-press/).




# Current status

- All known documents listed in [docs.yaml](docs.yaml)
- All known documents downloaded to [docs/originals](docs/originals)
- All known documents pushed to Github

## Todo

- Run ABBYY on documents that need them
- Run pdftotext on all OCRed PDFs
- wget archive the whole site at http://www.michigan.gov/snyder
- Upload stuff to [DocumentCloud](https://documentcloud.org)



### Trying out Git LFS

Since the PDFs are so large (up to 400+MB in size), this is a good chance to test out Github's support of [Large File Storage (LFS)](https://git-lfs.github.com/), which I initiated with:

        $ git lfs track "*.pdf"
        $ git add *.pdf
        $ git commit -m 'pdfs'
        $ git push
        DN0a22359a:flint_emails dtown$ git push
        Git LFS: ( of 24 files) 126.96 MB / 1.80 GB   
