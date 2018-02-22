---
# The default content type is "page": https://gohugo.io/templates/lookup-order/#hugo-layouts-lookup-rules
# Problem is, that means the layout that gets selected from the home page is page/list.html, which lists pages, not posts.
# By changing the content type of the index page to "post", Hugo will use post/list.html, which is what we want.
type: "post"
---
