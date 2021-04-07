from GoogleNews import GoogleNews

hyperlink_format = '<a href="{link}">{text}</a><p>'
out = f = open("searchresults.html", "w")

def initFile(f):
    initFile = open("initFile.html")
    for char in initFile:
        out.write(char)

searchParams = {'"Brand New Bundestag"', "Lu Yen Roloff", "Kassem", "Franka Kretschmer", "Dr. Franka Kretschmer", "Armand Zorn", "Ed Greve", "Rasha Nasr", "Kassem Taher Saleh", "Kassem Saleh", "Paul Schilling", "Zandile Ngono", "Philippa Sigl-Glöckner"}
def newsScraper(language, period, searchParams):
    googlenews = GoogleNews()
    googlenews = GoogleNews(period=period)
    googlenews = GoogleNews(encode='utf-8')
    googlenews.set_lang(language)
    for param in searchParams:
        f.write("<button type=\"button\" class=\"btn btn-info\" data-toggle=\"collapse\" data-target=\"#"+param.replace(" ", "") + "\">Here are the reseluts for: " +param +"</button>"
 + "<div id=\"" + param.replace(" ", "").replace("\"", "") + "\">")
        searchREsults = googlenews.search(param)
        searchResultsLinks = googlenews.get_links()
        searchResultsText = googlenews.get_texts()
        for text, link in zip(searchResultsText, searchResultsLinks):
            f.write(hyperlink_format.format(link=link, text=text) + "\n")
            print(link)
        i = 2
        while len(searchResultsLinks) == 10:
            googlenews.get_page(i)

            searchResultsLinks = googlenews.get_links()
            searchResultsText = googlenews.get_texts()
            for text, link in zip(searchResultsText, searchResultsLinks):
                f.write(hyperlink_format.format(link=link, text=text))
                print(link)
            i += 1
        f.write("</div>")
        googlenews.clear()
    f.write("</div>")

initFile(f)
newsScraper("de", "7d", searchParams)
f.close()