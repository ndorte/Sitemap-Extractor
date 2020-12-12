filename = "sitemap.xml"

with open(filename, "r", encoding="utf-8") as sitemap:
    for url in sitemap.readlines():
        if "<loc>" in url:
            urlstrip = url.strip()

            # if you want include domain use this line
            print (urlstrip[5:-6])

            # if you want exclude domain use this line
            #domain = "https://example.com"
            #rep = urlstrip.replace(domain,"")
            #print(rep[5:-6])

        else:
            continue
